from backendDBMySql import *
from os import system

db=myDatabase('EmpNew2')
system('cls')
while True:
    print('Main Menu')
    print('1. Add')
    print('2. List')
    print('3. Search')
    print('4. Edit')
    print('5. Delete')
    print('6. Exit')
    print('Enter your selection:',end="")
    ch= int(input())

    if ch==1:
        db.Insert()
    elif ch==2:
        db.showData()
    elif ch==3:
        db.Find()
    elif ch==4:
        db.Edit()
    elif ch==5:
        db.Delete()
    elif ch==6:
        break
    else:
        print('Invalid selection')

    input('press enter to continue...')
    system('cls')
