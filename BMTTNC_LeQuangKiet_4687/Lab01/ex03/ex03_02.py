def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("nhập danh sách các số, cách nhau bởi dấu phẩy: ")
num = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(num)
print("List sau khi dao nguoc: ", list_dao_nguoc)