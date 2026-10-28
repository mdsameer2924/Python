import argparse

flag = argparse.ArgumentParser(
    usage="%(prog)s [option] [numbers]", description="Maths's Toolkit"
)
flag.add_argument("-sq", action="store_true", help="calculate the square")
flag.add_argument("-sum", action="store_true", help="To perform addition")
final = flag.parse_args()


def sum(*args):
    for i in args:
        print(i)


a = 5
if final.sq:
    print(f"{a} square: {a * a}")
elif final.sum:
    sum(3, 5, 6)
