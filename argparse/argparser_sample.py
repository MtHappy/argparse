import argparse

# argparser_sample.py

#引数パーサーの起動
#parser = argparse.ArgumentParser()
#parser.parse_args()


# 位置引数の取得
parser = argparse.ArgumentParser()
#parser.add_argument("date", help="the target fdate for summrizing data.",type=int)
parser.add_argument("square", help="the target date for summrizing data.",type=int)
args = parser.parse_args()
print(args.square**2)

