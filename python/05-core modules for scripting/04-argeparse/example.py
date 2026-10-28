import argparse

parser = argparse.ArgumentParser(
    usage="%(prog)s [option] [numbers]",  # %(prog)s dynamically uses your script's name
    description="Maths's Toolkit",
)

# Add your arguments as usual
sq = parser.add_argument("-sq", action="store_true", help="calculate the square")
s = parser.add_argument("-sum", action="store_true", help="To perform addition")
parser.add_argument("numbers", nargs="*", type=float, help="Numbers to process")

args = parser.parse_args()

if args.sum:
    total = sum(args.numbers)
    print(f"SUM: {total}")
