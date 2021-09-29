import math


def find_gcd(x, n):
    multipliers = []
    i = 0
    while x != 0:
        temp = x
        multipliers.append(math.floor(n / x))
        x = (n % x)
        print("Step ", i, ": ", n, " = ", multipliers[i], "(", temp, ")", " + ", x, sep='')
        n = temp
        i += 1
    return n
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while 1:
        x = int(input("Please input the first number you want to find the gcd for: "))
        n = int(input("Please input the other number you want to find the gcd for: "))
        print("You would like to find the gc of ", x, " and ", n, "? [y/n] ", sep='', end='')
        response = input()
        if response == "y" or response == "yes":
            gcd = find_gcd(x,n)
            if x % gcd == 0 and n % gcd == 0:
                print("The GCD is: ", gcd, "!", sep='')
                break
            else:
                print("Unfortunately the GCD could not be calculated")
