import re
import sys


def input_validation(ip):
    macthobj = re.compile(r'[A-Za-z]{2,}').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be 3 or more Alphabets only")
        sys.exit()


if __name__ == '__main__':
    name = input("Enter Username (with minimum 3 letters): ").title()
    input_validation(name)
    print("Hello "+name+", How are you?")
