#problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def naturalnums(number):
    sum = 0
    for idx in range(number):
        if idx % 3 ==0 or idx % 5 == 0:
            sum += idx
    return sum
naturalnums (1000)
#sum_below ( 1000)
#def divisibles(below, *divisors):
    return (n for n in xrange(below) if 0 in (n % d for d in divisors))

print sum(divisibles(1000, 3, 5))
