import mysql.connector
#pip install mysql-connector-python
#pip

class myDatabase:
    def __init__(self,dbname):
        self.CreateDatabase(dbname)

        self.conn= mysql.connector.connect(host="localhost",user="root",password="", database=dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("Create Table if not exists Employee (Id integer primary key AUTO_INCREMENT, Name varchar (50), Email Varchar (50), DOB Date)")
        self.conn.commit()

    def CreateDatabase(self,db):
        mydb = mysql.connector.connect(host="localhost",user="root",password="")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS " + db)
        mydb.close()

    def AddData(self,Name,Email,DOB):
        self.cur.execute("Insert into Employee (Name,Email,DOB) values(%s,%s,%s)",(Name,Email,DOB))
        self.conn.commit()

    def Insert(self):
        print('Add new Data')
        print(50*"=")
        name=  input('Enter Employee name                 :')
        email= input('Enter Email address                 :')
        dob=   input('Enter Date Of Birth [yyyy-mm-dd]    :')

        self.AddData(name,email,dob)

    def showData(self):
        print('List all employee information')
        print(50*"=")
        self.cur.execute("select * from Employee")

        print("%-5s %-30s %-20s %-15s" %('Id','Employee Name','Email Address','Date Of Birth'))
        print(70 *'=')

        employees= self.cur.fetchall()

        for Data in employees:
            print("%-5s %-30s %-20s %-15s" %(Data[0],Data[1],Data[2],Data[3]))

        print("Total Record   : %s" %len(employees))
        
    def searchData(self,idn):
        found=False
        self.cur.execute("select * from Employee where Id=%s",(idn,))
        mydata=self.cur.fetchall()
        if len(mydata)>0:

            for Data in mydata:
                print('Id Number     :%s' % (Data[0]))
                print('Employee Name :%s' % (Data[1]))
                print('Email Address :%s' % (Data[2]))
                print('Date of Birth :%s' % (Data[3]))
                print(60*"=")

            found= True
        
        else:
            print('Sorry record not found !!!')
        return found

    def Find(self):
        print('search by id')
        print(50*"=")
        idn=input('Enter Employee id number: ')
        found = self.searchData(idn,)
    
    def updateData(self,Id,Name,Email,DOB):
        self.cur.execute("Update Employee Set Name=%s, Email=%s, DOB=%s where Id=%s ", (Name,Email,DOB,Id))
        self.conn.commit()

        print("data update sucessfully")

    def Edit(self):
        print('Edit employee information')
        idn=input('Enter Employee id: ')

        self.cur.execute("Select * from Employee where Id=%s",(idn,))
        mydata=self.cur.fetchall()
        if len(mydata)>0:

            for Data in mydata:
                ename=Data[1]
                eemail=Data[2]
                edob=Data[3]
            
            name=input('Enter employee name: ')
            if name =='': name= ename
            email=input('Enter email address: ')
            if email =='': email= eemail
            dob=input('Enter date of birth: ')
            if dob =='': dob= edob

            self.updateData(idn,name,email,dob)
        else:
            print('No data Found !!!')
    
    def Delete(self):
        print('Delete employee information')
        idnum=input('Enter id number for delete: ')
        if self.searchData(idnum):
            yn=input('Are you sure you want to delete this record?[y/n]')
            if yn=="y" or yn=="Y":
                self.cur.execute("Delete from Employee where Id=%s ", (idnum,))
                self.conn.commit()
                print("data Deleted successfully")
            else:
                print('No found !!!')
    
    def __del__(self):
        self.conn.close()


'''obj = myDatabase('Emp.db')
obj.Insert()
obj.showData()
obj.Find()'''