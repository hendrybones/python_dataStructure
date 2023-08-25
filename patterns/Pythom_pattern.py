
rows = 5
# outer loop
for i in range(rows+ 1):
    # nestedloop
    for j in range(i):
        print(i,end="")
    print('')

from itertools import product
a= list(map(int,input("Enter number Pair").split()))
b= list(map(int,input("Enter number pair").split()))
p= list(product(a,b))

for i in p:
    print(i,end='')


from itertools import permutations
s , n = input().split()
for i in list(permutations(sorted(s),int(n))):
    print(''.join(i))