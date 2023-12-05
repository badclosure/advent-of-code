import re
import sys
import time
from dataclasses import dataclass
from typing import Tuple

from rich import print
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

with open(sys.argv[1]) as f:
    content = [line.strip() for line in f.readlines()]

pattern = re.compile(r"\d+")


@dataclass()
class Part:
    row: int
    cols: Tuple[int, int]
    value: int


parts = []

matches = [pattern.finditer(line) for line in content]
for row, matches_line in enumerate(matches):
    for m in matches_line:
        parts.append(Part(row, (m.start(), m.end()), int(m.group())))


# print(parts)


def generate_grid(part):
    output = ""
    c1, c2 = part.cols
    c1 = max(0, c1 - 1)
    c2 = min(len(content[0]), c2 + 1)
    for row, line in enumerate(content):
        if row in [part.row - 1, part.row + 1]:
            output += (
                f"[blue]{line[:c1]}[/blue]"
                + "[green]"
                + line[c1:c2]
                + "[/green]"
                + f"[blue]{line[c2:]}[/blue]"
                + "\n"
            )
        elif row == part.row:
            if part.cols[0] == 0:
                output += f"[red]{line[:c2-1]}[/red][green]{line[c2-1]}[/green][blue]{line[c2:]}[/blue]\n"
            elif part.cols[1] == len(line):
                output += f"[red]{line[:c1]}[/red][green]{line[c1]}[/green][red]{line[c1+1:]}[/red]\n"
            else:
                output += (
                    f"[blue]{line[:c1]}[/blue]"
                    + f"[green]{line[c1]}[/green]"
                    + f"[red]{line[c1+1:c2-1]}[/red]"
                    + f"[green]{line[c2-1]}[/green]"
                    + f"[blue]{line[c2:]}[/blue]"
                    + "\n"
                )

        else:
            output += "[blue]" + line + "\n"

    panel_group = Group(
        Panel(f"Searching for {part.value}..., cols ({part.cols})"),
        Panel(output),
    )
    return Panel(panel_group)


if __name__ == "__main__":
    with Live(generate_grid(parts[0]), refresh_per_second=4) as live:
        for part in parts:
            time.sleep(1.0)
            live.update(generate_grid(part))
