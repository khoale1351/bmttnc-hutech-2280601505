import sys
sys.stdout.reconfigure(encoding='utf-8')

#1. Nhap ten, tuoi
name = input("Nhập tên của bạn: ")
age = input("Nhập tuổi: ")
print(f"Người dùng {name} {age} tuổi");

#2. Tinh dien tich hinh tron
ban_kinh = float(input("Nhập bán kính hình tròn: "))
dien_tich = 3.14 * (ban_kinh ** 2)
print(f"Diện tích hình tròn: {dien_tich}")

#3. Nhap, kiem tra so nguyen
num = input("Nhập 1 số nguyên: ")
if num.isdigit():
    print(f"{num} là một số nguyên!")
else:
    print(f"{num} không phải số nguyên!")

#4. Tạo list rỗng, duyệt các số trong [2000,3200]. Kiểm tra xem i % 7 = 0 và i % 5 != 0
array = []
for i in range(2000,3200):
    if i % 7 == 0 and i % 5 != 0:
        array.append(i)
print("Danh sách các số chia hết cho 7 không phải bội số của 5:", array)

#5. Nhập, xuất và tính giờ làm
from datetime import datetime
shift_start = input("Giờ vào làm (HH:MM): ")
shift_end = input("Giờ tan làm: (HH:MM): ")
fmt = "%H:%M"
gio_lam = datetime.strptime(shift_end, fmt) - datetime.strptime(shift_start, fmt)
print(f"So gio lam: {gio_lam}")

#6. Nhập các dòng từ User, chuyển thành chữ in hoa và xuất.
lines = []
while True:
    line = input("Nhập dòng văn bản (Nhập 'end' để dừng): ")
    if line.lower() == 'end':
        break
    lines.append(line.upper())
print(lines)

#7. Hàm kiểm tra số nhị phân chia hết 5.
def nhi_phan_chia_het_cho_5(binary_num):
    decimal_num = int(binary_num, 2)
    if decimal_num % 5 == 0:
        return True
    else:
        return False
#Kiểm tra hàm
binary_input = input("Nhập số nhị phân: ")
if nhi_phan_chia_het_cho_5(binary_input):
    print(f"{binary_input} chia hết cho 5.")
else:
    print(f"{binary_input} không chia hết cho 5.")

#8. Nhập chuỗi nhị phân từ User, tách và in số nhị phân chia hết 5.
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
binary_list = chuoi_nhi_phan.split(',')
chia_het_cho_5 = [num for num in binary_list if nhi_phan_chia_het_cho_5(num)]
if len(binary_list) > 0:
    print(f"Các số chia hết cho 5: {', '.join(chia_het_cho_5)}")
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")
