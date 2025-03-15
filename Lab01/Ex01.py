#Hàm tính tổng chẵn
def tinh_tong_chan(lst):
    tong = 0;
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
#Nhập dữ liệu và tính toán
input_lst = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu phẩy: ").split(',')))
tong_chan = tinh_tong_chan(input_lst)
print(f"Tổng các số chẵn: {tong_chan}")