#!/usr/bin/env node
/**
 * Syncs Astryx Design System assets (@astryxdesign/core + @astryxdesign/theme-neutral)
 * into riley/static/astryx.css for zero-runtime serving by riley.web.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const coreResetPath = path.join(rootDir, "node_modules/@astryxdesign/core/src/reset.css");
const neutralThemePath = path.join(rootDir, "node_modules/@astryxdesign/theme-neutral/dist/theme.css");
const corePkgPath = path.join(rootDir, "node_modules/@astryxdesign/core/package.json");
const outPath = path.join(rootDir, "riley/static/astryx.css");

const corePkg = JSON.parse(fs.readFileSync(corePkgPath, "utf8"));
const resetCss = fs.readFileSync(coreResetPath, "utf8").trim();
const neutralThemeCss = fs.readFileSync(neutralThemePath, "utf8").trim();

const astryxButtonBaseCss = `
@layer astryx-base {
  :root {
    --spacing-0: 0rem;
    --spacing-0-5: 0.125rem;
    --spacing-1: 0.25rem;
    --spacing-1-5: 0.375rem;
    --spacing-2: 0.5rem;
    --spacing-3: 0.75rem;
    --spacing-4: 1rem;
    --spacing-5: 1.25rem;
    --spacing-6: 1.5rem;
    --spacing-7: 1.75rem;
    --spacing-8: 2rem;
    --spacing-9: 2.25rem;
    --spacing-10: 2.5rem;
    --spacing-11: 2.75rem;
    --spacing-12: 3rem;

    --size-element-sm: 28px;
    --size-element-md: 32px;
    --size-element-lg: 36px;

    --border-width: 1px;

    --focus-outline-width: 2px;
    --focus-outline-style: solid;
    --focus-outline-color: var(--color-accent);
    --focus-outline-offset: 3px;

    --font-weight-normal: 400;
    --font-weight-medium: 500;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;

    --ease-standard: cubic-bezier(0.24, 1, 0.4, 1);
    --ease-entrance: cubic-bezier(0.24, 1, 0.4, 1);
    --ease-move: cubic-bezier(0.24, 1, 0.4, 1);
    --ease-exit: cubic-bezier(0.3, 0, 0.6, 0.6);
  }

  /* Astryx Button, IconButton & ToggleButton (@astryxdesign/core Button.tsx / ToggleButton.tsx) */
  .astryx-button {
    --button-focus-offset: var(--focus-outline-offset);
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: var(--spacing-2);
    padding-block: var(--spacing-2);
    padding-inline: var(--spacing-3);
    border-width: 0;
    border-style: none;
    border-radius: var(--_button-radius, var(--radius-element));
    font-family: inherit;
    font-size: var(--text-label-size);
    line-height: var(--text-label-leading);
    font-weight: var(--font-weight-medium);
    white-space: nowrap;
    min-width: 0;
    max-width: 100%;
    text-decoration: none;
    touch-action: manipulation;
    user-select: none;
    cursor: pointer;
    outline-width: 0;
    outline-style: none;
    outline-offset: 0;
    transform: scale(1);
    transition-property: background-image, background-color, border-color, color, opacity, transform;
    transition-duration: var(--duration-fast);
    transition-timing-function: var(--ease-standard);
  }

  .astryx-button:focus-visible {
    outline-width: var(--focus-outline-width);
    outline-style: var(--focus-outline-style);
    outline-color: var(--focus-outline-color);
    outline-offset: var(--button-focus-offset);
  }

  /* Sizes */
  .astryx-button[data-size="sm"] {
    height: max(var(--size-element-sm), 1lh);
    padding-block: var(--spacing-1);
    padding-inline: var(--spacing-2);
    font-size: var(--font-size-sm);
    gap: var(--spacing-1-5);
  }

  .astryx-button[data-size="md"] {
    height: max(var(--size-element-md), 1lh);
  }

  .astryx-button[data-size="lg"] {
    height: max(var(--size-element-lg), 1lh);
    padding-inline: var(--spacing-4);
  }

  /* IconButton (isIconOnly) */
  .astryx-button[data-icon-only="true"] {
    aspect-ratio: 1 / 1;
    padding-inline: 0;
    padding-block: 0;
    flex-shrink: 0;
    max-width: none;
  }

  .astryx-button[data-icon-only="true"][data-size="sm"] {
    width: var(--size-element-sm);
    height: var(--size-element-sm);
  }

  .astryx-button[data-icon-only="true"][data-size="md"] {
    width: var(--size-element-md);
    height: var(--size-element-md);
  }

  .astryx-button[data-icon-only="true"][data-size="lg"] {
    width: var(--size-element-lg);
    height: var(--size-element-lg);
  }

  .astryx-button[data-width="full"] {
    width: 100%;
    justify-content: flex-start;
  }

  /* Variants */
  .astryx-button[data-variant="primary"] {
    background-color: var(--color-accent);
    color: var(--color-on-accent);
    --_button-fill: var(--color-accent);
    --_button-on-fill: var(--color-on-accent);
  }

  .astryx-button[data-variant="secondary"] {
    background-color: var(--color-neutral);
    color: var(--color-text-primary);
  }

  .astryx-button[data-variant="ghost"] {
    background-color: transparent;
    color: var(--color-text-primary);
  }

  .astryx-button[data-variant="destructive"] {
    background-color: var(--color-error);
    color: var(--color-on-error);
    --_button-fill: var(--color-error);
    --_button-on-fill: var(--color-on-error);
  }

  .astryx-button[data-variant="destructive"]:focus-visible {
    outline-color: var(--color-error);
  }

  /* Layered interaction overlays (interactionOverlay.stylex.ts) */
  @media (hover: hover) {
    .astryx-button:where(:not(:disabled, [aria-disabled="true"])):hover {
      background-image: linear-gradient(var(--color-overlay-hover), var(--color-overlay-hover));
    }

    .astryx-button:where(:not(:disabled, [aria-disabled="true"])):hover:active {
      background-image: linear-gradient(var(--color-overlay-pressed), var(--color-overlay-pressed));
    }
  }

  .astryx-button:where(:not(:disabled, [aria-disabled="true"])):active,
  .astryx-button[data-astryx-press="on"] {
    background-image: linear-gradient(var(--color-overlay-pressed), var(--color-overlay-pressed));
    transform: scale(0.98);
  }

  .astryx-button:disabled,
  .astryx-button[aria-disabled="true"] {
    opacity: 0.5;
    cursor: default;
    background-image: none;
    transform: none;
  }

  /* ToggleButton pressed state (ToggleButton.tsx) */
  .astryx-toggle-button[aria-pressed="true"],
  .astryx-toggle-button[data-is-pressed="true"] {
    background-color: var(--color-overlay-pressed);
    color: var(--color-text-primary);
  }

  .astryx-toggle-button[aria-pressed="true"] .astryx-button-label,
  .astryx-toggle-button[data-is-pressed="true"] .astryx-button-label {
    font-weight: var(--font-weight-semibold);
  }

  /* Internal layout slots (Button.tsx) */
  .astryx-button-content {
    display: flex;
    flex: 1 1 auto;
    align-self: stretch;
    flex-direction: inherit;
    align-items: center;
    justify-content: inherit;
    gap: inherit;
    min-width: 0;
    pointer-events: none;
  }

  .astryx-button-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 16px;
    height: 16px;
    pointer-events: none;
  }

  .astryx-button-icon svg {
    width: 16px;
    height: 16px;
    display: block;
  }

  .astryx-button-label {
    overflow: hidden;
    text-overflow: ellipsis;
    min-width: 0;
  }

  .astryx-button-end {
    display: inline-flex;
    align-items: center;
    margin-inline-start: auto;
    color: inherit;
    flex-shrink: 0;
  }

  /* Elevation levels */
  .astryx-button[data-elevation="low"] {
    box-shadow: var(--shadow-low);
  }

  .astryx-button[data-elevation="med"] {
    box-shadow: var(--shadow-med);
  }

  .astryx-button[data-elevation="high"] {
    box-shadow: var(--shadow-high);
  }

  /* Forced colors accessibility (WCAG 1.4.11) */
  @media (forced-colors: active) {
    .astryx-button[data-variant="primary"],
    .astryx-button[data-variant="secondary"],
    .astryx-button[data-variant="destructive"] {
      border-width: 1px;
      border-style: solid;
      border-color: ButtonText;
    }

    .astryx-button[data-variant="destructive"] {
      border-color: CanvasText;
    }

    .astryx-toggle-button[aria-pressed="true"] {
      forced-color-adjust: none;
      background-color: Highlight;
      color: HighlightText;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .astryx-button {
      transition-duration: 0s;
    }

    .astryx-button:active,
    .astryx-button[data-astryx-press="on"] {
      transform: scale(1);
    }
  }
}
`.trim();

const banner = `/*
 * @generated by scripts/sync-astryx.mjs from @astryxdesign/core@${corePkg.version}
 * and @astryxdesign/theme-neutral@${corePkg.version}.
 * Run \`npm run sync-astryx\` after upgrading Astryx packages.
 */`;

const output = `${banner}\n\n${resetCss}\n\n${astryxButtonBaseCss}\n\n${neutralThemeCss}\n`;
fs.writeFileSync(outPath, output, "utf8");
console.log(`Synced Astryx CSS (${output.length} bytes) -> ${path.relative(rootDir, outPath)}`);
