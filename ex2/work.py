from math import ceil

def calc_account(m):
    # 実装は入れていません、自分で入れてください
    d = 1700
    cnt = 0
    if m <= 0:
        return None
    while True:
        if m <= d:
            return 610 + (80 * cnt)
        else:
            cnt += 1
            d += 315

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


