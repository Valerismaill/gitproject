def main():
    print("Welcome to the lab-git-project!")

if __name__ == "__main__":
    main()

from utils import add_numbers, multiply_numbers

def main():
    a = 5
    b = 3

    print(f"The sum of {a} and {b} is: {add_numbers(a, b)}")
    print(f"The product of {a} and {b} is: {multiply_numbers(a, b)}")

if __name__ == "__main__":
    main()