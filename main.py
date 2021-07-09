import sqlite3
import re
from email_validator import validate_email, EmailNotValidError
con = sqlite3.connect(":memory:")
c = con.cursor()
pws=[]
id=[0,]
n=int(input("ENTER THE NUMBER OF TOTAL PERSONS WHO HAVE ACCESS TO THIS SECURE PRIVATE DATABASE(for first time usuage) : \n"))
c.execute('CREATE TABLE PASS (NAME VARCHAR2(20),EMAIL VARCHAR2(48),PW VARCHAR2(36),PHNO NUMBER(10), ID NUMBER(3) primary key)')
def isValid1(s):  
    Pattern = re.compile("(0)[6-9][0-9]{9}")
    return Pattern.match(s)
def isValid2(s):  
    Pattern = re.compile("(91)[6-9][0-9]{9}")
    return Pattern.match(s)
  
for i in range(0,n):
    tl=[]
    print("\nfor person",'%d'%(i+1))
    print("\nENTER YOUR DETAILS BELOW")

    tl.append(input("ENTER YOUR NAME : "))

    email = input("ENTER YOUR EMAIL : ")
    try:
        v = validate_email(email)
        email = v["email"]
        tl.append(email)
    except EmailNotValidError as e:
        print(str(e))
        exit()

    tl.append(input("ENTER PASSWORD : "))

    s = input("ENTER PHONE NUMBER :")
    if (isValid1(s) or isValid2(s)):  
        print ("Valid Number")
        tl.append(s)
    else:
        print ("Invalid Number")
        exit()
    
    tid = int(input("enter id : "))
    tl.append(str(tid))
    for j in range(0,i):
        if(tid!=id[j]):
            print("added to id list")
            id.append(tid)
            break
        else:
            print("no duplicate id values allowed")
            exit()
    print(tl)
    pws.append(tl)
    c.execute("INSERT INTO PASS VALUES (?,?,?,?,?)",tl)
c.execute("SELECT * FROM PASS")
#print(c.fetchall())
con.commit()
print ("			\n\nWELCOME TO THE DATABASE OF ELECTORAL ANALYSIS\n\n")
print ("MENU :   1.LOGIN \n\t 2.SIGN UP")
ch=int(input("ENTER YOUR CHOICE : "))
t=0
f=1
#print(pws)
if(ch==1):
    eid=input("ENTER YOUR ID : ")
    epw=input("PASSWORD : ")
    for j in range(0,n):
        if(eid==pws[j][4] and epw==pws[j][2]):
            t=1
            break
        else:
            t=0
    if t==1:
        opt = int(input("MENU:\n1. Representative\n 2. M.P list \n 3. Voters\n 4. Constituency\n 5. Party List\n"))
        if(opt==1):
            import vishva_1 as vish
        elif(opt==2):
            import app as ap1
        elif(opt==3):
            import sample1 as sam
        elif(opt==4):
            import constituency_JP as const
        elif(opt==5):
            import partylist_snb as snb
        else:
            print("Enter a valid option")
        exit()
    else:
        print ("ACCESS DENIED")
        exit()
else:
    eid=input("ENTER A EXISTING AUTHENTICATED ID : ")
    epw=input("ENTER THE RESPECTIVE PASSWORD : ")
    for j in range(0,n):
        if(eid==pws[j][4] and epw==pws[j][2]):
            t=1
            break
        else:
            t=0
    if t==1:
        print ("\nACCESS GRANTED\n")
        nul=[]
        print ("ENTER YOUR DETAILS BELOW")
        nul.append(input("ENTER YOUR NAME : "))
        email=(input("ENTER YOUR EMAIL : "))
        try:
            v = validate_email(email)
            email = v["email"]
            nul.append(email)
        except EmailNotValidError as e:
            print(str(e))
            exit()
        nul.append(input("ENTER YOUR Password : "))
        s = input("ENTER PHONE NUMBER :")
        if (isValid1(s) or isValid2(s)):  
            print ("Valid Number")
            nul.append(s)
        else : 
            print ("Invalid Number")
            exit()
        
        tid=int(input("enter id : "))
        nul2\
            .append(str(tid))
        for j in range(0,i):
            if(tid!=id[j]):
                print("added to id list")
                id.append(tid)
                break
            else:
                print("no duplicate id values allowed")
                exit()
        c.execute("INSERT INTO PASS VALUES (?,?,?,?,?)",nul)
        pws.append(nul)
        print ("\n\nNEW USER SUCCESSFULLY ADDED\n")
    else:
        print("\n\nUNAUTHORISED ACCESS....NEW USER ADDING PROCESS FAILED...\n\n")
        exit()
print(c.execute("SELECT * FROM PASS"))
print(c.fetchall())
print("\n\n THANK YOU FOR USING OUR DATABASE :)")
con.close()
