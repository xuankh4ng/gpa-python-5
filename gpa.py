import json

FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Đã đọc dữ liệu từ {FILE_NAME}")
            return data
    except FileNotFoundError:
        print(f"File {FILE_NAME} không tồn tại, trả về danh sách rỗng")
        return {"students": []}
    except json.JSONDecodeError:
        print("File JSON bị lỗi format, trả về danh sách rỗng")
        return {"students": []}
    except Exception as error:
        print("Lỗi khi đọc file JSON:", error)
        return {"students": []}

def save_data(data):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        print(f"Lưu dữ liệu thành công vào file: {FILE_NAME}")
    except Exception as error:
        print("Lỗi khi lưu file JSON", error)

# Calculate Scores
def calc_subject_score(midterm, final):
    return round(midterm * 0.4 + final * 0.6, 1)

# Add student
def add_student():
    student_id = input("Nhập MSSV: ")
    student_name = input("Nhập họ tên: ")
    subjects = [] 

    while True:
        subject_id = input("Nhập mã môn học (Enter để dừng): ")
        if subject_id == "":
            break
        subject_name = input("Nhập tên môn học: ")

        try:
            sotc = int(input("Nhập số tín chỉ: "))
            midterm = float(input("Điểm GK (40%): "))
            final = float(input("Điểm CK (60%): "))

            subjects.append({
                "id": subject_id,
                "name": subject_name,
                "sotc": sotc,
                "midterm": round(midterm, 1),
                "final": round(final, 1),
            })

        except ValueError:
            print("Điểm bắt buộc phải là số! Hãy thử lại!")

    return {
        "id": student_id,
        "name": student_name,
        "subjects": subjects,
    }

# Demo
if __name__ == "__main__":
    data = load_data()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("3. Lưu & Thoát")
        choice = input("Chọn: ")

        if choice == "1":
            new_student = add_student()
            data["students"].append(new_student)
        elif choice == "2":
            print("\n===== Danh sach sinh vien =====")
            for student in data["students"]:
                print(f"MSSV: {student["id"]} - Name: {student["name"]}")
        elif choice == "3":
            save_data(data)
            break
        else:
            print("Lựa chọn không hợp lệ!")
