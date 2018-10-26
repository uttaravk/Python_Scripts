import subprocess
import sys
credit = 0
# Extract PID
output1 = subprocess.check_output(
    'ps l | grep -w ./signalHandlerExc | awk \'{print $2;exit;}\'', shell=True)
output1 = str(output1)
print("Start 1")
output2 = subprocess.run('kill -s INT ' + output1[2:6], shell=True)
output2 = subprocess.run('sleep 5', shell=True)
credit = credit + 10
print("Stop 1")
output2 = subprocess.run('kill -s INT ' + output1[2:6], shell=True)
output2 = subprocess.run('sleep 5', shell=True)
credit = credit + 10
print("Start 2")
output2 = subprocess.run('kill -s INT ' + output1[2:6], shell=True)
output2 = subprocess.run('sleep 5', shell=True)
credit = credit + 10
print("Stop 2")
output2 = subprocess.run('kill -s INT ' + output1[2:6], shell=True)
output2 = subprocess.run('sleep 5', shell=True)
credit = credit + 10
print("Final Quit")
output2 = subprocess.run('kill -s QUIT ' + output1[2:6], shell=True)
credit = credit + 10
print("Completed")

print("Total Points (Part 2)= " + str(credit))
