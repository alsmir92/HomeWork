# RANGE
my_range = range(10, 25, 2)

print(my_range.start)
print(my_range.stop)
print(my_range.step)

range_list = list(my_range)

print(range_list)
print(type(range_list))

for n in range_list:
    print(n)
