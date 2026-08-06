s = input("Enter a string: ")

print("Duplicate Characters:")

for ch in s:
    if s.count(ch) > 1:
        print(ch)