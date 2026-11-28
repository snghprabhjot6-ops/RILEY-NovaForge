from __future__ import annotations

import ast
import operator
import math
import re
from collections.abc import Sequence
from datetime import datetime

from ..models import Message
from .base import ConversationBackend


TEXT = {
    "en": {
        "hello": "Hello! I'm Riley. How can I help you today?",
        "help": "I can chat, tell the date or time, do basic arithmetic, remember this conversation, listen, and speak.",
        "time": "The current time is {value}.", "date": "Today's date is {value}.",
        "thanks": "You're welcome!", "unknown": "I'm still learning. Try asking for the time, date, help, or a calculation.",
        "calculation": "The answer is {value}.", "calculation_error": "I couldn't safely calculate that expression.",
    },
    "hi": {
        "hello": "नमस्ते! मैं Riley हूँ। आज मैं आपकी कैसे मदद कर सकती हूँ?",
        "help": "मैं बातचीत कर सकती हूँ, तारीख या समय बता सकती हूँ, सामान्य गणना कर सकती हूँ, सुन सकती हूँ और बोल सकती हूँ।",
        "time": "अभी समय {value} है।", "date": "आज की तारीख {value} है।", "thanks": "आपका स्वागत है!",
        "unknown": "मैं अभी सीख रही हूँ। समय, तारीख, सहायता या गणना के बारे में पूछें।",
        "calculation": "उत्तर {value} है।", "calculation_error": "मैं इस अभिव्यक्ति की सुरक्षित गणना नहीं कर सकी।",
    },
    "fr": {
        "hello": "Bonjour ! Je suis Riley. Comment puis-je vous aider ?",
        "help": "Je peux discuter, donner la date ou l'heure, effectuer des calculs simples, écouter et parler.",
        "time": "Il est {value}.", "date": "Nous sommes le {value}.", "thanks": "Avec plaisir !",
        "unknown": "J'apprends encore. Demandez l'heure, la date, de l'aide ou un calcul.",
        "calculation": "La réponse est {value}.", "calculation_error": "Je n'ai pas pu calculer cette expression en toute sécurité.",
    },
    "bn": {
        "hello": "নমস্কার! আমি Riley। আজ কীভাবে সাহায্য করতে পারি?",
        "help": "আমি কথা বলতে, তারিখ বা সময় জানাতে, সাধারণ হিসাব করতে, শুনতে ও বলতে পারি।",
        "time": "এখন সময় {value}।", "date": "আজকের তারিখ {value}।", "thanks": "স্বাগতম!",
        "unknown": "আমি এখনও শিখছি। সময়, তারিখ, সাহায্য বা হিসাব সম্পর্কে জিজ্ঞাসা করুন।",
        "calculation": "উত্তর হলো {value}।", "calculation_error": "আমি নিরাপদে এই হিসাবটি করতে পারিনি।",
    },
    "sa": {
        "hello": "नमस्ते! अहं Riley अस्मि। कथं साहाय्यं करोमि?",
        "help": "अहं संवादं, समयं दिनाङ्कं च वक्तुं, सामान्यगणनां कर्तुं, श्रोतुं वक्तुं च शक्नोमि।",
        "time": "वर्तमानसमयः {value}।", "date": "अद्य दिनाङ्कः {value}।", "thanks": "स्वागतम्!",
        "unknown": "अहं अधुना शिक्षे। समयं, दिनाङ्कं, साहाय्यं गणनां वा पृच्छतु।",
        "calculation": "उत्तरम् {value}।", "calculation_error": "एतां गणनां सुरक्षिततया कर्तुं न शक्तवती।",
    },
    "es": {
        "hello": "¡Hola! Soy Riley. ¿Cómo puedo ayudarte hoy?",
        "help": "Puedo conversar, decir la fecha o la hora, hacer cálculos básicos, escuchar y hablar.",
        "time": "La hora actual es {value}.", "date": "La fecha de hoy es {value}.", "thanks": "¡De nada!",
        "unknown": "Todavía estoy aprendiendo. Pregunta por la hora, la fecha, ayuda o un cálculo.",
        "calculation": "La respuesta es {value}.", "calculation_error": "No pude calcular esa expresión de forma segura.",
    },
}

_BINARY = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Mod: operator.mod, ast.Pow: operator.pow}
_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _safe_calculate(expression: str) -> int | float:
    if len(expression) > 100:
        raise ValueError("Expression is too long")
    tree = ast.parse(expression, mode="eval")

    def bounded(value: int | float) -> int | float:
        if isinstance(value, complex) or abs(value) > 1_000_000_000_000 or not math.isfinite(value):
            raise ValueError("Result is outside the supported range")
        return value

    def evaluate(node: ast.AST) -> int | float:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in {int, float}:
            return bounded(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY:
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large")
            return bounded(_BINARY[type(node.op)](left, right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
            return bounded(_UNARY[type(node.op)](evaluate(node.operand)))
        raise ValueError("Unsupported expression")

    result = evaluate(tree)
    if isinstance(result, complex) or not math.isfinite(result) or abs(result) > 1_000_000_000_000:
        raise ValueError("Result is too large")
    return result


class LocalBackend(ConversationBackend):
    """Offline, deterministic conversational backend with a small intent set."""

    def generate(self, messages: Sequence[Message], language: str) -> str:
        phrases = TEXT.get(language, TEXT["en"])
        prompt = next((message.content.strip() for message in reversed(messages) if message.role == "user"), "")
        normalized = prompt.casefold()
        if re.search(r"\b(hello|hi|hey|bonjour|hola)\b", normalized) or any(word in normalized for word in ("नमस्ते", "নমস্কার")):
            return phrases["hello"]
        if any(word in normalized for word in ("help", "सहायता", "aide", "ayuda", "সাহায্য", "साहाय्य")):
            return phrases["help"]
        if any(word in normalized for word in ("thank", "धन्यवाद", "merci", "gracias", "ধন্যবাদ")):
            return phrases["thanks"]
        if any(word in normalized for word in ("time", "समय", "heure", "hora", "সময়")):
            return phrases["time"].format(value=datetime.now().strftime("%H:%M"))
        if any(word in normalized for word in ("date", "तारीख", "दिनाङ्क", "fecha", "তারিখ")):
            return phrases["date"].format(value=datetime.now().strftime("%Y-%m-%d"))

        match = re.search(r"(?:calculate|calc|what is|गणना|calcule|calcular|হিসাব)\s*[:：]?\s*([\d\s+\-*/().%]+)$", normalized)
        if match:
            try:
                value = _safe_calculate(match.group(1).strip())
                return phrases["calculation"].format(value=value)
            except (SyntaxError, ValueError, ZeroDivisionError, OverflowError):
                return phrases["calculation_error"]
        return phrases["unknown"]
