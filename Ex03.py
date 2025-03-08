def tao_tuple_tu_list(lst):
    return tuple(lst)
#Nhập liệu
input_list = input("Nhập danh sách các dãy số, cách nhau bằng dấu phẩy: ")
nums = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(nums)
print(f"List: {input_list}")
print(f"Tuple từ List: {my_tuple}")