# app.py - Talabalar kontingenti AT
students = []


def add_student(name, group):
    students.append({"name": name, "group": group})
    print(f"Qo'shildi: {name} ({group})")


def show_students():
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - {s['group']}")


if __name__ == "__main__":
    show_students()