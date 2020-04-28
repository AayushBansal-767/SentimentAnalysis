from tkinter import *
import SentimentSetup as s
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database='sentiment'
)
mycursor = mydb.cursor()

def getlist():
	mycursor.execute("select * from review")
	row=mycursor.fetchall()
	frm=Frame(f)
	scrollbar = Scrollbar(frm)
	scrollbar.pack( side = RIGHT, fill=Y )
	frm.pack(side=LEFT, padx=30)
	frm.place(x=100,y=400)

	tv=ttk.Treeview(frm,columns=(1,2,3,4),show="headings",height='5')
	tv.pack()
	tv.heading(1,text="Id")
	tv.column(1,minwidth=0,width=30, stretch=NO)
	tv.heading(2,text="Name")
	tv.column(2,minwidth=0,width=100, stretch=NO)
	tv.heading(3,text="Review")
	tv.column(3,minwidth=0,width=300, stretch=NO)
	tv.heading(4,text="Result")
	tv.column(4,minwidth=0,width=100, stretch=NO)
	for i in row:
		tv.insert('','end',values=i)
	
	

def getsent():
	Name=E1.get("1.0","end-1c")
	Review=E2.get("1.0","end-1c")
	if Review=='' or Name=='':
		showerror("Error","Required field is empty")
	else:
		Result=s.sentiment(Review)
		showinfo("Result", Result)
		sql="insert into review(name,review,result) values(%s,%s,%s)"

		mycursor.execute(sql,(Name,Review,Result))

		mydb.commit()
		E1.delete("1.0","end-1c")
		E2.delete("1.0","end-1c")

f = Tk()
f.configure(bg='grey') 
f.geometry("800x700")
f.resizable(False,False)
f.title("Review Analysis")
l1=Label(f,text="Reviewer Name",font=50,bg='grey')
l1.place(x=200,y=100)
E1=Text(f,width=30,height=1)
E1.place(x=350,y=100)
l2=Label(f,text="Review",font=50,bg='grey')
l2.place(x=200,y=150)
E2=Text(f,height=5,width=30)
E2.place(x=350,y=150)
B1=Button(f,text='Submit',width=10,height=1,font=30,command=getsent)
B1.place(x=230,y=300)
B2=Button(f,text='List all reviews',width=16,height=1,font=30,command=getlist)
B2.place(x=400,y=300)
l1=Label(f,text='',)
f.mainloop() 