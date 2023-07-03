##########        IMPORTED MODULES         ###########################
import mysql.connector
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from time import *
###########       GLOBALLY   DECLARED         #########################
im=['virat1','david1','rohit1','cris1','shane1','bumrah1','ab-de-villiers-sa','rashid','kane','shikhar']
l=[]
window1=Tk()
window1.configure(bg='blue4')
color1=['violet','orange','yellow','goldenrod','pink','midnightblue','red',]  
color=['red','goldenrod','orange','yellow','pink']
team=['csklogo','mi','kkr','dc']
teamm=['Chennai Super Kings','Mumbai Indians','Kolkata Knight Riders','Delhi Capitals']
#########################  ADMIN MENU ######################################
def terminal():
  def update():
        print("\n")
        print("\t\t\t\t1.\tUpdate Matches Played")
        print("\t\t\t\t2.\tUpdate Rank")
        print("\t\t\t\t3.\tUpdate Strike Rate")
        print("\t\t\t\t4.\tUpdate Bid Price")
        print("*"*94)
        choice=0
        choice=int(input("Enter your choice\t\t\t\t:"))
        if choice==1:
              print("*"*28,"To update the no. of matches played ","*"*28)
              conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="tiger",
                    database="system24")
              player=input("Enter the name of the player\t\t\t:")
              new=input("Enter the new no. of matches played\t\t:")
              cur=conn.cursor()
              sql=("update players set iplmatches="+new+" where name="+"'"+player+"'")

              cur.execute(sql)
              cur.execute("commit")
              conn.close()
              print("\n")
              print("*"*37,"RECORD IS UPDATED","*"*38)
              print("\n")
        if choice==2:
              print("*"*31,"To update the rank of a player","*"*31)
              conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="tiger",
                    database="system24")
              player=input("Enter the name of the player\t\t\t:")
              new=input("Enter the new rank\t\t\t\t:")
              cur=conn.cursor()
              sql=("update players set rank="+new+" where name="+"'"+player+"'")

              cur.execute(sql)
              cur.execute("commit")
              conn.close()
              print("\n")
              print("*"*37,"RECORD IS UPDATED","*"*38)
              print("\n")
        if choice==3:
               print("*"*28,"To update the strike rate  of  the player","*"*24)
               conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="tiger",
                    database="system24")
               player=input("Enter the name of the player\t\t\t:")
               new=input("Enter the strike rate of the player\t\t:")
               cur=conn.cursor()
               sql=("update players set strikerate ="+"'"+new+"'"+ "where name="+"'"+player+"'")
               cur.execute(sql)
               cur.execute("commit")
               conn.close()
               print("\n")
               print("*"*37,"RECORD IS UPDATED","*"*38)
               print("\n")
        if choice==4:
              print("*"*30,"To update the bid price of the player ","*"*24)
              conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="tiger",
                    database="system24")
              player=input("Enter the name of the player\t\t\t:")
              new=input("Enter the sold price of the team\t\t:")
              cur=conn.cursor()
              sql=("update players set bidprice="+"'"+new+"'"+ "where name="+"'"+player+"'")
              cur.execute(sql)
              cur.execute("commit")
              conn.close()
              print("\n")
              print("*"*37,"RECORD IS UPDATED","*"*38)
              print("\n")
              
  def insert():
           conn=mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="tiger",
              database="system24")
           cur=conn.cursor()
           n=int(input("Enter the the no. of records\t\t\t:"))
           print("*"*94)
           k=10
           for i in range(1,n+1):
              idp="a0"+str(k+1)
              na=input("Enter the name of the player\t\t\t:")
              country=input("Enter the country of the player\t\t\t:")
              specialism=input("Enter the specialism of the player\t\t:")
              matches=int(input("Enter the ipl matches played\t\t\t:"))
              rank=int(input("Enter the rank of the player\t\t\t:"))
              bid=input("Enter the bid price of the player\t\t:")
              run=int(input("Enter the runs taken by the player\t\t:"))
              wicket=int(input("Enter the wickets taken by the player\t\t:"))
              strike=input("Enter the strike rate of the player\t\t:")
              query=("insert into players(id,name,country,specialism,iplmatches,rank,bidprice,runstaken,wicketstaken,strikerate) values('{}','{}','{}','{}',{},{},'{}',{},{},'{}')".format(idp,na,country,specialism,matches,rank,bid,run,wicket,strike))
              cur.execute(query)
              cur.execute("commit")
              k=k+1
           conn.close()
           print("\n")
           print("*"*37,"RECORD IS INSERTED","*"*37)
           print("\n")
           
  def search():
      conn=mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="tiger",
          database="system24")
      l1=[]
      cur=conn.cursor()
      count=int(input("Enter the no. of records to be searched\t\t:"))
      for i in range(0,count):
          search=input("Enter the name of the player\t\t\t:")
          l1.append(search)
      t=tuple(l1)
      sql=("select id,name,country,specialism,iplmatches,rank,bidprice,strikerate from players where name in "+str(t))
      cur.execute(sql)
      rec2=cur.fetchall()
      print(tabulate(rec2,headers=["Id","Name","Country","Specialism","IPL Matches","Rank","Bid Price","Strike Rate"],tablefmt='grid'))
      conn.close()

  def delete():
      conn=mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="tiger",
          database="system24")
      cur=conn.cursor()
      name=input("Enter the name of the player to be deleted\t:")
      sql=("delete from players where name="+"'"+name+"'")
      cur.execute(sql)
      cur.execute("commit")
      print("\n")
      print("*"*37,"RECORD IS DELETED","*"*40)
      print("\n")
      conn.close()

  def display():
       conn=mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="tiger",
          database="system24")
       cur=conn.cursor()
       sql="select id,name,country,specialism,iplmatches,rank,bidprice,strikerate from players"
       cur.execute(sql)
       rec=cur.fetchall()
       conn.close()
       print(tabulate(rec, headers=["Id","Name","Country","Specialism","IPL Matches","Rank", "Bid Price","Strike Rate"],tablefmt='grid'))
  choice=0              
  while choice<6:
      print("\n")
      print('''\t
\t██╗██████╗ ██╗          █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
\t██║██╔══██╗██║         ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
\t██║██████╔╝██║         ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
\t██║██╔═══╝ ██║         ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
\t██║██║     ███████╗    ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
\t╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
''')
      print("*"*94)
      print('''\t\t\t\t
       █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
      ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
      ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
      ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
      ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
      ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
''')
      print("*"*94)
      print("\t\t\t\t1.\tTO INSERT RECORDS")
      print("\t\t\t\t2.\tTO UPDATE RECORDS")
      print("\t\t\t\t3.\tTO SEARCH RECORDS")
      print("\t\t\t\t4.\tTO DELETE RECORDS")
      print("\t\t\t\t5.\tTO DISPLAY RECORDS")
      print("*"*94)
      choice=int(input("Enter your choice\t\t\t\t:"))
      if choice==1:
                  print("*"*30,"To insert records into the table ","*"*29)
                  insert()
                  print("*"*94)
      elif choice==2:
                  print("*"*30,"To update records into the table","*"*30)
                  update()
                  print("*"*94)
      elif choice==3:
                  print("*"*33,"To search records from the table","*"*37)
                  search()
                  print("*"*104)
      elif choice==4:
                  print("*"*30,"To delete records from the table","*"*31)
                  delete()
                  print("*"*94)
      elif choice==5:
                  print("*"*40,"To display records from the table","*"*37)
                  display()
                  print("*"*112)
      else:
          print("*"*112)
          print("EXIT")
