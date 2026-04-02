def tinh_tong_so_chan(lst):
    tong = 0 
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cáh nhau bangwf đấu phẩy")
num = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(num)
print("Tong các số chắn trong List là: ", tong_chan)
