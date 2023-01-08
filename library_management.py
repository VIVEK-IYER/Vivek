from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
  def __init__(self,root):
    self.root=root
    self.root.title("Library Management System")
    self.root.geometry("1366x768+0+0")
    

    ######################################variable#############################################
    self.member_var=StringVar()
    self.prn_var=StringVar()
    self.id_var=StringVar()
    self.firstname_var=StringVar()
    self.lastname_var=StringVar()
    self.address1_var=StringVar()
    self.address2_var=StringVar()
    self.postcode_var=StringVar()
    self.mobile_var=StringVar()
    self.bookid_var=StringVar()
    self.booktitle_var=StringVar()
    self.auther_var=StringVar()
    self.dateborrowed_var=StringVar()
    self.datedue_var=StringVar()
    self.daysonbook=StringVar()
    self.lateratefine_var=StringVar()
    self.dateoverdue=StringVar()
    self.finallprice=StringVar()


    lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
    lbltitle.pack(side=TOP,fill=X)

    frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    frame.place(x=0,y=130,width=1356,height=383)

    #===================================DataFrameLeft==========================================
    DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
    DataFrameLeft.place(x=0,y=5,width=810,height=348)

    lblmember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=2,pady=6)
    lblmember.grid(row=0,column=0,sticky=W)

    comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",font=("arial",12,"bold"),width=27)
    comMember["value"]=("Admin staf","Student","Lecturer")
    comMember.grid(row=0,column=1)

    lblref=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("arial",12,"bold"),padx=2,pady=6)
    lblref.grid(row=1,column=0,sticky=W)
    txtref=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.prn_var,width=29)
    txtref.grid(row=1,column=1)

    lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("arial",12,"bold"),padx=2,pady=6)
    lblTitle.grid(row=2,column=0,sticky=W)
    txtTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.id_var,width=29)
    txtTitle.grid(row=2,column=1)

    lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name:",font=("arial",12,"bold"),padx=2,pady=6)
    lblFirstName.grid(row=3,column=0,sticky=W)
    txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=29)
    txtFirstName.grid(row=3,column=1)


    lblLastName=Label(DataFrameLeft,bg="powder blue",text="Surname:",font=("arial",12,"bold"),padx=2,pady=6)
    lblLastName.grid(row=4,column=0,sticky=W)
    txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
    txtLastName.grid(row=4,column=1)

    lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("arial",12,"bold"),padx=2,pady=6)
    lblAddress1.grid(row=5,column=0,sticky=W)
    txtAddress1=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address1_var,width=29)
    txtAddress1.grid(row=5,column=1)

    lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("arial",12,"bold"),padx=2,pady=6)
    lblAddress2.grid(row=6,column=0,sticky=W)
    txtAddress2=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.address2_var,width=29)
    txtAddress2.grid(row=6,column=1)

    lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
    lblPostCode.grid(row=7,column=0,sticky=W)
    txtPostCode=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=29)
    txtPostCode.grid(row=7,column=1)

    lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile No:",font=("arial",12,"bold"),padx=2,pady=6)
    lblMobile.grid(row=8,column=0,sticky=W)
    txtMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
    txtMobile.grid(row=8,column=1)

    lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("arial",12,"bold"),padx=2,pady=4)
    lblBookId.grid(row=0,column=2,sticky=W)
    txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
    txtBookId.grid(row=0,column=3)

    lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
    lblBookTitle.grid(row=1,column=2,sticky=W)
    txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
    txtBookTitle.grid(row=1,column=3)

    lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author Name:",font=("arial",12,"bold"),padx=2,pady=6)
    lblAuthor.grid(row=2,column=2,sticky=W)
    txtAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
    txtAuthor.grid(row=2,column=3)

    lblDataBorrowed=Label(DataFrameLeft,bg="powder blue",text="Data Borrowed:",font=("arial",12,"bold"),padx=2,pady=6)
    lblDataBorrowed.grid(row=3,column=2,sticky=W)
    txtDataBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
    txtDataBorrowed.grid(row=3,column=3)

    lblDataDue=Label(DataFrameLeft,bg="powder blue",text="Data Due:",font=("arial",12,"bold"),padx=2,pady=6)
    lblDataDue.grid(row=4,column=2,sticky=W)
    txtDataDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
    txtDataDue.grid(row=4,column=3)

    lblDaysonBook=Label(DataFrameLeft,bg="powder blue",text="Days on Books:",font=("arial",12,"bold"),padx=2,pady=6)
    lblDaysonBook.grid(row=5,column=2,sticky=W)
    txtDaysonBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
    txtDaysonBook.grid(row=5,column=3)

    lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
    lblLateReturnFine.grid(row=6,column=2,sticky=W)
    txtLateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
    txtLateReturnFine.grid(row=6,column=3)

    lblDateOverdate=Label(DataFrameLeft,bg="powder blue",text="Date Over date:",font=("arial",12,"bold"),padx=2,pady=6)
    lblDateOverdate.grid(row=7,column=2,sticky=W)
    txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
    txtDateOverdate.grid(row=7,column=3)

    lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=6)
    lblActualPrice.grid(row=8,column=2,sticky=W)
    txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice,width=29)
    txtActualPrice.grid(row=8,column=3)




  





    #============================DataFrameRight========================

    DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("arial",12,"bold"))
    DataFrameRight.place(x=820,y=5,width=480,height=348)

    self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=28,height=16,padx=2,pady=6)
    self.txtBox.grid(row=0,column=2)

    listScrollbar=Scrollbar(DataFrameRight)
    listScrollbar.grid(row=0,column=1,sticky="ns")

    listBoooks=['Head Firt Book','Learn Python the Hard Way','Secrete Rashy','Python CookBook','Into to Machine Learning','Fluent Python','Machine Techno','My Python','Joss Ellif guru','Elite Jungle Python','Jungli Python','Mumbai Python','Mumbai Python','Pune Python','Machine Python','Advance Python','Inton Python','Red Chill Python','Ishq Python']

    
    def SelectBook(event=""):

        value=str(ListBox.get(ListBox.curselection))
        x=value
        if (x=="Head Firt Book"):
          self.bookid_var.set("BKID5454")
          self.booktitle_var.set("Python Manual")
          self.auther_var.set("Paul Berry")

          d1=datetime.datetime.today()
          d2=datetime.timedelta(days=15)
          d3=d1+d2
          self.dateborrowed_var(d1)
          self.datedue_var.set(d3)
          self.daysonbook.set(15)
          self.lateratefine_var.set("Rs.50")
          self.dateoverdue.set("NO")
          self.finallprice.set("Rs.788")



    
    ListBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=16,height=16)
    ListBox.bind("<<ListboxSelect>>",SelectBook)
    ListBox.grid(row=0,column=0,padx=4)
    listScrollbar.config(command=ListBox.yview)

    for item in listBoooks:
      ListBox.insert(END,item)


    # ==============================Button Frame========================
    Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    Framebutton.place(x=0,y=515,width=1356,height=60)

    btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
    btnAddData.grid(row=0,column=0)

    btnAddData=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
    btnAddData.grid(row=0,column=1)

    btnAddData=Button(Framebutton,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
    btnAddData.grid(row=0,column=2)

    btnAddData=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
    btnAddData.grid(row=0,column=3)

    btnAddData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
    btnAddData.grid(row=0,column=4)

    btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
    btnAddData.grid(row=0,column=5)



    #============================InformationFrame=======================
    FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    FrameDetails.place(x=0,y=575,width=1356,height=130)

    Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
    Table_frame.place(x=0,y=1,width=1306,height=110)


    xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
    yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
    self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

    xscroll.pack(side=BOTTOM,fill=X)
    yscroll.pack(side=RIGHT,fill=Y)

    xscroll.config(command=self.library_table.xview)
    yscroll.config(command=self.library_table.yview)




    self.library_table.heading("membertype",text="Member Type")
    self.library_table.heading("prnno",text="PRN No.")
    self.library_table.heading("title",text="Title")
    self.library_table.heading("firstname",text="First Name")
    self.library_table.heading("lastname",text="Last Name")
    self.library_table.heading("adress1",text="Address1")
    self.library_table.heading("adress2",text="Address2")
    self.library_table.heading("postid",text="Post ID")
    self.library_table.heading("mobile",text="Mobile Number")
    self.library_table.heading("bookid",text="Book ID")
    self.library_table.heading("booktitle",text="Book Title")
    self.library_table.heading("auther",text="Auther")
    self.library_table.heading("dateborrowed",text="Date of Borrowed")
    self.library_table.heading("datedue",text="Date Due")
    self.library_table.heading("days",text="DaysOnBook")
    self.library_table.heading("latereturnfine",text="LateReturnFine")
    self.library_table.heading("dateoverdue",text="DateOverDue")
    self.library_table.heading("finalprice",text="Final Price")

    self.library_table["show"]="headings"
    self.library_table.pack(fill=BOTH,expand=1)
    
    self.library_table.column("membertype",width=100)
    self.library_table.column("prnno",width=100)
    self.library_table.column("title",width=100)
    self.library_table.column("firstname",width=100)
    self.library_table.column("lastname",width=100)
    self.library_table.column("adress1",width=100)
    self.library_table.column("adress2",width=100)
    self.library_table.column("postid",width=100)
    self.library_table.column("mobile",width=100)
    self.library_table.column("bookid",width=100)
    self.library_table.column("booktitle",width=100)
    self.library_table.column("auther",width=100)
    self.library_table.column("dateborrowed",width=100)
    self.library_table.column("datedue",width=100)
    self.library_table.column("days",width=100)
    self.library_table.column("latereturnfine",width=100)
    self.library_table.column("dateoverdue",width=100)
    self.library_table.column("finalprice",width=100)

  def adda_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="I_vivek2001@1",database="Mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.auther_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook.get(),
                                                                                                            self.lateratefine_var.get(),
                                                                                                            self.dateoverdue.get(),
                                                                                                            self.finallprice.get()

                                                                                                         ))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success","Member Has been Inserted Successfully")


    


if __name__=="__main__":
  root=Tk()
  obj=LibraryManagementSystem(root)
  root.mainloop()

