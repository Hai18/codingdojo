#find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace ('day','month')
#min and max
x = [2,54,-2,7,12,98]
print max (x)
print min (x)
#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x [0]
print x [-1]
x = [x[0], x[-1]]
print x
#New List
numbers = [19,2,54,-2,7,12,98,32,10,-3,6]
print numbers
numbers.sort ()
print numbers
first_half = numbers[:len(numbers)/2]
second_half =numbers[len(numbers)/2:]
print "first half", first_half
print "scond hald", second_half
second_half.insert(0,first_half)
print second_half
