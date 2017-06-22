import argparse

# 位置引数とOptionalの併用
parser = argparse.ArgumentParser()
parser.add_argument("-date",
                    help="the date for summarizing date.")

parser.add_argument("--verbose",
                    help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("the date specified is ", args.date)
else:
    print(args.date)