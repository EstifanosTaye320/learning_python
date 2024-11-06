def main():
    wholeNum = int(input("Enter a whole number: "))
    if is_even(wholeNum):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()