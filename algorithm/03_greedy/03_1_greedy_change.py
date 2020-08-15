"""
    거스름돈
    input ( n = 지불 금액, list = 동전 종류)

"""

n = 1260
list = [500, 100, 50, 10]

count = 0

for money in list:
    count += n // money
    n = n % money

print(count)