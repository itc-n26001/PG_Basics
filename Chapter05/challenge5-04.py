user = {
        "animal": "cat",
        "drink": "pepsi",
        "love": "games",
        }
print("animal,drink,loveの三択です")
key = input("調べたい名前を入力してください: ")

if key in user:
    print(user[key])
else:
    print("見つかりませんでした")
