import random
import sys
import re


def input_validation(ip):
    macthobj = re.compile(r'(\d)+').search(ip)
    if macthobj != None:
        return
    else:
        print("Input should be Integer only")
        sys.exit()


if __name__ == '__main__':
    heads = 0
    tails = 0
    coin_flips = input("Enter number of coin flips:")
    input_validation(coin_flips)
    coin_flips = int(coin_flips)

    for flips in range(coin_flips):
        y = random.randint(0, 1)
        if y < 0.5:
            heads += 1
        else:
            tails += 1
    head_flips = (heads/coin_flips)*100
    tail_flips = (tails/coin_flips)*100
    print("Heads vs Tail percentage is: {}, {}".format(head_flips, tail_flips))
