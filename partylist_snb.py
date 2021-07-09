import sqlite3
import csv
connection=sqlite3.connect('election_results2k19.db')
crsr=connection.cursor()
sql_command = """create table parties_list(s_no int(3),party_name varchar(100),leader_name varchar(52),founded_year int(4),reign varchar(26),ruled_area varchar(26));"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(1,'All India Trinamool congress','Mamata Banerjee',1998,'2011-2019','West bengal');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(2,'Bahujan samaj party','Mayawati',1984,'1993,1995,2003-05,2007-12','Utter pradesh');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(3,'Bharatiya janatha party','Amit shah',1980,'1996,1998-2004,2014-19','Lucknow,Varanasi');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(4,'Communist party of India','K.Subbarayan',1925,'1957-59,1969-77,1978-79','Lucknow');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(5,'Communist party of India(Marxist)','Sitaram vechury',1964,'1977-2011,1993-2018','West bengal,Tripura');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(6,'Indian national congress','Sonia gandhi',1885,'1947-77,1980-89,1991-96,2004-14','Assam,Amethi,UP');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(7,'Nationalist congress party','Sharad pawar',1999,'NULL','New delhi');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(8,'National people party','Conrad Sangma',2013,'2018-present','Megalaya');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(9,'Aam Aadhmi party','Aravind kejriwal',2012,'2013-2014,2015-present','Punjab');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(10,'All India anna dravida munnetra kazhagam','Edappadi palaniswami,O.Paneerselvam',1972,'1997-87,1988,1991-96,2001-06,2011-present','Tamil Nadu');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(11,'All India Forward bloc','Debebrata Biswas','1939','1956-61','West bengal');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(12,'All India Majilis-eeIttehadul Muslimeen','Asaduddin Qwaisi','1927','1974-77','Telangana');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(13,'All India N.R. Congress','N.Rangaswamy','2011','2011-15','Puducherry');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(14,'All India United Democratic Front','Bahruddin Ajmal','2004','2006-08','Assam');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(15,'All Jharkhand students Union','Sudesh Mahto','1986','1989-92','Jharkhand');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(16,'Asom Gana Parishad','Atol bora','1985','1987-91','Assam');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(17,'Biju Janatha Dal','Naveen Patnaik','1997','2002-2006','Orisha');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(18,'Bodoland people front','Hagrama mohilary','1985','1990-94','Assam');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(19,'Desiya murpokku dravida kazhagam','Vijayakanth','2005','2011-15','Tamil Nadu');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(20,'Dravida munnetra kazhagam','M.K.Stalin','1949','1967-77,1980-84,1996-98,1999-2014,2019-present','Tamil Nadu,Puducherry');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(21,'Goa forward party','Vijai sardesai','2016','2016-18','Goa');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(22,'Hill state people democratic party','Hopingstone Lyngdoh','1968','1970-77,1980-82,1985-89,1996-2004','Meghalaya');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(23,'Indian National Lok Dal','Om Prakash chautala','1999','1970-77,2000-05,2010-15','Haryana');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(24,'Indian Union Muslim league','Sayed Hyderali Shihab  thangal','1948','1956-67','Kerala,Tamil Nadu');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(25,'Indigenous people front of tripura','Mevar Kumar jamatia','2009','2011-15','Tripura');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(26,'Jammu and Kashmir national conference','Omar abdullah','1932','1943-54,1967-71','Jammu and Kashmir');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(27,'Jammu and Kashmir national Panthers party','Bhim Singh','1982','1993-94,19697-2001','Jammu and Kashmir');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(28,'Jammu and Kashmir national peopless democratic party','Mehbooba mufti','1998','2000-2010','Jammu and Kashmir');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(29,'Janta congress chhattisgarh','Ajit jogi','2016','2016-19','Chhattisgarh');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(30,'Janata Dal(secular)','H.D. Deve Gowda','1999','2000-07','Arunacha pradesh,Bihar');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(31,'Janata Dal(United)','Nitish kumar','1999','2007-14','Arunacha pradesh,Karnataka,Kerala');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(32,'Jharkhand mukti morcha','Shibu soren','1972','1988-94','Jharkhand');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(33,'Jharkhand vikas morcha(prajatantrik)','Babu lal marandi','2006','2008-12','Jharkhand');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(34,'Kerala congress(M)','C.F.Thomas','1979','1982-87','Kerala');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(35,'Lok Janshakti party','Ram vilas Paswan','2000','2005-10','Bihar');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(36,'Maharashtrawadi Gomantak party','Deepak Dhavalikar','2006','2007-09','Maharastra');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(37,'Mizo National front','Zoramthanga','1959','1964-69','Mizoram');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(38,'Maharastra Navnirman sena','Raj Thackeray','1963','1971-77','Maharastra');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(39,'Naga people Front','T.R. Zeliang','2002','2003-07','Manipur');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(40,'Mizoram people conference','Lalhmingthanga','1972','1980=87','Mizoram');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(41,'National democratic progressive party','Neiphiu Rio','2018','2018-present','Nagaland');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(42,'Pattali makkal katchi','Anbumani ramadoss','1989','2001-02,2004-05,2012-13','Puducherry');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(43,'Peoples democratic Alliance','Bd.Behring Anal','2012','2015-17','Manipur');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(44,'Peoples democratic front','P.N.Syiem','2017','2017-19','Meghalaya');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(45,'Peoples party of Arunachal','Tomo Riba','1987','1990-93,1995-99','Arunachal pradesh');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(46,'Rashtriya janatha party','Lulu prasad Yadav','1997','1998-2001,2003-05,2009-11','Bihar,Jharkhand');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(47,'Rashtriya lok dal','Chaudhary Ajit singh','1998','2000-02,2006-08','Utterpradesh');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(48,'Rashtriya loktantrik party','Hanuman beniwal','2018','2018-present','Rajasthan');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(49,'Rashtriya lok samta party','Upendra kushwaha','2013','2015-17','Bihar');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(50,'Revolutionary socialist','T.J.chandrachoodan','1940','1942-46,1956-59,1977-86','West bengal');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(51,'Samajwadi party','Akilesh yadav','1992','1992-94,1997-2000','Utter pradesh');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(52,'Shiromani akali dal','Sukhbir singh badal','1920','1948-57,1962-67,1975-77','Punjab');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(53,'Shiv sena','Uddhav Thackeray','1966','1971-75,1981-84,1992-97','Maharastra');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(54,'Sikkim democratic front','Pawan kumar chamling','1993','1995-96,1998-99','Sikkim');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(55,'Sikkim Krantkari morcha','Prem singh tamang','2013','2014-16','Sikkim');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(56,'Telangana rashtra samithi','Kalvakuntla Chandrasekar rao','2001','2001-05,2006-12,2013-18','Telangana');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(57,'Telugu desam party','N. chandra Babu Naidu','1982','1983-88,1989-97,1997-2000','Andra Pradesh,Telangana');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(58,'United Democratic party','Donkupar Roy','1972','1980-82,1988-92','Meghalaya');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(59,'YSR Congress party','Y.S. Jaganmohan Reddy','2011','2013-14','Andra pradesh,Telangana');"""
crsr.execute(sql_command)
sql_command="""insert into parties_list values(60,'Zoram Nationalist party','Lalduhawma','1997','2002-03,2007-09','Mizoram');"""
crsr.execute(sql_command)
connection.commit()
crsr.execute("select s_no,party_name,leader_name,founded_year,reign,ruled_area from parties_list")
for row in crsr:
    print("Serial number: ",row[0])
    print("Party Name: ",row[1])
    print("Leader of Party: ",row[2])
    print("Foundation Year: ",row[3])
    print("Reign or Ruling period: ",row[4])
    print("Area ruled: ",row[5],"\n")

