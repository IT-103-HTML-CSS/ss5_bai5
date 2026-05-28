
while True:

    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Hướng dẫn sử dụng")
    print("3. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    # CHỨC NĂNG 1
    if choice == "1":

        branch_count = int(input("Nhập số lượng chi nhánh: "))

        max_students = 0
        best_branch = ""

        for branch in range(1, branch_count + 1):

            print(f"\n--- Chi nhánh {branch} ---")

            class_count = int(input("Nhập số lớp học: "))

            total_students = 0
            has_low_class = False

            for class_index in range(1, class_count + 1):

                while True:

                    students = int(
                        input(f"Nhập số học viên lớp {class_index}: ")
                    )

                    if students < 0:
                        print("Số học viên không được âm!")
                    else:
                        break

                total_students += students

                if students < 10:
                    print(f"Lớp {class_index} có sĩ số thấp")
                    has_low_class = True

            print("Tổng học viên:", total_students)

            if not has_low_class:
                print("Không có lớp nào dưới 10 học viên")

            if total_students > max_students:
                max_students = total_students
                best_branch = branch

        print("\n==========================")
        print(f"Chi nhánh có nhiều học viên nhất là: {best_branch}")
        print(f"Số học viên: {max_students}")

    # CHỨC NĂNG 2
    elif choice == "2":

        print("\n===== HƯỚNG DẪN =====")
        print("1. Chọn chức năng bằng số")
        print("2. Nhập số lượng chi nhánh")
        print("3. Nhập số lớp của từng chi nhánh")
        print("4. Nhập số học viên từng lớp")
        print("5. Hệ thống sẽ tự động thống kê")

    # CHỨC NĂNG 3
    elif choice == "3":

        print("Thoát chương trình")
        break

    # MENU KHÔNG HỢP LỆ
    else:
        print("Lựa chọn không hợp lệ!")
