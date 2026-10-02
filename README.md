# roman-ink

Convert integers to Roman numerals and back. Decoding accepts only canonical subtractive notation, so forms such as `IIX` are rejected instead of silently interpreted.

## Use

Requires Python 3.10+; no packages to install.

```sh
python roman_ink.py encode 2026
python roman_ink.py decode MMXXVI
python roman_ink.py decode mcmxciv
```

The supported range is 1–3999. Lowercase input is accepted when decoding; output uses uppercase Roman numerals. Invalid, noncanonical, zero, and out-of-range values return a concise error.

## License

MIT
