Reverse Words and swap cases
#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    word_list = sentence.split()
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()













=======================================================


Vending Machine

#!/bin/python3

import math
import os
import random
import re
import sys



class VendingMachine:
    def __init__(self,num_items,item_price):
        self.num_items=num_items
        self.item_price=item_price
    def buy(self,req_items,money):
        if req_items>self.num_items:
            return "Not enough items in the machine"
        else:
            if money>=req_items*self.item_price:
                self.num_items-=req_items
                return money-req_items*self.item_price
            else:
                return "Not enough coins"
    # Implement the VendingMachine here
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
