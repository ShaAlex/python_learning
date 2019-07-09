# -*- coding: utf8 -*-
import argparse
import math


def usage():
    print("""
    -h or --help: Show help message
    -t or --type: Set rectangular or circle
    If type is rect, there should be 2 int positionals.
    Otherwise, one int positional.
    """)


def circle(r):
    return 2 * math.pi * r


def rect(length, width):
    return 2 * (length + width)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", required=True, choices=["rect", "circle"], dest="type")
    parser.add_argument("edge", nargs="+", type=int)

    args = parser.parse_args()

    if args.type:
        if args.type == "rect":
            if len(args.edge) == 2:
                print("The circumference of rect is %d.\n"%rect(args.edge[0], args.edge[1]))
            else:
                usage()
                return
        elif args.type == "circle":
            if len(args.edge) == 1:
                print("The circumference of circle is %f.\n"%circle(args.edge[0]))
            else:
                usage()
                return


if __name__ == "__main__":
    main()
