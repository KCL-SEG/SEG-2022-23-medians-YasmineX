"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        med = (lst[len(lst)//2] + lst[len(lst)//2 - 1]) / 2
    else:
        med = lst[len(lst)//2]
    return med


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))