# Skill: Localization (L10n) & Internationalization (i18n) Audit

## Purpose
Ensure the application UI is resilient to different languages, character sets, and cultural formatting.

## Audit Areas
1. **String Length (Expansion)**: Test languages like German or Russian that often cause text overflow or button clipping.
2. **Character Sets**: Verify support for UTF-8, CJK (Chinese, Japanese, Korean), and special accents.
3. **Layout Resilience**: Check for layout breaks when text wraps or expands.
4. **Number/Date Formatting**: Validate currency symbols, date structures (DD/MM vs MM/DD), and decimal separators.

## Tools
- `playwright-browser_snapshot` (for layout analysis)
- `visual-regression` skill (for comparing UI across languages)
