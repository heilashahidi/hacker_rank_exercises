#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    # Write your code here
    new_arr = sorted(arr)
    middle_num = int(len(new_arr) / 2)
    lower_half = new_arr[:middle_num]
    upper_half = new_arr[-middle_num:]
    
    
    if len(new_arr) % 2 == 0:
        if middle_num % 2 == 0:
            #Q1
            position_q1 = int(len(lower_half) / 2)
            num1_q1 = lower_half[position_q1 - 1]
            num2_q1 = lower_half[-position_q1]
            median_q1 = int((num1_q1 + num2_q1) / 2)
            
            #Q2
            num1_q2 = new_arr[middle_num - 1]
            num2_q2 = new_arr[-middle_num]
            median_q2 = int((num1_q2 + num2_q2) / 2)
            
            #Q3
            position_q3 = int(len(upper_half) / 2)
            num1_q3 = upper_half[position_q3 - 1]
            num2_q3 = upper_half[-position_q3]
            median_q3 = int((num1_q3 + num2_q3) / 2)
            
            return median_q1, median_q2, median_q3
        
        else:
            #Q1
            position_q1 = math.ceil(len(lower_half) / 2)
            median_q1 = lower_half[position_q1 - 1]
            
            #Q2
            num1_q2 = new_arr[middle_num - 1]
            num2_q2 = new_arr[-middle_num]
            median_q2 = int((num1_q2 + num2_q2) / 2)
            
            #Q3
            position_q3 = math.ceil(len(upper_half) / 2)
            median_q3 = upper_half[position_q3 - 1]
            
            return median_q1, median_q2, median_q3
    else:
        if middle_num % 2 == 0:
            #Q1
            position_q1 = int(len(lower_half) / 2)
            num1_q1 = lower_half[position_q1 - 1]
            num2_q1 = lower_half[-position_q1]
            median_q1 = int((num1_q1 + num2_q1) / 2)
            
            #Q2
            position_q2 = math.ceil(len(new_arr) / 2)
            median_q2 = new_arr[position_q2 - 1]
            
            #Q3
            position_q3 = int(len(upper_half) / 2)
            num1_q3 = upper_half[position_q3 - 1]
            num2_q3 = upper_half[-position_q3]
            median_q3 = int((num1_q3 + num2_q3) / 2)
            
            return median_q1, median_q2, median_q3
        
        else:
            #Q1
            position_q1 = math.ceil(len(lower_half) / 2)
            median_q1 = lower_half[position_q1 - 1]
            
            #Q2
            position_q2 = math.ceil(len(new_arr) / 2)
            median_q2 = new_arr[position_q2 - 1]
            
            #Q3
            position_q3 = math.ceil(len(upper_half) / 2)
            median_q3 = upper_half[position_q3 - 1]
            
            return median_q1, median_q2, median_q3
            
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
