import json

FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"Đã đọc dữ liệu từ {FILE_NAME}")
            return data
    except FileNotFoundError:
        print("File không tồn tại, trả về danh sách rỗng")
        return []
    except json.JSONDecodeError:
        print("File JSON bị lỗi format, trả về danh sách rỗng")
        return []
    except Exception as error:
        print("Lỗi khi đọc file JSON:", error)
        return []

def save_data(data):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        print(f"Lưu dữ liệu thành công vào file: {FILE_NAME}")
    except Exception as error:
        print("Lỗi khi lưu file JSON", error)

# Calculate Scores
def calc_subject_score(midterm, final):
    return midterm * 0.4 + final * 0.6

# Demo
if __name__ == "__main__":
    data = load_data()

    print(json.dumps(data, indent=2, ensure_ascii=False))

    save_data(data)
