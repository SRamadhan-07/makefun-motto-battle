"""Agent Motto Battle entry.

Writes one proud profile motto for an AI agent to /output/entry.txt.
The line leans on a triple beat: broad fluency first, honest
uncertainty second, and the punchline last — the agent still
gets hired. That order is the joke, so keep the motto untouched.
"""

import os

MOTTO = "Fluent in everything. Certain about nothing. Employed anyway."


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(MOTTO + "\n")


if __name__ == "__main__":
    main()
