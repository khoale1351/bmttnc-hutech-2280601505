#Hàm đảo ngược danh sách
def reversed_list(lst):
    return lst[::-1]
#Nhập danh sách
input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
nums = list(map(int, input_list.split(',')))

list_nguoc = reversed_list(nums)
print(f"List sau khi đảo ngược: {list_nguoc}")