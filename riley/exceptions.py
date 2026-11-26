class RileyError(Exception):
    """Base exception for recoverable Riley errors."""


class ConfigurationError(RileyError):
    """Raised when configuration cannot be validated."""


class BackendError(RileyError):
    """Raised when a conversation backend cannot respond."""


class SpeechInputError(RileyError):
    """Raised when speech cannot be captured or recognized."""


class VoiceOutputError(RileyError):
    """Raised when speech output fails."""
