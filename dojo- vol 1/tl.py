#sum
mix = ['magical unicorns',19,'hello',98.98,'world']
for idx in mix:
    if type (idx) is int or  type (idx) is float:
        print (idx)
#mix of types
mix = ['magical unicorns',19,'hello',98.98,'world']
for idx in mix:
    if type (idx) is str or type (idx) is float or type (idx) is int:
        print ("The array you entered is of mixed type")
