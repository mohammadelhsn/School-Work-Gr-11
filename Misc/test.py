import sys 

sys.path.append(".")

from my_file import Student

print(Student("joe", 90).print_score())