print("Operation done successfully")

crsr.execute("UPDATE parties_list set reign='1957-59,1969-77,1978-79' where party_name='Communist party of India';" )
print("Total number of rows updated :", connection.total_changes)
connection.commit()
crsr.execute("select s_no,party_name,leader_name,founded_year,reign,ruled_area from parties_list")
for row in crsr:
    print("Serial number: ",row[0])
    print("Party Name: ",row[1])
    print("Leader of Party: ",row[2])
    print("Foundation Year: ",row[3])
    print("Reign or Ruling period: ",row[4])
    print("Area ruled: ",row[5],"\n")

print("Operation done successfully")
connection.commit()
crsr.execute("delete from parties_list where s_no=60;")
connection.commit()
crsr.execute("select s_no,party_name,leader_name,founded_year,reign,ruled_area from parties_list")
for row in crsr:
    print("Serial number: ",row[0])
    print("Party Name: ",row[1])
    print("Leader of Party: ",row[2])
    print("Foundation Year: ",row[3])
    print("Reign or Ruling period: ",row[4])
    print("Area ruled: ",row[5],"\n")

print("Operation done successfully")
connection.commit()
def insert():
    s=int(input('Enter serial number: '))
    p=input('Enter Party Name: ')
    l=input('Enter Leader Name: ')
    f=input('Enter Foundation year: ')
    r=input('Enter Reign or ruling period: ')
    a= input('Enter Area ruled: ')
    crsr.execute('insert into parties_list(s_no,party_name,leader_name,founded_year,reign,ruled_area) values(?,?,?,?,?,?)',(s,p,l,f,p,r,a))
    connection.commit()
    print("inserted Data successfully")
