import sys
import time as t
import calendar
from os import path

def createFile(dest):
    name='MyFile.txt'
    if not(path.isfile(dest+name)):
        f=open(dest+name,'w')
        f.write('File Created')
        f.close()

def createFileDate(dest):
    date=t.localtime(t.time())
    name='%d_%s_%d.txt'%(date[2], calendar.month_name[date[1]], date[0])
    if not(path.isfile(dest+name)):
        f=open(dest+name,'w')
        f.write('File Created')
        f.close()

if __name__ =='__main__':
    distnation = '//Users//uttara//Desktop/'
    createFile(distnation)
    createFileDate(distnation)
    print('done')
