import csv
import sqlite3
import time
import os
from vishva_2 import get_election_result, main_list, state_list, party_percentage
start_time = time.time
opt = int(input("MENU :\n 1. ADD NEW REPRESENTATIVE\n 2. DELETE A REPRESENTATIVE\n 3. UPDATE NAME\n 4. Analytics\n :"))
con = sqlite3.connect("election_results2k19.db")
cur = con.cursor()
if(opt == 1):
    osn = int(input("Enter OSN:\t"))
    candidate = input("\nName Of candidate:\t")
    party = input("\nParty Name:\t")
    evmvote = int(input("\nEnter EVM vote:\t"))
    postvote = int(input("\nEnter the POSTAL vote:\t"))
    totalvote = evmvote+postvote
    perofvote = float(input("\nEnter the Percentage Of vote:\t"))
    cid = int(input("\nEnter C.ID:\t"))
    constituency = input("\nEnter the constituency name:\t")
    sid = input("\nEnter the State ID:\t")
    state = input("\nEnter the State name:\t")
    todb = (osn, candidate, party, evmvote, postvote, totalvote, perofvote, cid, constituency, sid, state)
    try:
        cur.execute("INSERT INTO t (O_S_N , Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", todb)
        print("New Record Added Successfully")
    except sqlite3.IntegrityError as error:
        print("Error is " + error)
elif(opt == 2):
    cid = int(input("\nEnter C.ID:\t"))
    party = input("\nParty Name:\t")
    sid = input("\nEnter S.ID:\t")
    try:
        cur.execute("DELETE FROM t WHERE Party = ? AND Constituency_id = ? AND State_id = ?;", (party, cid, sid))
        print("Record Deleted")
    except sqlite3.IntegrityError as error:
        print("Error is " + error)
elif(opt == 3):
    cid = int(input("\nEnter C.ID:\t"))
    party = input("\nParty Name:\t")
    candidate = input("\nName Of candidate:\t")
    sid = input("\nEnter S.ID:\t")
    cur.execute("UPDATE t SET Candidate = ? where Party = ? AND Constituency_id = ? AND State_id = ?;", (candidate, party, cid, sid))
    print("Value Updated For " + candidate)