def read():
    crsr.execute('select * from parties_list')
    csv_file= csv.reader(open('DBMS_project.csv', 'r'))
    for row in csv_file:
        print(row)
def update():
    no=int(input('Enter  Serial number'))
    pn=int(input('Enter Party Name'))
    csv_file = csv.reader(open('DBMS_project.csv', 'r'))

    csv_file.execute('Update parties_list set party_name =? where s_no=?', (pn, no))
    connection.commit()
    print('updated Data successfully')

    def searchbypartyname():
        state = input("Enter Party Name:\n")
        csv_file = csv.reader(open('DBMS_project.csv', 'r'))
        crsr.execute('select * from parties_list where party_name=? ', (party_name,))

        for row in csv_file:
            if state == row[1]:
                print(row[0:])
    def searchbyleader():
        cons = input("Enter Party Leader name:\n")
        csv_file = csv.reader(open('DBMS_project.csv', 'r'))
        cursor.execute('select * from parties_list where leader_name=? ', (l_name,))

        for row in csv_file:
            if state == row[2]:
                print(row[0:])
    def searchbyfounedyear():
        state = input("Enter Foundation year:\n")
        csv_file = csv.reader(open('DBMS_project.csv', 'r'))

        for row in csv_file:
            if state == row[3]:
                print(row[0:])
    def searchbyruledarea():
        state = input("Enter Ruled Area\n")
        csv_file = csv.reader(open('DBMS_project.csv', 'r'))

        for row in csv_file:
            if state == row[4]:
                print(row[0:])
    i = 1
    while i == 1:
        a = int(input("Enter 1 to search data acccording to Party Name: \nEnter 2 to search data acccording to Party Leader Name: \nEnter 3 to search data acccording to Founded year: \nEnter 4 to search data acccording to Ruled Area:\nEnter 5 to exit: \n"))
        if a == 1:
            searchbystate()
        if a == 2:
            searchbyconstituency()
        if a == 3:
            searchbyelectedmp()
        if a == 4:
            searchbyparty()
        if a == 5:
            break
        if a >= 6:
            print("Wrong Option\n")
