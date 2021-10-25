import math


def find_gcd(x, n):
    multipliers = []
    i = 0
    while x != 0:
        temp = x
        multipliers.append(math.floor(n / x))
        x = (n % x)
        # print("Step ", i, ": ", n, " = ", multipliers[i], "(", temp, ")", " + ", x, sep='')
        n = temp
        i += 1
    return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1, 15):
        x = i + 1
        n = math.pow(i, 4) + 4
        c = n * 3
        if x > n:
            gcdL = find_gcd(n, x)
        else:
            gcdL = find_gcd(x, n)
        if x > 3:
            gcdF = find_gcd(3, x)
        else:
            gcdF = find_gcd(x, 3)
        if x > c:
            gcdC = find_gcd(c, x)
        else:
            gcdC = find_gcd(x, c)

        print("N: ", i, "; N+1: ", x, "; n^4 + 4: ", n, "; gcd(n+1,3): ", gcdF, "; gcd(n+1,n^4+4): ", gcdL,"; gcd(n+1,3n^4+12): ", gcdC, sep="")
