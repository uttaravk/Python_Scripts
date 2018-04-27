import subprocess
import os

# Part 1
credit1=0;
output=subprocess.check_output('g++ -std=c++11 -o mymain trialcpp.cpp',shell=True)
if not output:
    print("Successfull")
    credit1=credit1+25
    print(credit1)
else:
    print("Unsucessfull")

# Part 2
credit2=0;
f=open('creditfile.txt', 'w')
output=subprocess.call('g++ -std=c++11 -o mymain trialcpp.cpp',shell=True, stdout=f)
if output == 0:
    print("Successfull")
    credit2=credit2+25
    credit='Credit: '+str(credit2)
    with open('creditfile.txt','a') as f1:
        f1.write(credit)
        f1.close()
    print(credit2)
else:
    print("Unsucessfull")
f.close()

# Part 3
f1=open('output.txt', 'w')
output1=subprocess.check_output("g++ -std=c++11 -o mymain trialcpp.cpp; exit 0", stderr=subprocess.STDOUT, shell=True)
print(str(output1))
valid=subprocess.check_output('./mymain \"{2, 3, 1}; exit 0\"', stderr=subprocess.STDOUT, shell=True)
print('Valid: ',valid)
valid2='Output: '+str(valid)
f1.write(valid2)
f1.close()

if os.stat("output.txt").st_size == 0 :
    print("Invalid Output")
else:
    print("Output is in File")
