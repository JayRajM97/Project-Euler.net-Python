#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

arrsumofsq = []
sqofsum=0
for i in range(1,101):
    arrsumofsq.append(i**2)
    sqofsum+=i
print(sum(arrsumofsq))
print(sqofsum**2)
print(sqofsum**2-sum(arrsumofsq))


#Answer: 25164150
