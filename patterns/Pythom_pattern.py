def diamond_pattern(n):
    for i in range(n):
        print(" "*(n - i -1) + "*"* (2* i+ 1))
    for i in range(n, 0, -1):
        print(" "* (n-i) + "*"*(2 * i-1))

diamond_pattern(5)
rows = 5
# outer loop
for i in range(rows + 1):
    # nestedloop
    for j in range(i):
        print(i, end="")
    print('')

    # printing a pyramid
n = 5  # Number of rows

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("*" * (2*i+1))
# creating un inverted pyramid
n= 5
for i in range(n, 0, -1):
    print(" "*(n-i),end="")
    print("*"* (2*i-1))
n = 5
for i in range(n+ 1):
    for j in range(i):
        print(i,end="")
    print("")

# Triangle pattern
t = 6


from itertools import product
a= list(map(int,input("Enter number Pair").split()))
b= list(map(int,input("Enter number pair").split()))
p= list(product(a,b))

for i in p:
    print(i,end='')


from itertools import permutations
print("\n")
s , n = input("Enter value").split()
for i in list(permutations(sorted(s),int(n))):
    print(''.join(i))

from itertools import combinations

s , k = input().split()
k = int(k)
s = sorted(s)
for i in range(1,k+1):
    for j in list(combinations(s,i)):
        print("".join(s))