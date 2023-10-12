# TODO Найдите количество книг, которое можно разместить на дискете

size_of_symbols = 4
symbols = 25
strings = 50
sheets = 100

num_of_byte_in_str = size_of_symbols * symbols
num_of_byte_in_sheet = num_of_byte_in_str * strings
num_of_byte_in_book = num_of_byte_in_sheet * sheets
storage_in_byte = 1.44 * (2 ** 20)

print("Количество книг, помещающихся на дискету:", int(storage_in_byte / num_of_byte_in_book))
