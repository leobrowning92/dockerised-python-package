from ball_pass.construct import load_file_input
from ball_pass.solve import nx_solve, manual_solve
import argparse
import textwrap
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ball_pass",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent(
        """\
        ball_pass determines the largest group of people who can touch a ball
        ---------------------------------------------------------------------
        takes a file, or list of files as input
        file_format:
            player1, visible_player_1, visible_player_2, ...
            player2, visible_player_1, visible_player_2, ...
        """
    ),
)

parser.add_argument("files", nargs="+", type=str, help="file(s) to process")
parser.add_argument(
    "--manual",
    action="store_true",
    help="use manual solving functions instead of networkx",
)

args = parser.parse_args()
for f in args.files:
    try:
        lookup = load_file_input(Path(f))
    except FileNotFoundError:
        print(f"File {f} not found")
        continue

    if args.manual:
        print(manual_solve(lookup))
    else:
        print(nx_solve(lookup))
