import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


entry_name = None
entry_contact = None
entry_email = None
entry_rollno = None
entry_branch = None

def create_database():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS STUD_REGISTRATION ("
                   "STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                   "STU_NAME TEXT,"
                   "STU_CONTACT TEXT,"
                   "STU_EMAIL TEXT,"
                   "STU_ROLLNO TEXT,"
                   "STU_BRANCH TEXT)"
                   )
    conn.commit()
    conn.close()

def insert_record():
    global entry_name, entry_contact, entry_email, entry_rollno, entry_branch
    stu_name = entry_name.get()
    stu_contact = entry_contact.get()
    stu_email = entry_email.get()
    stu_rollno = entry_rollno.get()
    stu_branch = entry_branch.get()

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO STUD_REGISTRATION (STU_NAME, STU_CONTACT, STU_EMAIL, STU_ROLLNO, STU_BRANCH) "
                   "VALUES (?, ?, ?, ?, ?)",
                   (stu_name, stu_contact, stu_email, stu_rollno, stu_branch)
                   )
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student record added successfully!")




def delete_record_by_name_and_roll(sqlite_db_file, table_name):
    try:
        display_screen = tk.Tk()
        display_screen.geometry("900x400")
        display_screen.title("Delete a Record")
        iname = ttk.Label(display_screen, text="Student Name:")
        iname.pack()
        name = ttk.Entry(display_screen)
        name.pack()

   
        iroll = ttk.Label(display_screen, text="Roll Number:")
        iroll.pack()
        roll = ttk.Entry(display_screen)
        roll.pack()

        btn_display = ttk.Button(display_screen, text="Delete the record", command=lambda:delete_student(name, roll))
        btn_display.pack()


    except sqlite3.Error as e:
        messagebox.showinfo("Error", "Error in deleting record!")

        
def delete_student(name, rollno):
    try:
        global entry_name,entry_rollno
        name = entry_name.get()  # Get the value from the Entry widget
        rollno = entry_rollno.get()
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        query = 'DELETE FROM STUD_REGISTRATION WHERE STU_NAME = ? AND STU_ROLLNO = ?'
        cursor.execute(query, (name, rollno))
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
    except sqlite3.Error as e:
        messagebox.showinfo("Error", "Error in deleting record!")
    


def display_table():
    
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUD_REGISTRATION")
    data = cursor.fetchall()
    conn.close()

    top = tk.Toplevel()
    top.title("Student Records")

    tree = ttk.Treeview(top, columns=("S.no","Name", "Contact", "Email", "Roll No", "Branch"))
    tree.heading("#1", text="S.no")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Contact")
    tree.heading("#4", text="Email")
    tree.heading("#5", text="Roll No")
    tree.heading("#6", text="Branch")

    for row in data:
        tree.insert("", "end", values=row)

    tree.pack()

def create_gui():
    global entry_name, entry_contact, entry_email, entry_rollno, entry_branch
    display_screen = tk.Tk()
    display_screen.geometry("900x400")
    display_screen.title("Admission Management System")

    label_name = ttk.Label(display_screen, text="Student Name:")
    label_name.pack()
    entry_name = ttk.Entry(display_screen)
    entry_name.pack()

    
    label_contact = ttk.Label(display_screen, text="Contact Number:")
    label_contact.pack()
    entry_contact = ttk.Entry(display_screen)
    entry_contact.pack()

    label_email = ttk.Label(display_screen, text="Email Address:")
    label_email.pack()
    entry_email = ttk.Entry(display_screen)
    entry_email.pack()

    label_rollno = ttk.Label(display_screen, text="Roll Number:")
    label_rollno.pack()
    entry_rollno = ttk.Entry(display_screen)
    entry_rollno.pack()

    label_branch = ttk.Label(display_screen, text="Branch:")
    label_branch.pack()
    entry_branch = ttk.Entry(display_screen)
    entry_branch.pack()

    btn_insert = ttk.Button(display_screen, text="Insert Record", command=insert_record)
    btn_insert.pack()

    btn_display = ttk.Button(display_screen, text="Display Table", command=display_table)
    btn_display.pack()

    btn_display = ttk.Button(display_screen, text="Delete a record", command=lambda: delete_record_by_name_and_roll("student.db","STUD_REGISTRATION"))
    btn_display.pack()

    create_database()

    display_screen.mainloop()

create_gui()
