"""Example script for argument parsing.

Print the sum of the x and y inputs.

Example
-------
$ python -m sum -x 3 -y 2.5
5.5

"""
import argparse

# Argument parsing
parser = argparse.ArgumentParser(__doc__)  # Show the doc when calling help
parser.add_argument("-x",
                    "--in1",
                    dest="x",
                    type=float,
                    help="First number for the sum")
parser.add_argument("-y",
                    "--in2",
                    dest="y",
                    type=float, default=0.,
                    help="Second number for the sum (default: 0.)")

args = parser.parse_args()

print(f"Result: {args.x + args.y}")
