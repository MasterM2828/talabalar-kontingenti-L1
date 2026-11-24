# app.py - Talabalar kontingenti AT
import csv

students = []


def add_student(name, group):
    students.append({"name": name, "group": group})
    print(f"Qo'shildi: {name} ({group})")


def group_list(group):
    return [s["name"] for s in students if s["group"] == group]


def export_csv(path="students.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "group"])
        for s in students:
            writer.writerow([s["name"], s["group"]])
    print(f"Eksport qilindi: {path}")


def show_students():
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} - {s['group']}")


if __name__ == "__main__":
    add_student("Aliyev Vali", "DI-101")
    add_student("Karimova Madina", "DI-102")
    print("DI-101:", group_list("DI-101"))
    export_csv()
    show_students()