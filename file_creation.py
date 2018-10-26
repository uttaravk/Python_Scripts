import sys
import time as t
import calendar
from os import path


# Create file
def createFile(destination):
    file_name = 'output.txt'
    if not(path.isfile(destination + file_name)):
        f = open(destination + file_name, 'w')
        f.write('File Created')
        f.close()


# Create file with file name as date of creation
def createFileDate(destination):
    date = t.localtime(t.time())
    file_name = '%d_%s_%d.txt' % (
        date[2], calendar.month_name[date[1]], date[0])
    if not(path.isfile(destination + file_name)):
        f = open(destination + file_name, 'w')
        f.write('File Created')
        f.close()


# Function Call
if __name__ == '__main__':
    destination = './output/'
    createFile(destination)
    createFileDate(destination)
