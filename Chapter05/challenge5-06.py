a = ["パン", "お米", "麺", "芋", "砂糖"]
b = ["パン", "お米", "まぜそば", "ケーキ", "芋"]
diff = []

for item in a:
    if item not in b:
        diff.append(item)
print(a)
print(b)
print(diff)
