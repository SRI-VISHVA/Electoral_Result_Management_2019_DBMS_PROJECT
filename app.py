import sqlite3
import csv
conn = sqlite3.connect(":memory:")
cursor=conn.cursor()
print("opened successfully")

command = "create table todo ( no number(5)  ,state varchar(30) ,constituency varchar(30),nameofelectedmp varchar(30),partyaffiliation varchar(30))"
conn.execute(command)
print("table created")
# 
# read and write csv file
with open('DBMS_projectvaibav.csv','r')as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # 
    with open('new_names.csv','w') as new_file:
        fieldnames = ['no','state','constituency','nameofelectedmp','partyaffiliation']
        # 
        csv_writer = csv.DictWriter(new_file , fieldnames=fieldnames, delimiter='\t')
        # 
        csv_writer.writeheader()
        # 
        # 
        for line in csv_reader:
            csv_writer.writerow(line)
# 
def searchbystate():
    s = input("Enter state name\n")
    csv_file=csv.reader(open('DBMS_projectvaibav.csv' , 'r'))
    command="select * from todo "
    conn.execute(command)
    # 
    for row in csv_file:
        if s==row[1]:
            print(row)
            print(row[2:])
            print("\n")
# 
def insert():
    n=int(input('Enter serial number should be greater than 543'))
    s=input('Enter state: ')
    c=input('Enter Constituency: ')
    m=input('Enter name of MP: ')
    p=input('Enter name of party: ')
    cursor.execute('insert into todo(no,state,constituency,nameofelectedmp,partyaffiliation) values(?,?,?,?,?)',(n,s,c,m,p))
    conn.commit()
    print("inserted")

def read():
    cursor.execute('select * from todo')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        print(row)

def update():
    number=int(input('enter number'))
    st=input('Enter state')
    cos=input('Enter constituency')
    mp=input('Enter name of MP')
    party=input('Enter name of party')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('Update todo set state =?,constituency=?,nameofelectedmp=?,partyaffiliation=? where no=?', (st,cos,mp,party, number))
        conn.commit()
    print('updated')

def deleteno():
    number=int(input('enter number'))
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('delete from todo  where no=?', (number,))
        conn.commit()
    print('deleted')

def deletest():
    st=input('Enter state')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('delete from todo  where state=?', (st,))
        conn.commit()
    print('deleted')
def deletecons():
    cos=input('Enter constituency')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('delete from todo  where constituency=?', (cos,))
        conn.commit()
    print('deleted')
def deletemp():
    mp=input('Enter name of MP')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('delete from todo  where nameofelectedmp=?', (mp,))
        conn.commit()
    print('deleted')

def deleteparty():
    party=input('Enter name of party')
    csv_file = csv.reader(open('DBMS_projectvaibav.csv', 'r'))
    for row in csv_file:
        cursor.execute('delete from todo  where partyaffiliation=?', (party,))
        conn.commit()
    print('deleted')


def searchbystate():
    state = input("Enter state name\n")
    csv_file=csv.reader(open('DBMS_projectvaibav.csv' , 'r'))

    cursor.execute('select state from todo where state=? ',(state,))

    for row in csv_file:
        if state==row[1]:
            print(row[0:])
            #print(row[3:])
            #print("\n")

def searchbyconstituency():
    cons = input("Enter constituency name\n")
    csv_file=csv.reader(open('DBMS_projectvaibav.csv' , 'r'))
    cursor.execute('select state from todo where constituency=? ', (cons,))

    for row in csv_file:
        if state==row[2]:
            print(row[0:])
            #print(row[3:])
            #print("\n")

def searchbyelectedmp():
    state = input("Enter elected MP name\n")
    csv_file=csv.reader(open('DBMS_projectvaibav.csv' , 'r'))

    for row in csv_file:
        if state==row[3]:
            print(row[0:])
            #print(row[4:])
            print("\n")
def searchbyparty():
    state = input("Enter Party  name\n")
    csv_file=csv.reader(open('DBMS_projectvaibav.csv', 'r'))

    for row in csv_file:
        if state==row[4]:
            print(row[0:])
            #print("\n")


i=1
while  i==1:
    a=int(input("Enter 1 to search data acccording to state: \nEnter 2 to search data acccording to constituency: \nEnter 3 to search data acccording to nameofelectedmp: \nEnter 4 to search data acccording to partyaffiliation:\nEnter 5 to update: \nEnter 6 to insert: \nEnter 7 to delete numberwise: \nEnter 8 to delete statewise: \nEnter 9 to delete constituencywise: \nEnter 10 to delete MPwise: \nEnter 11 to delete partywise: \nEnter 12 to exit:\n"))
    if a==1:
        searchbystate()
    if a==2:
        searchbyconstituency()
    if a==3:
        searchbyelectedmp()
    if a==4:
        searchbyparty()
    if a == 5:
        update()
    if a == 6:
        insert()
    if a == 7:
        deleteno()
    if a == 8:
        deletest()
    if a == 9:
        deletecons()
    if a == 10:
        deletemp()
    if a == 11:
        deleteparty()
    if a==12:
        break
    if a>=13:
        print("Wrong Option\n")

