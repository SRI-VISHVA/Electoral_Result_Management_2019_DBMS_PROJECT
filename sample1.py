import csv
import sqlite3
csv_reader = csv.reader("election_result2k19sonali.csv")
con = sqlite3.connect(":memory:")
cur  = con.cursor()

# create the required table
#all the attributes with their respective constraint

cur.execute("Create table voting_list ( Aadhar number(3),Voter_name varchar(100) PRIMARY KEY, Age number(3),"
            " Sex char(3) ,"
            " C_id number(3),Constituency varchar(100), State_id varchar(3), "
            "State_name varchar(100),voting_status varchar(4));")

#Read the CSV file
with open('election_result2k19sonali.csv','r') as csv_file:
    for i in csv_file:
        print(i)


'''cur.executemany(
            "Insert into voting_list ( Aadhar, Voter_name, Age, Sex, "
            "C_id, Constituency, State_id, State_name, voting_status)"
            "values (?,?,?,?,?,?,?,?,?);", list(i))'''


#To insert into the database the new voters with all there details
#takes input for as many voters the user wants
#checks if the user wnts to insert the data
l='Y'
while True:
    l=input('Do you want to enter any details about the voters(Y/N):')
    if l=='N':
        break
    n=int(input("Enter the number of data you want to input: "))
    for i in  range(0,n):
        tl = []
        tl.append(input("Enter the aadhar : "))
        tl.append(input("Enter the name : "))
        tl.append(input("Enter the age : "))
        tl.append(input("Enter Sex: "))
        tl.append(input("Enter the Constituency: "))
        tl.append(input("Enter the Constituency id:  "))
        tl.append(input("Enter the state id : "))
        tl.append(input("Enter the state name: "))
        tl.append(input("Enter the Voting status: "))
        print("\n")
'''     try:
            cur.execute("insert into voting_list values (?,?,?,?,?,?,?,?,?)",tl)'''


csv_file.close()

