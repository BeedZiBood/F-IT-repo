numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

lenght = len(numbers)
ind_of_missing = 4
sum_of_num = sum(numbers[:ind_of_missing]) + sum(numbers[ind_of_missing + 1:])
numbers[ind_of_missing] = sum_of_num / lenght

print("Измененный список:", numbers)
