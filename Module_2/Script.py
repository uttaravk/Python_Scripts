import subprocess
import sys

credit=0;
print("Compilation Started")
output=subprocess.run('gcc -o mymain 3.c',shell=True)
credit=credit+25
print("Compilation Completed")
print("Execution Started")
output=subprocess.run('./mymain',shell=True)
credit=credit+25
print("Execution Completed")
print("Total Score (Part 1)= "+str(credit))