###################   MY SQL CONNECTIVITY #####################################
conn=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tiger",
  database="system24")
cur=conn.cursor()
sql1="select * from players"
cur.execute(sql1)
rec=cur.fetchall()
sql2="select * from iplteams"
cur.execute(sql2)
rec1=cur.fetchall()
length=len(rec)
length1=len(rec1)
############################## flashing   #####################################################
def flashing(d,window,t,a,b,font):
        def flash1(c):
                if c==-1:
                    c=len(d)-1
                lbl1=Label(window,text=t,font=("Perpetua Titling MT",font,'bold'),bg=d[c])
                lbl1.place(x=a,y=b)

                window.after(500,flash,c-1)
        def flash(c):
                if c==-1:
                    c=len(d)-1
                lbl2=Label(window,text=t,font=("Perpetua Titling MT",font,'bold'),bg=d[c])
                lbl2.place(x=a,y=b)
                window.after(500,flash1,c-1)
        flash(len(d)-1)
#############  WINDOW 4  (START BIDDING) ########################

def bidding(m):
  if m==0:
    window1.destroy()
  for j in range(m,m+1):
   
    ############################  WINDOW 4 PLAYERS AUCTION ################################
    if m<length:
            i=rec[j]
            window4=Tk()
            window4.geometry("1500x1000")
            window4.title("ONLINE AUCTION")
            window4.configure(bg="midnightblue")
            name=" "
            co=" "
            def g(en):
                if en==entry1:
                    name="Chennai Super Kings"
                    owner="CSK Cricket Limited"
                if en==entry2:
                    name="Mumbai Indians"
                    owner="Reliance Industries Limited"
                if en==entry3:
                    name="Kolkata Knight Riders"
                    owner="Shah Rukh Khan,Ajay Mehta"
                if en==entry4:
                    name="Delhi Capitals"
                    owner="GMR Group,JSW Sports"
                co=en.get()
                l.clear()
                l.append(name)
                l.append(co)
                l.append(owner)
            flashing(color,window4,"PLAYER INFORMATION",300,0,50)
            Label(window4,text="Name\t\t:"+i[1]+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=150)
            Label(window4,text="Country\t\t:"+str(i[2])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=180)
            Label(window4,text="Specialism\t\t:"+str(i[3])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=210)
            Label(window4,text="IPL Matches\t:"+str(i[4])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=240)
            Label(window4,text="Rank\t\t:"+str(i[5])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=270)
            Label(window4,text="Bid Price\t\t:"+str(i[8])+"\t\t\t",font=("Elephant",16),bg="pink").place(x=100,y=300)
            Label(window4,text="Runs Taken\t:"+str(i[10])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=330)
            Label(window4,text="Wickets Taken\t:"+str(i[11])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=360)
            Label(window4,text="Strike Rate\t\t:"+str(i[12])+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=390)
            ############################     image    #############################
            z=PhotoImage(file="\\\srlab\\tcdata\\system24\\Documents\\RIYA 12A\\project\\project images\\"+im[m]+".png")
            lbl2=Label(window4,image=z,bg="sky blue")
            lbl2.place(x=950,y=150)
            lbl2.image=z
            Label(window4,text="IPL TEAMS",font=("Stencil",22), padx=80, pady=20,bg="goldenrod").place(x=300,y=550)
            Label(window4,text="Chennai Super Kings\t:",font=("Elephant",16),bg="goldenrod").place(x=100,y=640)
            Label(window4,text="Mumbai Indians\t:",font=("Elephant",16),bg="goldenrod").place(x=100,y=680)
            Label(window4,text="Kolkata Knight Riders   :",font=("Elephant",16),bg="goldenrod").place(x=100,y=720)
            Label(window4,text="Delhi Capitals\t:",font=("Elephant",16),bg="goldenrod").place(x=100,y=760)
            
            entry1=Entry(window4,font=("Elephant",16))
            entry1.place(x=380,y=640)
            entry2=Entry(window4,font=("Elephant",16))
            entry2.place(x=380,y=680)
            entry3=Entry(window4,font=("Elephant",16))
            entry3.place(x=380,y=720)
            entry4=Entry(window4,font=("Elephant",16))
            entry4.place(x=380,y=760)
            
            entry1.bind('<Return>',g)
            entry2.bind('<Return>',g)
            entry3.bind('<Return>',g)
            entry4.bind('<Return>',g)
            
            b1=Button(window4,text="SUBMIT",bd=5,width=12,font=("Aharani",10),height=1,bg="gold",command=lambda:g(entry1)).place(x=730,y=640)
            b2=Button(window4,text="SUBMIT",bd=5,width=12,font=("Aharani",10),height=1,bg="gold",command=lambda:g(entry2))
            b2.place(x=730,y=680)
            b3=Button(window4,text="SUBMIT",bd=5,width=12,font=("Aharani",10),height=1,bg="gold",command=lambda:g(entry3))
            b3.place(x=730,y=720)
            b4=Button(window4,text="SUBMIT",bd=5,width=12,font=("Aharani",10),height=1,bg="gold",command=lambda:g(entry4))
            b4.place(x=730,y=760)
            def next2fun():
                 window4.destroy()
                 bidding(m+1)

            def graph2fun():
                 window4.destroy()
                 last(window4) 

            if m==length-1:
                 br=Button(window4,text="GRAPHS",bd=10,font=("Elephant",14),width=16,height=2,bg="green",command=lambda:graph2fun())
                 br.place(x=1010,y=650)
            else:
                 bnext=Button(window4,text="NEXT",bd=10,font=("Elephant",14),width=16,height=2,bg="green",command=lambda:next2fun())
                 bnext.place(x=1010,y=650)
           ################# WINDOW 4 (TIME  CALCULATION) #######################

            for z in range(30,-1,-1) :
               if z>=0:
                  flashing(color1,window4,"TIME LEFT",1020,490,26)
                  lbl1=Label(window4,font=("Elephant",24),bg="light coral",fg="red",text="  "+"00:00:"+str(z)+"\t  ")
                  lbl1.place(x=1010,y=550)
                  window4.update()
               sleep(1)
            entry1=Entry(window4,state='disabled',font=("Elephant",16))
            entry1.place(x=380,y=640)

            entry2=Entry(window4,state='disabled',font=("Elephant",16))
            entry2.place(x=380,y=680)

            entry3=Entry(window4,state='disabled',font=("Elephant",16))
            entry3.place(x=380,y=720)

            entry4=Entry(window4,state='disabled',font=("Elephant",16))
            entry4.place(x=380,y=760)
