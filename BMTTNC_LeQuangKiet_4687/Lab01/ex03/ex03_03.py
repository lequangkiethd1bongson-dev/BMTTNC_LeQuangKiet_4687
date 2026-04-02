def tao_tuple_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số: ")
num = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_list(num)
print("List: ", num)
print("Tuple từ List: ", my_tuple)