import argparse

parse = argparse.ArgumentParser(
    usage="%(prog)s [-flags]", description="simple utility to test combined flag"
)

parse.add_argument("-g", action="store_true", help="to say greeting")
parse.add_argument("-n", action="store_true", help="to show name")

get_parse = parse.parse_args()

if get_parse.g:
    print("hello")

if get_parse.n:
    print("sameer")