elif(opt == 4):
    if os.path.exists('election_results2k19.csv'):
        if os.path.exists('election_results2k19.db'):
            with open('election_results2k19.csv', mode='r', newline='') as csv1:
                csvreader = csv.reader(csv1)
                for row in csvreader:
                    try:
                        if os.path.exists('election_results2k19.db'):
                            i = 'Y'
                            while True:
                                s_name = input('Enter the state name:\t')
                                party_percentage(s_name)
                                i = input('Do you want to repeat [Y/N] ?\t')
                                if i == 'N':
                                    break
                            break
                        else:
                            # Writing csv into sqlite 3 database
                            con = sqlite3.connect("election_results2k19.db")
                            cur = con.cursor()
                            cur.execute(
                                "CREATE TABLE t (O_S_N NUMBER(2), Candidate VARCHAR(100) NOT NULL, Party VARCHAR(100), EVM_Votes NUMBER(6), Postal_Votes NUMBER(4), Total_Votes NUMBER(7), percen_of_Votes NUMBER(4,2), Constituency_id NUMBER(2), Constituency VARCHAR(100), State_id VARCHAR(3), State_name VARCHAR(100), CONSTRAINT PK_t PRIMARY KEY (State_id,Constituency_id,Party));")

                            with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
                                # csv.DictReader uses first line in file for column headings by default
                                dr = csv.DictReader(csvf)  # comma is default delimiter
                                to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'],
                                          i['Total_Votes'], i['%_of_Votes'], i['Constituency_id'], i['Constituency'],
                                          i['State_id'], i['State_name']) for i in dr]

                            cur.executemany(
                                "INSERT INTO t (O_S_N , Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                                to_db)
                            con.commit()
                            con.close()
                            i = 'Y'
                            while True:
                                s_name = input('Enter the state name:\t')
                                party_percentage(s_name)
                                i = input('Do you want to repeat [Y/N] ?\t')
                                if i == 'N':
                                    break
                            break
                    except:
                        with open('election_results2k19.csv', mode='w', newline='') as csv_file:
                            fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes',
                                          '%_of_Votes',
                                          'Constituency_id', 'Constituency', 'State_id', 'State_name']
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            writer.writeheader()

                        result_list = []
                        for cor in main_list:
                            for s_id, c_lt in cor.items():
                                for c_id, c_name in c_lt.items():
                                    result_list.append(get_election_result(int(c_id), c_name, s_id, state_list[s_id]))
                        with open('election_results2k19.csv', mode='a', newline='') as csv_file:
                            for city1 in result_list:
                                for person in city1:
                                    fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes',
                                                  'Total_Votes', '%_of_Votes', 'Constituency_id', 'Constituency',
                                                  'State_id', 'State_Name']
                                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                    writer.writerow({'O.S.N': person[0], 'Candidate': person[1], 'Party': person[2],
                                                     'EVM_Votes': person[3], 'Postal_Votes': person[4],
                                                     'Total_Votes': person[5], '%_of_Votes': person[6],
                                                     'Constituency_id': person[7], 'Constituency': person[8],
                                                     'State_id': person[9], 'State_Name': person[10]})

                        end_time = time.time()
                        writing_time = end_time - start_time
                        print(writing_time)

                        # Writing csv into sqlite 3 database
                        con = sqlite3.connect("election_results2k19.db")
                        cur = con.cursor()
                        cur.execute(
                            "CREATE TABLE t (O_S_N NUMBER(2), Candidate VARCHAR(100) NOT NULL, Party VARCHAR(100), EVM_Votes NUMBER(6), Postal_Votes NUMBER(4), Total_Votes NUMBER(7), percen_of_Votes NUMBER(4,2), Constituency_id NUMBER(2), Constituency VARCHAR(100), State_id VARCHAR(3), State_name VARCHAR(100), CONSTRAINT PK_t PRIMARY KEY (State_id,Constituency_id,Party);")

                        with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
                            # csv.DictReader uses first line in file for column headings by default
                            dr = csv.DictReader(csvf)  # comma is default delimiter
                            to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'],
                                      i['Total_Votes'], i['%_of_Votes'], i['Constituency_id'], i['Constituency'],
                                      i['State_id'], i['State_name']) for i in dr]

                        cur.executemany(
                            "INSERT INTO t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                            to_db)
                        con.commit()
                        con.close()
                        i = 'Y'
                        while True:
                            s_name = input('Enter the state name:\t')
                            party_percentage(s_name)
                            i = input('Do you want to repeat [Y/N] ?\t')
                            if i == 'N':
                                break
                        break
        else:
            with open('election_results2k19.csv', mode='r', newline='') as csv1:
                csvreader = csv.reader(csv1)
                for row in csvreader:
                    # Writing csv into sqlite 3 database
                    con = sqlite3.connect("election_results2k19.db")
                    cur = con.cursor()
                    cur.execute(
                        "CREATE TABLE t (O_S_N NUMBER(2), Candidate VARCHAR(100) NOT NULL, Party VARCHAR(100), EVM_Votes NUMBER(6), Postal_Votes NUMBER(4), Total_Votes NUMBER(7), percen_of_Votes NUMBER(4,2), Constituency_id NUMBER(2), Constituency VARCHAR(100), State_id VARCHAR(3), State_name VARCHAR(100), CONSTRAINT PK_t PRIMARY KEY (State_id,Constituency_id,Party);")

                    with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
                        # csv.DictReader uses first line in file for column headings by default
                        dr = csv.DictReader(csvf)  # comma is default delimiter
                        to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'],
                                  i['Total_Votes'],
                                  i['%_of_Votes'], i['Constituency_id'], i['Constituency'], i['State_id'],
                                  i['State_name']) for i in
                                 dr]

                    cur.executemany(
                        "INSERT INTO t (O_S_N , Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                        to_db)
                    con.commit()
                    con.close()
                    i = 'Y'
                    while True:
                        s_name = input('Enter the state name:\t')
                        party_percentage(s_name)
                        i = input('Do you want to repeat [Y/N] ?\t')
                        if i == 'N':
                            break
                    break

    else:
        with open('election_results2k19.csv', mode='w', newline='') as csv_file:
            fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes', '%_of_Votes',
                          'Constituency_id', 'Constituency', 'State_id', 'State_name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

        result_list = []
        for cor in main_list:
            for s_id, c_lt in cor.items():
                for c_id, c_name in c_lt.items():
                    result_list.append(get_election_result(int(c_id), c_name, s_id, state_list[s_id]))
        with open('election_results2k19.csv', mode='a', newline='') as csv_file:
            for city1 in result_list:
                for person in city1:
                    fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes',
                                  '%_of_Votes',
                                  'Constituency_id', 'Constituency', 'State_id', 'State_Name']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow(
                        {'O.S.N': person[0], 'Candidate': person[1], 'Party': person[2], 'EVM_Votes': person[3],
                         'Postal_Votes': person[4], 'Total_Votes': person[5], '%_of_Votes': person[6],
                         'Constituency_id': person[7], 'Constituency': person[8], 'State_id': person[9],
                         'State_Name': person[10]})

        # Writing csv into sqlite 3 database
        con = sqlite3.connect("election_results2k19.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE t (O_S_N NUMBER(2), Candidate VARCHAR(100) NOT NULL, Party VARCHAR(100), EVM_Votes NUMBER(6), Postal_Votes NUMBER(4), Total_Votes NUMBER(7), percen_of_Votes NUMBER(4,2), Constituency_id NUMBER(2), Constituency VARCHAR(100), State_id VARCHAR(3), State_name VARCHAR(100), CONSTRAINT PK_t PRIMARY KEY (State_id,Constituency_id,Party);")

        with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(csvf)  # comma is default delimiter
            to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'], i['Total_Votes'],
                      i['%_of_Votes'], i['Constituency_id'], i['Constituency'], i['State_id'], i['State_name']) for i in
                     dr]

        cur.executemany(
            "INSERT INTO t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            to_db)
        con.commit()
        con.close()
        i = 'Y'
        while True:
            s_name = input('Enter the state name:\t')
            party_percentage(s_name)
            i = input('Do you want to repeat [Y/N] ?\t')
            if i == 'N':
                break
else:
    print("Enter a valid Option")
con.commit()
con.close()
