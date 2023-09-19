MAX = 8
A = [[0] * MAX for _ in range(MAX)]  # Khởi tạo mảng giá trị 0
X = [-2, -2, -1, -1, 1, 1, 2, 2]
Y = [-1, 1, -2, 2, -2, 2, -1, 1]
dem = 0  # Số bước đi
n = 0

def xuat():
    for row in A:
        for a in row:
            if a != 0:
                print (str(a)+" ",end="")
        print("")

def diChuyen(x, y):
    global dem
    dem += 1  # Tăng giá trị bước đi
    A[x][y] = dem  # Đánh dấu đã đi

    if dem == n * n:
        print("Cac buoc di la:")
        xuat()
        exit(0)  # Kết thúc chương trình

    for i in range(8):
        u = x + X[i]  # Tạo một vị trí x mới
        v = y + Y[i]  # Tạo một vị trí y mới

        # Kiểm tra xem vị trí mới có hợp lệ và chưa đi qua chưa
        if 0 <= u < n and 0 <= v < n and A[u][v] == 0:
            diChuyen(u, v)

    # Nếu không tìm được bước đi thì phải trả lại các giá trị ban đầu
    A[x][y] = 0
    dem -= 1

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    while 0>n or n>8:
        print("Nhap n: ")
        n = int(input())

    x = int(input("Nhap vi tri ban dau.\nx: "))

    y = int(input("y: "))
    diChuyen(x, y)

    # Nếu không tìm được bước đi thì sẽ thông báo
    print("Khong tim thay duong di.")