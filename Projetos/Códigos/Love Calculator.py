def calculateLove(name1, name2):
    combineStr = name1 + " loves " + name2
    strCount = ""

    for c1 in combineStr:
        if combineStr.count(c1) != 0:
            strCount += str(combineStr.count(c1))
            combineStr = combineStr.replace(c1, "")

    n = list(map(int, strCount))

    while len(n) > 2:
        n = shortenNumber(n)

    per = int("".join(map(str, n)))
    return per


def shortenNumber(n):
    i = 0
    j = len(n) - 1
    nl = []

    while i <= j:
        per = n[i] + n[j]

        if i == j:
            per = n[i]

        nl.append(per)
        i += 1
        j -= 1

    return nl


if __name__ == '__main__':
    n1 = input("Enter your name: ").lower()
    n2 = input("Enter Partner/Crush name: ").lower()

    print(f"\nLove between {n1.upper()} and {n2.upper()}")
    print(f"{calculateLove(n1, n2)}%")
