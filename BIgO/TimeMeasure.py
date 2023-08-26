# program to print squared number
def squared_num(number):
    squared_numbers = []
    for n in number:
        squared_numbers.append(n * n)
    return squared_numbers


numbers = [1, 2, 3, 4]
a = squared_num(numbers)
print(a)


# time complecity is 0(n) which is leaner graph

def find_first(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe


# time complecity from list 0(1)

numbers = [1, 2, 3, 4, 5, 3, 7, 8, 2, 4]
for i in range(len(numbers)):# the length of the array
    for j in range(i + 1, len(numbers)): # number in the specific range to the end of the array
        if numbers[i] == numbers[j]: # if the number in the length
            duplicate = numbers[i]
            break
for i in range(len(numbers)):
    if i == duplicate:
        print(i)

