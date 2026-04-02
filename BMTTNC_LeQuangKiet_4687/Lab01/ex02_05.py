so_gio_lan = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lan - gio_tieu_chuan)
thuc_linh = so_gio_lan *luong_gio + gio_vuot_chuan *luong_gio*1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")