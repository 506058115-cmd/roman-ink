#!/usr/bin/env python3
"""Convert between integers and canonical Roman numerals."""

import argparse
import sys


VALUES = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
)


def to_roman(value):
    if not 1 <= value <= 3999:
        raise ValueError("integer must be between 1 and 3999")
    result = []
    for amount, numeral in VALUES:
        count, value = divmod(value, amount)
        result.append(numeral * count)
    return "".join(result)


def from_roman(text):
    numeral = text.upper()
    if not numeral or any(char not in "IVXLCDM" for char in numeral):
        raise ValueError("Roman numeral must contain only I, V, X, L, C, D, and M")
    values = {symbol: amount for amount, symbol in VALUES if len(symbol) == 1}
    total = 0
    for index, char in enumerate(numeral):
        current = values[char]
        if index + 1 < len(numeral) and values[numeral[index + 1]] > current:
            total -= current
        else:
            total += current
    if not 1 <= total <= 3999 or to_roman(total) != numeral:
        raise ValueError("Roman numeral is not in canonical form")
    return total


def main():
    parser = argparse.ArgumentParser(description="Convert integers and canonical Roman numerals.")
    subparsers = parser.add_subparsers(dest="action", required=True)
    encoder = subparsers.add_parser("encode", help="convert an integer from 1 to 3999")
    encoder.add_argument("number", help="positive base-10 integer")
    decoder = subparsers.add_parser("decode", help="convert a canonical Roman numeral")
    decoder.add_argument("numeral", help="Roman numeral; lower-case is accepted")
    args = parser.parse_args()
    try:
        if args.action == "encode":
            if not args.number or any(char < "0" or char > "9" for char in args.number):
                raise ValueError("integer must contain decimal digits only")
            result = to_roman(int(args.number))
        else:
            result = from_roman(args.numeral)
    except ValueError as error:
        print(f"roman-ink: {error}", file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
