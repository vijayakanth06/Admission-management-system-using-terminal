import sqlite3
def create_database():
    conn = sqlite3.connect("final.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS STUD_REGISTRATION ("
                   "STU_NAME TEXT,"
                   "STU_CONTACT TEXT,"
                   "STU_EMAIL TEXT,"
                   "STU_ROLLNO TEXT,"
                   "STU_BRANCH TEXT)"
                   )
    conn.commit()
    conn.close()

def generate_email(first_name,domain=".23aim@kongu.edu"):
    first_initial = first_name.lower()
    email = f"{first_initial}{domain}"
    return email

def get_students():
    conn = sqlite3.connect('final.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM STUD_REGISTRATION')
    rows = cur.fetchall()
    column_names = ['Student Name', 'Contact', 'Email', 'Roll Number', 'Branch']
    column_widths = [len(col) for col in column_names]  
    for row in rows:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(cell)))

  
    format_str = " | ".join(f"{{:<{width}}}" for width in column_widths)

    
    print(format_str.format(*column_names))
    print("-" * (sum(column_widths) + 3 * (len(column_names) - 1))) 

  
    for row in rows:
        print(format_str.format(*row))

    conn.close()
    
    print("Record printed!")


def insert_record(name, contact, email, rollno, branch):
    conn = sqlite3.connect("final.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO STUD_REGISTRATION (STU_NAME, STU_CONTACT, STU_EMAIL, STU_ROLLNO, STU_BRANCH) "
                   "VALUES (?, ?, ?, ?, ?)",
                   (name, contact, email, rollno, branch)
                   )
    conn.commit()
    conn.close()
    print("Record entered successfully!")
    
def delete_record(name, rollno):
    conn = sqlite3.connect("final.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM STUD_REGISTRATION WHERE STU_NAME = ? AND STU_ROLLNO = ?",
                   (name, rollno)
                   )
    conn.commit()
    conn.close()
    print("Record deleted successfully!")

def admission_management():
    while True:
        
        print("Admission Management System")
        print("1. Add new student")
        print("2. View student details")
        print("3. Delete student record")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Adding a new student...")
            name=input("Enter the student name: ")
            contact=input("Enter the contact number: ")
            rollno=input("Enter the roll number: ")
            branch=input("Enter the branch: ")
            email = generate_email(name)
            insert_record(name, contact, email, rollno, branch)
            
            
            
        elif choice == '2':
            print("Viewing student details...")
            get_students()
            
 
            
            
        elif choice == '3':
            print("Deleting student record...")
            name=input("Enter the student name: ")
            rollno=input("Enter the roll number: ")
            delete_record(name, rollno)
            
        elif choice == '4':
            print("Exiting the system...")
            break  
            

       
        continue_choice = input("Do you want to perform another operation? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break
create_database()
admission_management()
