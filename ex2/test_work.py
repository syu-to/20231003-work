from work import calc_account



def test_calc_account():
    """タクシーの運賃計算
    タクシーの運賃を計算するコードを作成せよ
    * 初乗り運賃は 1700m までは610円とする
    * 1700mを超えるとその後は 315m毎に 80円増えるものとする
    * 引数として走行距離(整数でm単位)が渡されるものとする
    * 戻り値は金額(整数値)とする
    * 1mでも超えれば80円単位でかかるものとする
    * 0mおよびマイナスの場合はNoneを返す
    """
    min = 610 # 初乗り運賃
    assert calc_account(1000) == min
    assert calc_account(1700) == min
    assert calc_account(1701) == 690 # 1mでも超えれば増える
    assert calc_account(2015) == 690
    assert calc_account(2016) == 770
    assert calc_account(0) == None
    assert calc_account(-10) == None
    # 初乗りの距離までは定額610円



