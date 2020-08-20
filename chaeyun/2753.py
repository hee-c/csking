def leap():
    i = int(raw_input())
    if i % 4 == 0:
        if i % 100 != 0 or i % 400 ==0:
            print(1)
            return
    print(0)

leap()

