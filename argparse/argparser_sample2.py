import argparse

# argparser_sample.py

# Optional引数の導入
parser = argparse.ArgumentParser()
parser.add_argument("--date",help="the date for summarizing date.")
args = parser.parse_args()

if args.date:
    print("args.date is defined. date = " , args.date)
else:
    print("args.date is undefined.")