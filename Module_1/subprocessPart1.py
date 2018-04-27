import subprocess
subprocess.call('ls', shell=True)
output=subprocess.check_output('ls',shell=True)
print("Successfull Part 1")
print(output)

subprocess.call('g++ -std=c++11 -o mymain trialcpp.cpp', shell=True)
subprocess.call('./mymain', shell=True)
output=subprocess.check_output('./mymain',shell=True)
print("Successfull Part 2")
print(output)
