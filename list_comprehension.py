num_list = [y for y in range(100)]
print(num_list)

num_list1 = [y if (y % 2 == 0) else "Odd" for y in range(100)]
print(num_list1)

num_list2 = [y for y in range(100) if (y % 2 == 0)]
print(num_list2)

num_list3 = [y for y in range(100) if (y % 2 == 0) if (y % 5 == 0)]
print(num_list3)

num_list4 = [y for y in range(100) if ((y % 2 == 0) and (y % 5 == 0))]
print(num_list4)

# num_list5 = [y if (y % 2 == 0) for y in range(100)]  # Syntax Error
# print(num_list5)
