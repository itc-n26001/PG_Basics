numbers = [3, 7, 10, 25, 50]

while True:
    s = input("数字を入力してください('q'で終了): ")

    if s == "q":
        break

    try:
        n = int(s)

        if n in numbers:
            print("正解")
        else:
            print("不正解")

    except ValueError:
        print("数字か'q'を入力してください")