#######################  WINDOW 4 UPDATING TABLE(TEAM,SOLD PRICE)   #####################3
            def name1():

                    Label(window4,text="Team Name\t\t:"+l[0]+"\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=420)
                    sql3="update players set team = "+"'"+l[0]+"'"+" where name = "+"'"+i[1]+"'"
                    sql5="update players set owner = "+"'"+l[2]+"'"+" where name = "+"'"+i[1]+"'"
                    cur.execute(sql5)
                    cur.execute(sql3)
                    cur.execute("commit")
                    Label(window4,text="Sold Price\t\t:"+l[1]+"\t\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=450)
                    Label(window4,text="Owner\t\t:"+l[2]+"\t\t",font=("Elephant",16),bg="lightcoral").place(x=100,y=480)
                    sql4="update players set pricesold = "+"'"+l[1]+"'"+" where name = "+"'"+i[1]+"'"
                    cur.execute(sql4)
                    cur.execute("commit")
                    l.clear()
            name1()
#################    WINDOW 2( LOG IN )  #############################
def admin():

    window1.destroy() 
    window2=Tk()
    window2.geometry("1500x1000")
    window2.title("ONLINE AUCTION")
    window2.configure(bg="orange red")
    z=PhotoImage(file="\\\srlab\\tcdata\\system24\\Documents\\RIYA 12A\\project\\project images\\login.png")
    lbl2=Label(window2,image=z,bg="goldenrod")
    lbl2.place(x=0,y=0)
    lbl2.image=z
    color=['midnightblue','red','violet']
    flashing(color,window2,"LOGIN AS ADMIN",620,90,50)
    mi=StringVar()
    kkr=StringVar()
    dc=StringVar()

    def myfun():
     s=name.get()
     p=passwrd.get()
     if s=="admin" and p=="admin123":
          messagebox.showinfo("LOG IN SUCCESSFULL","WELCOME TO THE ONLINE AUCTION !!")
          window2.destroy()
          terminal()
     else:
        messagebox.showinfo("LOG IN UNSUCCESSFULL","WRONG USERNAME OR PASSWORD !!")
        window2.destroy()
    Label(window2,text="Enter the username\t:",font=("Perpetua Titling MT",24),bg='midnightblue',fg='white').place(x=250,y=350)
    Label(window2,text="Enter the password\t:",font=("Perpetua Titling MT",24),bg='midnightblue',fg='white').place(x=250,y=420)
    name=StringVar()
    passwrd=StringVar()
    Entry(window2,font=("Elephant",24),textvariable=name).place(x=850,y=350)
    Entry(window2, show="*",font=("Elephant",24),textvariable=passwrd).place(x=850,y=420)
    Button(window2,text="Submit",bd=10,font=("ELEPHANT",24),bg='brown2',command=myfun).place(x=680,y=530)
################### WINDOW 5 (IPL PLAYERS) ####################### 
def players():

    window5=Tk()
    window5.configure(bg='sienna2')
    window5.geometry("1500x1000")
    window5.title("ONLINE AUCTION")
    flashing(color,window5,"LIST OF PLAYERS FOR AUCTION",140,0,50)
    Label(window5,text="     ICC RANK \t |\tPLAYER NAME\t",font=("Elephant",22),bg='goldenrod2').place(x=200,y=100)
    for p in range(0,length):
        x=rec[p]
        Label(window5,text="\t"+str(x[5])+"\t |\t"+x[1],font=("Elephant",22),bg='sienna2').place(x=200,y=150+(p*60))
        Label(window5,text="",font=("Elephant",22),bg='sienna2').place(x=200,y=160+(p*30))
    bback=Button(window5,text="BACK",font=("Elephant",12),bd=10,width=16,height=2,bg="coral2",command= window5.destroy)
    bback.place(x=1100,y=650)
################### WINDOW 7 (IPL TEAMS) #######################
def iplteams():
  window1.destroy()
  teams(0)
def teams(b):
 
  if b<length1:

          for t in range(b,b+1):
              window7=Tk()
              window7.configure(bg='gold')
              window7.geometry("1500x1000")
              window7.title("ONLINE AUCTION")
              def next2fun():
                window7.destroy()
                teams(b+1)
              flashing(color,window7,"LIST OF REGISTERED TEAMS FOR AUCTION",150,30,40)
              Label(window7,text="LIST OF REGISTERED TEAMS FOR AUCTION",font=("COOPER BLACK",34,'bold'),bg='orange red').place(x=50,y=2200)
              x=rec1[t]
              Label(window7,text= "   TEAM\t  :"+x[1],font=("Elephant",28),bg='gold').place(x=38,y=200)
              Label(window7,text="\t",font=("Elephant",28),bg='gold').place(x=50,y=250)
              Label(window7,text="OWNER\t:"+x[2],font=("Elephant",28),bg='gold').place(x=55,y=300)
              Label(window7,text="ICC RANK\t\t |\tPLAYER NAME\t",font=("Elephant",22),bg='midnightblue',fg='white').place(x=50,y=400)
              query="select rank,name from players where team = '{}'".format(teamm[b])
              cur.execute(query)
              record=cur.fetchall()
              length2=len(record)
              for i in range(0,length2):
                Label(window7,text="      "+str(record[i][0])+"\t\t |\t"+record[i][1]+"\t",font=("Elephant",22),bg='gold').place(x=50,y=450+(50*i))
              t=PhotoImage(file="\\\srlab\\tcdata\\system24\\Documents\\RIYA 12A\\project\\project images\\"+team[b]+".png")
              lbl2=Label(window7,image=t,bg="gold")
              lbl2.place(x=1100,y=150)
              lbl2.image=t
              def next3fun():
                window7.destroy()
                teams(b+1)
              
              if b==length1-1:
                bnext=Button(window7,text="EXIT",bd=10,font=("Elephant",12),width=16,height=2,bg="green",command=lambda:window7.destroy())
                bnext.place(x=1250,y=650)
              else:
                bnext=Button(window7,text="NEXT",bd=10,font=("Elephant",12),width=16,height=2,bg="green",command=lambda:next3fun())
                bnext.place(x=1250,y=650)
############################# window 4 LAST PAGE (GRAPHS) ##################################
def last(window):
    window=Tk()
    window.geometry("1500x1000")
    window.title("ONLINE AUCTION")
    window.configure(bg="purple")
    flashing(color,window,"GRAPHS FOR COMPARISON",200,0,50)
    def sold():
      plt.title("COMPARISON BASED ON BIDDING AND SOLD PRICE")
      plt.xlabel("PLAYERS")
      plt.ylabel("BIDDING AND SOLD PRICE (in crores)")
      players=[]
      bid=[]
      sold=[]
      t=np.arange(0,10,1)
      for i in rec:
        players.append(i[1])
        bid.append(int(i[8][0]))
        sold.append(int(i[9][0]))
      print(players)
      print(bid)
      print(sold)
      plt.xticks(t,labels=players,horizontalalignment='right',rotation=10)
      plt.bar(t,bid,width=0.3,color="purple",label="Bidding Price")
      plt.bar(t+0.3,sold,width=0.3,color="yellow",label="Sold Price")
      plt.legend()
      plt.show()
    def eachteam():
      plt.title("COMPARISON BASED ON NUMBER OF PLAYERS IN EACH TEAM")
      teamss=[]
      count=[]
      global teamm

     
      query1="select team,count(name) from players group by team"
      cur.execute(query1)
      rec5=cur.fetchall()
      for i in rec5:
        teamss.append(i[0])
        count.append(i[1])
    
      explode=(0.1,0,0,0)
      plt.pie(count,labels=teamss,explode=explode,startangle=140,shadow=True,autopct="%1.1f%%")
      plt.show()
      
    Button(window,text="BID PRICE V/S SOLD PRICE OF EACH PLAYER",command=sold,font=("FORTE",22,'bold'),width=46,height=1,bg='green yellow',bd=10).place(x=280,y=200)
    Button(window,text="NUMBER OF PLAYERS IN EACH TEAM",command=eachteam,font=("FORTE",22,'bold'),width=46,height=1,bg='green yellow',bd=10).place(x=280,y=400)  
    
    bback=Button(window,text="EXIT",bd=10,font=("Elephant",12),width=16,height=2,bg="sandy brown",command=lambda:window.destroy())
    bback.place(x=590,y=650)
###########################################  GRAPH BUTTON ###############################33
def graphs():
    window1.destroy()
    window=Tk()
    window.geometry("1500x1000")
    window.title("ONLINE AUCTION")
    window.configure(bg="purple")
    flashing(color,window,"GRAPHICAL ANALYSIS",300,30,50)
    
    def runs():
      plt.title("PERFORMANCE BASED ON RUNS AND WICKETS TAKEN")
      plt.xlabel("PLAYERS")
      plt.ylabel("PERFORMANCE")
      players=[]
      run=[]
      wicket=[]
      t=np.arange(0,10,1)
      for i in rec:
        players.append(i[1])
        run.append(i[10])
        wicket.append(i[11])
      plt.xlabel("PLAYERS")
      plt.xticks(t,labels=players,horizontalalignment='right',rotation=10)
      plt.bar(t,run,width=0.3,color="red",label="RUNS TAKEN")
      plt.bar(t+0.3,wicket,width=0.3,color="blue",label="WICKETS TAKEN")
      plt.legend()
      plt.show()
      
    def strike():
      t=np.arange(0,10,1)
      plt.title("PERFORMANCE BASED ON STIKE RATE")
      plt.xlabel("PLAYERS")
      plt.ylabel("STRIKE RATE (IN %)")
      players=[]
      strike=[]
      for i in rec:
        players.append(i[1])
        strike.append(float(i[12]))
      plt.xticks(t,labels=players,horizontalalignment='right',rotation=10)
      plt.bar(t,strike,color="red")
      plt.show()
      
    def iplmatches():
      t=np.arange(0,10,1)
      plt.title("PERFORMANCE BASED ON NUMBER OF IPL MATCHES PLAYED")
      plt.xlabel("PLAYERS")
      plt.ylabel("IPL MATCHES PLAYED")
      players=[]
      ipl=[]
      for i in rec:
        players.append(i[1])
        ipl.append(i[4])
      plt.xticks(t,labels=players,horizontalalignment='right',rotation=10)
      plt.bar(t,ipl,color="red")
      plt.show()

    Button(window,text="RUNS AND WICKETS TAKEN",command=runs,font=("FORTE",22,'bold'),width=46,height=1,bg='green yellow',bd=10).place(x=280,y=200)
    Button(window,text="STRIKE RATE",command=strike,font=("FORTE",22,'bold'),width=46,height=1,bg='green yellow',bd=10).place(x=280,y=400)  
    Button(window,text="IPL MATCHES PLAYED",command=iplmatches,font=("FORTE",22,'bold'),width=46,height=1,bg='green yellow',bd=10).place(x=280,y=600)  
   
    bback=Button(window,text="EXIT",bd=10,font=("Elephant",12),width=16,height=2,bg="sandy brown",command=lambda:window.destroy())
    bback.place(x=1200,y=700)

def exitt():
  window1.destroy()
##################### WINDOW 1  (MAIN MENU) ######################################## 
def home():
    window1.configure(bg='blue4')
    window1.geometry("1500x1000")
    window1.title("ONLINE AUCTION")
    flashing(color,window1,"WELCOME TO THE ONLINE AUCTION OF IPL PLAYERS!!!!!",12,20,40)
    
    z=PhotoImage(file="\\\srlab\\tcdata\\system24\\Documents\\RIYA 12A\\project\\project images\\ipl.png")
    lbl2=Label(image=z,bg="sky blue")
    lbl2.place(x=0,y=0)
    lbl2.image=z
    Button(window1,text="ADMIN",command=admin,font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=40,y=200)  
    Button(window1,text="START BIDDING",command=lambda:bidding(0),font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=640,y=200)  
    Button(window1,text="GRAPHS",command=graphs,font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=640,y=290)  

    Button(window1,text="IPL PLAYERS",command=players,font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=1250,y=200)
    Button(window1,text="IPL TEAMS",command=lambda:iplteams(),font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=40,y=290)  
    Button(window1,text="EXIT",command=lambda:exitt(),font=("FORTE",22,'bold'),width=16,height=1,bg='green yellow',bd=10).place(x=1250,y=290)  
    
home()   

