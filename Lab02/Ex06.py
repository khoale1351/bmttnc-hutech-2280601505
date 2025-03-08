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