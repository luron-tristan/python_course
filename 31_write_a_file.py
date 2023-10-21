
text = "Yoooooooo\nWe are writing from 31_write_a_file.py\n"
new_line = 'see ya'

with open('31_test.txt', 'w') as file:
    file.write(text)

with open('31_test.txt', 'a') as file:
    file.write(new_line)
