import argparse

# Optional引数の指定（値は指定せずオプションのみ指定）
parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on.", args.verbose)