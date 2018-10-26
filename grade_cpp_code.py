import subprocess
import os

# Part 1
credit1 = 0
output = subprocess.check_output(
    'g++ -std=c++11 -o testFileExc testFile.cpp', shell=True)
if not output:
    print("Successfull")
    credit1 = credit1 + 25
    print(credit1)
else:
    print("Unsucessfull")

# Part 2
credit2 = 0
f = open('creditfile.txt', 'w')
output = subprocess.call(
    'g++ -std=c++11 -o testFileExc testFile.cpp', shell=True, stdout=f)
if output == 0:
    print("Successfull")
    credit2 = credit2 + 25
    credit = 'Credit: ' + str(credit2)
    with open('creditfile.txt', 'a') as credit_file:
        credit_file.write(credit)
        credit_file.close()
    print(credit2)
else:
    print("Unsucessfull")
f.close()

# Part 3
credit_file = open('output.txt', 'w')
output1 = subprocess.check_output(
    "g++ -std=c++11 -o testFileExc testFile.cpp; exit 0", stderr=subprocess.STDOUT, shell=True)
print(str(output1))
valid = subprocess.check_output(
    './testFileExc \"{2, 3, 1}; exit 0\"', stderr=subprocess.STDOUT, shell=True)
print('Valid: ', valid)
valid2 = 'Output: ' + str(valid)
credit_file.write(valid2)
credit_file.close()

if os.stat("output.txt").st_size == 0:
    print("Invalid Output")
else:
    print("Output is in File")
