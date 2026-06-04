def a(yeah):
    try:
        return float(yeah)
    except ValueError:
        print("間違い")
b = a("5")
print(b)
