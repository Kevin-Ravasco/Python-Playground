"""
QUIZ: Find the two numbers in the list below which when summed up, they can
add to the value of the sum.

array = [1, 3, 5, 6, 11, 23]
sum = 9
"""

array = [1, 3, 5, 6, 11, 23] 
sum = 9

def two_sum_solution(array, sum):
    index = 0
    number = 0

    while index < len(array):
        number = array[index]
        for num in array:
            if num != number and num + number == sum:
                return print('The two sum numbers are >>>', number, num)
        index += 1
        
    return print('no numbers matched !!!')


two_sum_solution(array, sum)