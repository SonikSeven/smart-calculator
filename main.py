import string
import re


def identifiers_check(user_input):
    operands = re.split("[-+/*()= ]", user_input)
    for i in operands:
        if set(i) & set(string.digits) and set(i) & set(string.ascii_letters):
            return "Invalid assignment" if "=" in user_input else "Invalid identifier"
    return False


def main():
    while True:
        user_input = "".join("**" if i == "^" else i for i in input().strip())
        if user_input == "/exit":
            return print("Bye!")
        elif user_input == "/help":
            print("The program calculates mathematical operations")
        elif user_input.startswith("/"):
            print("Unknown command")
        elif "//" in user_input:
            print("Invalid expression")
        elif user_input:
            check_result = identifiers_check(user_input)
            if check_result:
                print(check_result)
                continue
            if "=" in user_input:
                try:
                    exec(user_input)
                except NameError:
                    print("Unknown variable")
                except SyntaxError:
                    print("Invalid assignment")
            else:
                try:
                    result = eval(user_input)
                    print(int(result) if int(result) == result else result)
                except NameError:
                    print("Unknown variable")
                except SyntaxError:
                    print("Invalid expression")


if __name__ == "__main__":
    main()
