count = 0


def digui2():
    global count
    count += 1
    print(count)
    if divmod(count, 10) == (5, 1):
        return
    digui2()


digui2()