from random import *

import datetime
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='',database='dbit')
cur=con.cursor()

print("Press 1. to issue book")
print("Press 2. to return book")
print("Press 3. to to check status")
print("Press 4. to check fine")
print("Press 5. exit ")

n=int(input("enter the choice : "))

if n==1:
    sna=input("enter ur name : ")
    ide=input("enter ur id : ")
    sco=input("enter ur course name : ")
    sbr = input("enter ur branch : ")
    bna = input("enter book name : ")
    baname=input("enter book author name : ")

    x = 0
    s="select * from book "
    cur.execute(s)

    bid="dbit"
    z=int(randint(1,10000))
    for d in cur:
        x=x+1
    if x>0:
        x=x+1
        x=x+z
        bid=bid+str(x)
    else:
        bid="dbit101"
    x = str(datetime.date.today())
    z="issued"

    s="insert into book(stdid,stdname,stdcourse,stdbranch,bookname,bookid,bookauthorname,issuedate,status ) values('"+ide+"','"+sna+"','"+sco+"','"+sbr+"','"+bna+"','"+bid+"','"+baname+"','"+x+"','"+z+"')"
    cur.execute(s)

    con.commit()
    print("book issued and record updated to database")


if n==2:
    bid=input("enter the book id : ")
    stdid=input("enter student id : ")
    stdname=input("enter student name : ")
    r="returned"
    s="select * from book where bookid='"+bid+"' and stdid='"+stdid+"' and stdname='"+stdname+"' "
    cur.execute(s)
    x=0
    for d in cur:
         x=x+1
    if x>0:
        v=str(datetime.date.today())
        s = "update book set status='" + r + "' where stdid='" + stdid + "'  "
        cur.execute(s)
        s="update book set returndate='"+v+"' where stdid='"+stdid+"' "
        cur.execute(s)
        con.commit()
        print("book returned and record updated to database")
    else:
        print("invalid account ")

if n==3:
    stdid=input("enter student id : ")
    s="select * from book where stdid='"+stdid+"' "
    cur.execute(s)
    print(" | std id   |  name | course |branch|subject|book id |  author name    |  issue date | return date|  status |" )
    x=0
    for d in cur:
          x=x+1
          if x>0:
             print(d)

    for d in cur:
        if x==0:
            print("invalid student id ")
