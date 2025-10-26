import tkinter as tk
from tkinter import messagebox

# Assuming you have a cartoon font installed, use its name
cartoon_font = ("Comic Sans MS", 12)

class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self):
        self.students = []
        self.quiz_grades = []
        self.quiz_averages = []

    def add_student(self, student):
        self.students.append(student)

    def add_quiz_grade(self, student_index, grade):
        if len(self.quiz_grades) <= student_index:
            self.quiz_grades.append([])
        self.quiz_grades[student_index].append(grade)

    def compute_quiz_averages(self):
        self.quiz_averages = []
        for grades in self.quiz_grades:
            if grades:
                average = sum(grades) / len(grades)
                self.quiz_averages.append(average)
            else:
                self.quiz_averages.append(0)

    def get_student_names(self):
        return [student.name for student in self.students]

    def get_student_grades(self, student_index):
        return self.quiz_grades[student_index]

    def get_class_average(self):
        if self.quiz_averages:
            return sum(self.quiz_averages) / len(self.quiz_averages)
        else:
            return 0

classroom = Classroom()

def add_student():
    name = student_entry.get()
    if name.isalpha():
        classroom.add_student(Student(name))
        student_entry.delete(0, tk.END)
        update_students_listbox()
    else:
        messagebox.showinfo("Error", "Please enter a valid student name (letters only).")

def add_quiz_grade():
    selected_student_index = students_listbox.curselection()
    if selected_student_index:
        try:
            student_index = selected_student_index[0]
            if 0 <= student_index < len(classroom.students):
                grade = int(quiz_grade_entry.get())
                classroom.add_quiz_grade(student_index, grade)
                quiz_grade_entry.delete(0, tk.END)
                update_quiz_grades_listbox(student_index)
            else:
                messagebox.showinfo("Error", "Invalid student index.")
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid numeric grade.")
    else:
        messagebox.showinfo("Error", "Please select a student before adding a quiz grade.")

def student_averages():
    classroom.compute_quiz_averages()
    update_class_averages_listbox()

def on_student_select(event):
    selected_student_index = students_listbox.curselection()
    if selected_student_index:
        student_index = selected_student_index[0]
        update_quiz_grades_listbox(student_index)

def update_students_listbox():
    students_listbox.delete(0, tk.END)
    students_listbox.insert(tk.END, *classroom.get_student_names())

def update_quiz_grades_listbox(student_index):
    grades = classroom.get_student_grades(student_index)
    quiz_grades_listbox.delete(0, tk.END)
    quiz_grades_listbox.insert(tk.END, *grades)

def update_class_averages_listbox():
    class_averages_listbox.delete(0, tk.END)
    for student, average in zip(classroom.get_student_names(), classroom.quiz_averages):
        class_averages_listbox.insert(tk.END, f"{student} - Average: {average:.2f}")

    # Add class average
    class_average = classroom.get_class_average()
    class_averages_listbox.insert(tk.END, f"Class Average: {class_average:.2f}")

root = tk.Tk()
root.title("Classroom Quiz Grades")

# Set background color to light pink
root.configure(bg='#FFB6C1')  # Hex color code for light pink

# Create a frame for centering
center_frame = tk.Frame(root, bg='#FFB6C1')  # Use the same background color
center_frame.pack(expand=True, fill='both')

student_entry = tk.Entry(center_frame, font=cartoon_font)
student_entry.grid(row=0, column=0, padx=5, pady=5)

add_student_button = tk.Button(center_frame, text="Add Student", command=add_student, font=cartoon_font, height=1)
add_student_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")

students_listbox = tk.Listbox(center_frame, height=7, width=25, font=cartoon_font)
students_listbox.grid(row=1, column=0, padx=5, pady=5)

# Bind the event to the students_listbox
students_listbox.bind("<<ListboxSelect>>", on_student_select)

quiz_grade_entry = tk.Entry(center_frame, font=cartoon_font)
quiz_grade_entry.grid(row=2, column=0, padx=5, pady=5)

add_quiz_grade_button = tk.Button(center_frame, text="Add Quiz Grade", command=add_quiz_grade, font=cartoon_font, height=1)
add_quiz_grade_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

quiz_grades_listbox = tk.Listbox(center_frame, height=7, width=25, font=cartoon_font)
quiz_grades_listbox.grid(row=3, column=0, padx=5, pady=5 )

# Move to the right side
right_frame = tk.Frame(root, bg='#FFB6C1')
right_frame.pack(expand=True, fill='both')

compute_averages_button = tk.Button(right_frame, text="Student and Class Average", command=student_averages, font=cartoon_font, height=1)
compute_averages_button.grid(row=4, column=0, padx=10, pady=10, sticky="e")

class_averages_listbox = tk.Listbox(right_frame, height=15, width=25, font=cartoon_font)
class_averages_listbox.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
