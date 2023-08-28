# monthly expenditure
expenses = [2200, 2350, 2600, 2130, 2190]
extra_dollar = expenses[0]-expenses[2]
print("Extra dollar spent between january",extra_dollar)
quarter_report= expenses[0] + expenses[1] + expenses[2]
print("Quarterly report in three months",quarter_report)
exact_amount= 2000 in expenses
print(exact_amount)
add_june= expenses.append(1900)
refund= 200
expenses[3] -= refund
print("5. Corrected monthly expenses after refund:", expenses)


#string
heros =['spider man','thor','hulk','iron man','captain america']
length = len(heros)
print(length)
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
heros[1:3] = "Doctor strange"
heros.sort()

# list of odd numbers
max_number =int(input("Enter Number"))
odd_number= []
for num in range(1,max_number+1):
    if num % 2 !=0:
        odd_number.append(num)

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
    if numbers[i] == duplicate:
        print(i)

# time complexity 0(n2)