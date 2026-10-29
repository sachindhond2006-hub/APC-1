#1
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Roll Number: " + roll_no + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Student details saved successfully.")


#2
with open("student.txt", "r") as file:
    content = file.read()

print(content)


#3
info = input("Enter additional information: ")

with open("student.txt", "a") as file:
    file.write(info + "\n")

print("Information appended successfully.")


#4
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


#5
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))


#6
with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))


#7
with open("student.txt", "r") as file:
    content = file.read()

print("Total number of characters:", len(content))


#8
with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())


#9
with open("student.txt", "r") as file:
    content = file.read()

vowels = 0
consonants = 0

for char in content:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


#10
with open("student.txt", "r") as file:
    content = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for char in content:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    elif char != "\n":
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


#11
with open("student.txt", "r") as file:
    content = file.read()

words = content.split()
longest_word = max(words, key=len)

print("Longest word:", longest_word)
print("Length:", len(longest_word))


#12
with open("student.txt", "r") as file:
    content = file.read()

words = content.lower().split()
word_count = {}

for word in words:
    word = word.strip(".,!?;:")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


#13
search_word = input("Enter word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    words = line.lower().split()

    if search_word.lower() in words:
        count += words.count(search_word.lower())
        line_numbers.append(i)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)


#14
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("modified.txt", "w") as file:
    file.write(content)

print("Modified file created.")


#15
with open("program.py", "r") as file:
    lines = file.readlines()

with open("program_without_comments.py", "w") as file:
    for line in lines:
        if not line.lstrip().startswith("#"):
            file.write(line)

print("Comments removed successfully.")


#16
with open("student.txt", "r") as file:
    content = file.read()

with open("uppercase.txt", "w") as file:
    file.write(content.upper())

print("Uppercase file created.")


#17
with open("students.txt", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []

with open("students.txt", "r") as file:
    next(file)

    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))

print("All Records:")

for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
print("Highest marks:", highest)

total = sum(student[2] for student in students)
average = total / len(students)

print("Average marks:", average)

print("Students scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student)


#18
def display_employees():
    with open("employees.txt", "r") as file:
        for line in file:
            print(line.strip())


def highest_paid():
    with open("employees.txt", "r") as file:
        employees = []

        for line in file:
            emp_id, name, department, salary = line.strip().split(",")
            employees.append((emp_id, name, department, float(salary)))

    highest = max(employees, key=lambda x: x[3])
    print("Highest-paid employee:", highest)


def average_salary():
    with open("employees.txt", "r") as file:
        salaries = []

        for line in file:
            data = line.strip().split(",")
            salaries.append(float(data[3]))

    print("Average salary:", sum(salaries) / len(salaries))


def above_salary(amount):
    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if float(data[3]) > amount:
                print(line.strip())


with open("employees.txt", "w") as file:
    file.write("101,Amit,IT,50000\n")
    file.write("102,Priya,HR,60000\n")
    file.write("103,Rahul,Finance,75000\n")

display_employees()
highest_paid()
average_salary()

amount = float(input("Enter salary amount: "))
above_salary(amount)


#19
with open("attendance.txt", "w") as file:
    file.write("101,Amit,70,90\n")
    file.write("102,Priya,80,90\n")
    file.write("103,Rahul,60,90\n")

with open("attendance.txt", "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")

        present = int(present)
        total = int(total)

        percentage = (present / total) * 100

        print(name, ":", percentage, "%")

        if percentage < 75:
            print("Below 75%:", name)


#20
with open("transactions.txt", "w") as file:
    file.write("D,5000\n")
    file.write("W,1000\n")
    file.write("D,3000\n")
    file.write("W,500\n")

total_deposits = 0
total_withdrawals = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")

        amount = float(amount)
        transactions.append(amount)

        if transaction_type == "D":
            total_deposits += amount
        elif transaction_type == "W":
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", final_balance)
print("Largest transaction:", largest_transaction)


#21
books = []


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully.")


def search_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            print(book)
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False
                print("Book issued.")
            else:
                print("Book already issued.")

            return

    print("Book not found.")


def return_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            print("Book returned.")
            return

    print("Book not found.")


def display_available():
    for book in books:
        if book["available"]:
            print(book)


while True:
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")


#22
with open("file1.txt", "r") as file1:
    content1 = file1.read()

with open("file2.txt", "r") as file2:
    content2 = file2.read()

with open("combined.txt", "w") as file3:
    file3.write(content1)
    file3.write("\n")
    file3.write(content2)

print("Files combined successfully.")


#23
with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    min_lines = min(len(lines1), len(lines2))

    for i in range(min_lines):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break
    else:
        print("One file has additional lines.")
