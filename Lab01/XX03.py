#Câu 1
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

#Câu 2
#Hàm đảo ngược danh sách
def reversed_list(lst):
    return lst[::-1]
#Nhập danh sách
input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
nums = list(map(int, input_list.split(',')))

list_nguoc = reversed_list(nums)
print(f"List sau khi đảo ngược: {list_nguoc}")

#Câu 3
def tao_tuple_tu_list(lst):
    return tuple(lst)
#Nhập liệu
input_list = input("Nhập danh sách các dãy số, cách nhau bằng dấu phẩy: ")
nums = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(nums)
print(f"List: {input_list}")
print(f"Tuple từ List: {my_tuple}")

#Câu 4
def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
#Nhập liệu
input_tuple = eval(input("Nhập tuple, ví dụ (1,2,3): "))
first, last = truy_cap_phan_tu(input_tuple)
#Kết quả
print(f"Phần tử đầu tiên: {first}")
print(f"Phần tử cuối cùng: {last}")

#Câu 5
def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
#Nhập danh sách
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
#Kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print(f"Số lần xuất hiện của các phần tử: {so_lan_xuat_hien}")

#Câu 6
def xoa_phan_tu(dict, key):
    if key in dict:
        del dict[key]
        return True
    else:
        return False
#Sử dụng hàm và in kết quả
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
del_key = 'b'
result = xoa_phan_tu(my_dict, del_key)
if result:
    print(f"Phần tử đã được xoá từ Dictionary: {my_dict}")
else:
    print(f"Không tìm thấy phần tử cần xoá trong Dictionary.")
