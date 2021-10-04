import argparse
import sys


# print("enter your eq")
# N1 = int(input())
# op = input()
# N2 = int(input())
# def calc(args):
#     if op=="add":
#         if N1==56 and N2==9 or N1==9 and N2==56:
#             print("=77")
#         else:
#             print("=",N1 + N2)
#     elif op=="min":
#         print("=",N1 - N2,)
#     elif op=="div":
#         if N1==56 and N2==6:
#             print ("=4")
#         else:
#             print ("=",N1/N2)
#     elif op=="mul":
#         if N1==45 and N2==3 or N1==3 and N2==45:
#             print("=555")
#         else:
#             print("=", N1*N2)
def calc(args):
    if args.o == "add":
        if args.x == 56 and args.y == 9 or args.x == 9 and args.y == 56:
            print("=77")
        else:
            print("=", args.x + args.y)
    elif args.o == "min":
        print("=", args.x - args.y, )
    elif args.o == "div":
        if args.x == 56 and args.y == 6:
            print("=4")
        else:
            print("=", args.x / args.y)
    elif args.o == "mul":
        if args.x == 45 and args.y == 3 or args.x == 3 and args.y == 45:
            print("=555")
        else:
            print("=", args.x * args.y)
    else:
        return"something went worng"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first no1. This is a utility for calculation. Please contact me for further help")
    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter first no2. This is a utility for calculation. Please contact me for further help")
    parser.add_argument('--o', type=str, default='add',
                        help="Enter first no. This is a utility for calculation. Please contact me for further help")

args = parser.parse_args()
sys.stdout.write(str(calc(args)))
