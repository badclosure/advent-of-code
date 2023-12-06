import sys
from dataclasses import dataclass

example_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


@dataclass()
class Converter:
    low: int
    high: int
    delta: int

    def __repr__(self) -> str:
        return f"Conv[{self.low},{self.high}) {'+' if self.delta >= 0 else '-'} {abs(self.delta)}"


def converter_from_line(line: str) -> Converter:
    dst, src, range_ = [int(x) for x in line.split()]
    return Converter(src, src + range_, dst - src)


@dataclass()
class InputRange:
    low: int
    high: int

    def __add__(self, rhs: int):
        low = self.low + rhs
        high = self.high + rhs

        return InputRange(low, high)

    def __repr__(self) -> str:
        return f"Range[{self.low},{self.high})"


def intersect(irange: InputRange, conv: Converter):
    _converted = []
    _untouched = []
    conversion = True
    if irange.high <= conv.low or irange.low >= conv.high:
        _untouched = [irange + 0]
        conversion = False
    elif conv.low <= irange.low < conv.high and irange.high > conv.high:
        _converted = [InputRange(low=irange.low, high=conv.high) + conv.delta]
        _untouched = [InputRange(low=conv.high, high=irange.high)]
    elif conv.low < irange.high < conv.high and irange.low < conv.low:
        _converted = [InputRange(low=conv.low, high=irange.high) + conv.delta]
        _untouched = [InputRange(low=irange.low, high=conv.low)]
    elif conv.low <= irange.low and conv.high >= irange.high:
        _converted = [irange + conv.delta]
    elif irange.low < conv.low and irange.high >= conv.high:
        _converted = [InputRange(low=conv.low, high=conv.high) + conv.delta]
        _untouched = [
            InputRange(low=irange.low, high=conv.low),
            InputRange(low=conv.high, high=irange.high),
        ]
    else:
        print(irange, conv)
        raise ValueError("Not supposed to be happening")

    return (_converted, _untouched, conversion)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            content = f.read()
    else:
        content = example_input

    seeds, *mappings = content.split("\n\n")
    seeds = [int(s) for s in seeds[7:].split(" ")]
    seed_ranges = [InputRange(a, a + b) for a, b in zip(seeds[::2], seeds[1::2])]
    src2dst = [m.splitlines()[0][:-5].split("-to-") for m in mappings]
    mappings = [
        [converter_from_line(line) for line in m.splitlines()[1:]] for m in mappings
    ]

    current_ranges = seed_ranges

    for mapping_layer, [s, d] in zip(mappings, src2dst):
        new_ranges = []
        while len(current_ranges) > 0:
            irange = current_ranges.pop(0)
            for conv in mapping_layer:
                converted, untouched2, has_converted = intersect(irange, conv)
                new_ranges += converted[:]
                if has_converted:
                    current_ranges += untouched2[:]
                if len(converted) > 0:
                    break

            else:
                new_ranges.append(irange)

        current_ranges = new_ranges

    print(min([r.low for r in current_ranges]))
