from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from PIL import ImageTk
import pymysql
from tkinter import messagebox,ttk
import time
import os
import tempfile
from datetime import datetime

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="Login bg.jpeg")
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=120, y=150, height=340, width=500)

        title = Label(Frame_login, text="Login here", font=("Impact", 35, "bold"), fg="#d77337", bg="white")
        title.place(x=90, y=30)

        desc = Label(Frame_login, text="Employee & Admin Login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        desc.place(x=90, y=100)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        lbl_user.place(x=90, y=140)

        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="#f0f0f0")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        lbl_pass.place(x=90, y=210)

        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="#f0f0f0", show='*')
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        login_btn = Button(self.root, text="Login", command=self.login_function, fg="white", bg="#d77337", font=("times new roman", 20))
        login_btn.place(x=300, y=470, width=180, height=40)

    def check_connection_emp(self):
        try:
            con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
            cur=con.cursor()
            cur.execute("select * from epms_salary where e_id=%s",(self.txt_user.get()))
            rows=cur.fetchall()
            print("empst")
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

    def login_function(self):
        isAdmin=False
        self.username=self.txt_user.get()
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() == "123456" and self.txt_user.get() == "Rajat":
            isAdmin=False
        elif self.txt_pass.get() == "123456" and self.txt_user.get() == "Viraj":
            isAdmin=False
        elif self.txt_pass.get() == "123456" and self.txt_user.get() == "Soundarya":
            isAdmin=False
        elif self.txt_pass.get() == "admin" and self.txt_user.get() == "admin":
            isAdmin=True
        if(isAdmin):
            self.root.destroy()  # Close login window
            self.root = Tk()
            # self.employeeRoot = Tk()
            self.root.title("Employee Payroll Management System  | by Anshika")
            self.root.geometry("1530x790+0+0")
            self.root.config(bg="white")
            title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=350,y=0)
            btn_emp=Button(self.root,text="All Employee's`",command=self.employee_frame,font=("times new roman",15),bg="gray",fg="white").place(x=1100,y=10,height=30,width=140)

       #=========Frame1======================================
        #=========variable=====================================

            self.var_emp_code=StringVar()
            self.var_designation=StringVar()
            self.var_name=StringVar()
            self.var_age=StringVar()
            self.var_gender=StringVar()
            self.var_email=StringVar()
            self.var_hr_location=StringVar()
            self.var_dob=StringVar()
            self.var_doj=StringVar()
            self.var_experience=StringVar()
            self.var_proof_id=StringVar() #======Adhaar card=========
            self.var_contact_no=StringVar()
            self.var_status=StringVar()



            Frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
            Frame1.place(x=10,y=70,width=750,height=620)
            title2=Label(Frame1,text="Employee Details",font=("times new roman",22,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=250,y=0)

            lbl_code=Label(Frame1,text="Employee code",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=70)
            self.txt_code=Entry(Frame1,font=("times new roman",15,"bold"),textvariable=self.var_emp_code,bg="#FAFCE8",fg="black")
            self.txt_code.place(x=170,y=70,width=200)
            btn_Search=Button(Frame1,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#1976D2",fg="black").place(x=390,y=67,height=30)

        #part-1
            lbl_Designation=Label(Frame1,text="Designation",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=120)
            txt_Designation=Entry(Frame1,text="Designation",font=("times new roman",15,"bold"),textvariable=self.var_designation,bg="#FAFCE8",fg="black").place(x=170,y=125,width=200)
            lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=120)
            txt_dob=Entry(Frame1,text="D.O.B",font=("times new roman",15,"bold"),textvariable=self.var_dob,bg="#FAFCE8",fg="black").place(x=520,y=120)

            #part-2
            lbl_Name=Label(Frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=170)
            txt_Name=Entry(Frame1,text="Name",font=("times new roman",15,"bold"),textvariable=self.var_name,bg="#FAFCE8",fg="black").place(x=170,y=173,width=200)
            lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=170)
            txt_doj=Entry(Frame1,text="D.O.J",font=("times new roman",15,"bold"),textvariable=self.var_doj,bg="#FAFCE8",fg="black").place(x=520,y=170)

            #part-3
            lbl_age=Label(Frame1,text="Age",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=220)
            txt_age=Entry(Frame1,text="Age",font=("times new roman",15,"bold"),textvariable=self.var_age,bg="#FAFCE8",fg="black").place(x=170,y=223,width=200)
            lbl_Experience=Label(Frame1,text="Experience",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=220)
            txt_Experience=Entry(Frame1,text="Experience",font=("times new roman",15,"bold"),textvariable=self.var_experience,bg="#FAFCE8",fg="black").place(x=520,y=220)

            #part-4
            lbl_gender=Label(Frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=270)
            txt_gender=Entry(Frame1,text="Gender",font=("times new roman",15,"bold"),textvariable=self.var_gender,bg="#FAFCE8",fg="black").place(x=170,y=270,width=200)
            lbl_proofId=Label(Frame1,text="Proof Id",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=270)
            txt_proofId=Entry(Frame1,text="Proof Id",font=("times new roman",15,"bold"),textvariable=self.var_proof_id,bg="#FAFCE8",fg="black").place(x=520,y=270)

            #part-5
            lbl_Email=Label(Frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=320)
            txt_Email=Entry(Frame1,text="Email",font=("times new roman",15,"bold"),textvariable=self.var_email,bg="#FAFCE8",fg="black").place(x=170,y=320,width=200)
            lbl_ContactNo=Label(Frame1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=320)
            txt_ContactNo=Entry(Frame1,text="Contact No",font=("times new roman",15,"bold"),textvariable=self.var_contact_no,bg="#FAFCE8",fg="black").place(x=520,y=320)

            #prat-6
            lbl_hiredLocation=Label(Frame1,text="Hired Location",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=372)
            txt_hiredLocation=Entry(Frame1,text="Hired Location",font=("times new roman",15,"bold"),textvariable=self.var_hr_location,bg="#FAFCE8",fg="black").place(x=170,y=372,width=200)
            lbl_Status=Label(Frame1,text="Status",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=372)
            txt_Status=Entry(Frame1,text="Status",font=("times new roman",15,"bold"),textvariable=self.var_status,bg="#FAFCE8",fg="black").place(x=520,y=372)

            #part-7
            lbl_address=Label(Frame1,text="Address",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=422)
            self. txt_address=Text(Frame1,font=("times new roman",15,"bold"),bg="#FAFCE8",fg="black")
            self.txt_address.place(x=170,y=425,width=550,height=170)







        #==================Frame2=======================================



            self.var_salary=StringVar()
            self.var_absent=StringVar()
            self.var_medical=StringVar()
            self.var_pf=StringVar()
            self.var_convence=StringVar()
            self.var_net_salary=StringVar()

            Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="White")
            Frame2.place(x=770,y=70,width=580,height=300)


            title3=Label(Frame2,text="Employee Salary Details",font=("times new roman",22,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=140,y=0)

            #lbl_month=Label(Frame2,text="Month",font=("times new roman",14,"bold"),bg="white",fg="black").place(x=10,y=70)
            #lbl_month=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_month,bg="#FAFCE8",fg="black").place(x=85,y=70,width=100)

            #lbl_year=Label(Frame2,text="Year",font=("times new roman",14,"bold"),bg="white",fg="black").place(x=200,y=69)
            #lbl_year=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_year,bg="#FAFCE8",fg="black").place(x=260,y=70,width=100)

            lbl_Salary=Label(Frame2,text="B.Salary",font=("times new roman",14,"bold"),bg="white",fg="black").place(x=10,y=70)
            lbl_Salary=Entry(Frame2,font=("times new roman",15,"bold"),textvariable=self.var_salary,bg="#FAFCE8",fg="black").place(x=90,y=70,width=100)



        #part-1
            #lbl_Days=Label(Frame2,text="Days",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=110)
            #txt_Days=Entry(Frame2,text="Days",font=("times new roman",15,"bold"),textvariable=self.var_t_days,bg="#FAFCE8",fg="black").place(x=85,y=110,width=100)
            lbl_absent=Label(Frame2,text="absent",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=200,y=69)
            txt_absent=Entry(Frame2,text="absent",font=("times new roman",15,"bold"),textvariable=self.var_absent,bg="#FAFCE8",fg="black").place(x=270,y=70,width=110)

            #part-2
            lbl_Medical=Label(Frame2,text="Medical",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=150)
            txt_Medical=Entry(Frame2,text="Medical",font=("times new roman",15,"bold"),textvariable=self.var_medical,bg="#FAFCE8",fg="black").place(x=105,y=150,width=185)
            lbl_pf=Label(Frame2,text="P.F",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=310,y=150)
            txt_pf=Entry(Frame2,text="P.F",font=("times new roman",15,"bold"),textvariable=self.var_pf,bg="#FAFCE8",fg="black").place(x=365,y=150,width=185)

            #part-3
            lbl_convence=Label(Frame2,text="Convence",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=190)
            txt_convence=Entry(Frame2,text="Convence",font=("times new roman",15,"bold"),textvariable=self.var_convence,bg="#FAFCE8",fg="black").place(x=120,y=190,width=135)
            lbl_NetSalary=Label(Frame2,text="Net Salary",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=295,y=190)
            txt_NetSalary=Entry(Frame2,text="Net Salary",font=("times new roman",15,"bold"),textvariable=self.var_net_salary,bg="#FAFCE8",fg="black").place(x=410,y=190,width=140)

            btn_Calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",15),bg="light yellow",fg="black").place(x=100,y=225,height=30,width=140)
            self.btn_Save=Button(Frame2,text="Save",command=self.add,font=("times new roman",15),bg="light green",fg="black")
            self.btn_Save.place(x=250,y=225,height=30,width=140)
            btn_Clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",15),bg="Red",fg="black").place(x=400,y=225,height=30,width=140)

            self.btn_update=Button(Frame2,text="Update",command=self.update,font=("times new roman",15),bg="light blue",fg="black")
            self.btn_update.place(x=100,y=260,height=30,width=140)
            self.btn_delete=Button(Frame2,text="Delete",command=self.delete,font=("times new roman",15),bg="orange",fg="black")
            self.btn_delete.place(x=250,y=260,height=30,width=140)


            #================Frame3==============================================

            Frame3=Frame(self.root,bd=5,relief=RIDGE,bg="White")
            Frame3.place(x=770,y=380,width=580,height=310)

            #=================calculator Framework================================
            self.var_txt=StringVar()
            self.var_operator=''
            def btn_click(num):
                self.var_operator=self.var_operator+str(num)
                self.var_txt.set(self.var_operator)

            def result():
                res=str(eval(self.var_operator))
                self.var_txt.set(res)
                self.var_operator=''
            def clear_cal():
                self.var_txt.set('')
                self.var_operator=''



            Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
            Cal_Frame.place(x=2,y=1,width=280,height=300)


            txt_Result=Entry(Cal_Frame,bg='lightyellow',textvariable=self.var_txt,font=("times new roman",15),justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)

            #========================================Row 1==============================================

            btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=42,w=70,h=65)
            btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=69,y=42,w=70,h=65)
            btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=138,y=42,w=70,h=65)
            btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=207,y=42,w=70,h=65)

            #==========================================Row2===============================================

            btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=107,w=70,h=65)
            btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=69,y=107,w=70,h=65)
            btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=138,y=107,w=70,h=65)
            btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=207,y=107,w=70,h=65)

            #==========================================Row3===============================================

            btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=172,w=70,h=65)
            btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=69,y=172,w=70,h=65)
            btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=138,y=172,w=70,h=65)
            btn_min=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=207,y=172,w=70,h=65)
        # btn_per=Button(Cal_Frame,text='%',command=lambda:btn_click('%'),font=("times new roman",15,"bold")).place(x=207,y=172,w=69,h=65)

            #==========================================Row4===============================================

            btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=237,w=45,h=62)
            btn_Clear=Button(Cal_Frame,text='c',command=clear_cal,font=("times new roman",15,"bold")).place(x=45,y=237,w=45,h=62)
            btn_sum=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=90,y=237,w=60,h=62)
            btn_dot=Button(Cal_Frame,text='.',command=lambda:btn_click('.'),font=("times new roman",15,"bold")).place(x=150,y=237,w=55,h=62)
            btn_equal=Button(Cal_Frame,text='=',command=result,font=("times new roman",15,"bold")).place(x=207,y=237,w=69,h=65)


            #===========================================Salary Frame=========================================

            sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
            sal_Frame.place(x=285,y=1,width=290,height=300)
            title_sal=Label(sal_Frame,text="Salary Receipt",font=("times new roman",20,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=50,y=0,height=45)



            sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
            sal_Frame2.place(x=0,y=44,relwidth=1,height=225)
            self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------
Employee ID\t\t:
Salary Of\t\t:  Mon-YYYY
Generated On\t\t:  DD-MM-YYYY
------------------------------------------
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.-------
Net Salary\t\t:  Rs.-------
------------------------------------------
This is computer generated slip, not
required any signature

'''


            scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
            scroll_y.pack(fill=Y,side=RIGHT)

            self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",12),bg='lightyellow',yscrollcommand=scroll_y.set)
            self.txt_salary_receipt.pack(fill=BOTH,expand=1)
            scroll_y.config(command=self.txt_salary_receipt.yview)
            self.txt_salary_receipt.insert(END,self.sample)


            btn_Print=Button(sal_Frame,text="Print",command=self.Print_data,font=("times new roman",15,"bold"),bg="lightblue",fg="black").place(x=167,y=268,height=30,width=120)

            self.check_connection()

#=====================Employee Area=========================================================
        else:
           # messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}", parent=self.root)
            self.root.destroy()  # Close login window
            self.root3 = Tk()

            self.var_emp_code2=StringVar()
            self.var_designation2=StringVar()
            self.var_name2=StringVar()
            self.var_age2=StringVar()
            self.var_gender2=StringVar()
            self.var_email2=StringVar()
            self.var_hr_location2=StringVar()
            self.var_dob2=StringVar()
            self.var_doj2=StringVar()
            self.var_experience2=StringVar()
            self.var_contact_no2=StringVar()
            self.var_proof_id2=StringVar()
            self.var_status2=StringVar()
            self.var_Address2=StringVar()

                # self.employeeRoot = Tk()
            self.root3.title("Employee Area")
            self.root3.geometry("1530x790+0+0")
            self.root3.config(bg="white")

            title=Label(self.root3,text="Enter Employee Area",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w" ,padx=10).place(x=350,y=0)
            Frame_a=Frame(self.root3,bd=5,relief=RIDGE,bg="white")
            Frame_a.place(x=60,y=70,width=750,height=700)
            title2=Label(Frame_a,text="Employee Details",font=("times new roman",22,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=250 ,y=0)
            lbl_code=Label(Frame_a,text="Employee code",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=70)
            self.txt_code=Entry(Frame_a,font=("times new roman",15,"bold"),textvariable=self.var_emp_code2,bg="#FAFCE8",fg="black")
            self.txt_code.place(x=170,y=70,width=200)

            lbl_Designation=Label(Frame_a,text="Designation",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=120)
            txt_Designation=Entry(Frame_a,text="Designation",font=("times new roman",15,"bold"),textvariable=self.var_designation2 ,bg="#FAFCE8",fg="black").place(x=170,y=125,width=200)

            lbl_dob=Label(Frame_a,text="D.O.B",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=120)
            txt_dob=Entry(Frame_a,text="D.O.B",font=("times new roman",15,"bold"),textvariable=self.var_dob2,bg="#FAFCE8",fg="black").place(x=520,y=120)

            lbl_Name=Label(Frame_a,text="Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=170)
            txt_Name=Entry(Frame_a,text="Name",font=("times new roman",15,"bold"),textvariable=self.var_name2,bg="#FAFCE8",fg="black").place(x=170,y=173,width=200)
            lbl_doj=Label(Frame_a,text="D.O.J",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=170)
            txt_doj=Entry(Frame_a,text="D.O.J",font=("times new roman",15,"bold"),textvariable=self.var_doj2,bg="#FAFCE8",fg="black").place(x=520,y=170)

            #part-3
            lbl_age=Label(Frame_a,text="Age",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=220)
            txt_age=Entry(Frame_a,text="Age",font=("times new roman",15,"bold"),textvariable=self.var_age2,bg="#FAFCE8",fg="black").place(x=170,y=223,width=200)
            lbl_Experience=Label(Frame_a,text="Experience",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=220)
            txt_Experience=Entry(Frame_a,text="Experience",font=("times new roman",15,"bold"),textvariable=self.var_experience2,bg="#FAFCE8",fg="black").place(x=520,y=220)

            #part-4
            lbl_gender=Label(Frame_a,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=270)
            txt_gender=Entry(Frame_a,text="Gender",font=("times new roman",15,"bold"),textvariable=self.var_gender2,bg="#FAFCE8",fg="black").place(x=170,y=270,width=200)
            lbl_proofId=Label(Frame_a,text="Proof Id",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=270)
            txt_proofId=Entry(Frame_a,text="Proof Id",font=("times new roman",15,"bold"),textvariable=self.var_proof_id2,bg="#FAFCE8",fg="black").place(x=520,y=270)

            #part-5
            lbl_Email=Label(Frame_a,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=320)
            txt_Email=Entry(Frame_a,text="Email",font=("times new roman",15,"bold"),textvariable=self.var_email2,bg="#FAFCE8",fg="black").place(x=170,y=320,width=200)
            lbl_ContactNo=Label(Frame_a,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=320)
            txt_ContactNo=Entry(Frame_a,text="Contact No",font=("times new roman",15,"bold"),textvariable=self.var_contact_no2,bg="#FAFCE8",fg="black").place(x=520,y=320)

            #prat-6
            lbl_hiredLocation=Label(Frame_a,text="Hired Location",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=372)
            txt_hiredLocation=Entry(Frame_a,text="Hired Location",font=("times new roman",15,"bold"),textvariable=self.var_hr_location2,bg="#FAFCE8",fg="black").place(x=170,y=372,width=200)
            lbl_Status=Label(Frame_a,text="Status",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=395,y=372)
            txt_Status=Entry(Frame_a,text="Status",font=("times new roman",15,"bold"),textvariable=self.var_status2,bg="#FAFCE8",fg="black").place(x=520,y=372)

            #part-7
            lbl_address=Label(Frame_a,text="Address",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=10,y=422)
            self.txt_address=Text(Frame_a,font=("times new roman",15,"bold"),bg="#FAFCE8",fg="black")
            self.txt_address.place(x=170,y=425,width=550,height=170)


            self.btn_update=Button(Frame_a,text="Update",font=("times new roman",15),bg="light blue",fg="black")
            self.btn_update.place(x=380,y=605,height=30,width=140)

            Frame_b=Frame(self.root3,bd=5,relief=RIDGE,bg="White")
            Frame_b.place(x=810,y=450,width=400,height=315)

            



            #===========================================Salary Frame=========================================

            sal_Frame2=Frame(Frame_b,bg="white",bd=2,relief=RIDGE)
            sal_Frame2.place(x=95,y=1,width=290,height=300)
            title_sal=Label(sal_Frame2,text="Salary Receipt",font=("times new roman",20,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=50,y=0,height=45)



            sal_Frame2=Frame(sal_Frame2,bg='white',bd=2,relief=RIDGE)
            sal_Frame2.place(x=0,y=44,relwidth=1,height=225)
            self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------
Employee ID\t\t:
Salary Of\t\t:  Mon-YYYY
Generated On\t\t:  DD-MM-YYYY
------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.-------
Net Salary\t\t:  Rs.-------
------------------------------------------
This is computer generated slip, not
required any signature

'''


            scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
            scroll_y.pack(fill=Y,side=RIGHT)

            self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",12),bg='lightyellow',yscrollcommand=scroll_y.set)
            self.txt_salary_receipt.pack(fill=BOTH,expand=1)
            scroll_y.config(command=self.txt_salary_receipt.yview)
            self.txt_salary_receipt.insert(END,self.sample)


            btn_Print=Button(Frame_b,text="Print",font=("times new roman",15,"bold"),bg="lightblue",fg="black").place(x=167,y=270,height=30,width=120)

            #=======Announcement Frame=========
            Frame_c=Frame(self.root3,bd=5,relief=RIDGE,bg="white")
            Frame_c.place(x=810,y=70,width=400,height=350)
            #title2=Label(Frame_c,text="Announcement Corner",font=("times new roman",22,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=60,y=0)

            sal_Frame3=Frame(Frame_c,bg="white",bd=2,relief=RIDGE)
            sal_Frame3.place(x=95,y=1,width=290,height=300)
            title_sal=Label(sal_Frame3,text="Announcement",font=("times new roman",20,"bold"),bg="#EBF5FB",fg="black",anchor="w").place(x=50,y=0,height=45)



            sal_Frame3=Frame(sal_Frame3,bg='white',bd=2,relief=RIDGE)
            sal_Frame3.place(x=8,y=44,relwidth=1,height=225)
            self.sample=example_news = """
        - Announcement: Employee of the Month for January is John Doe.
        - Reminder: Don't forget to submit your timesheets by Friday.
        - Important: The office will be closed on Monday for maintenance.
        """


            scroll_y=Scrollbar(sal_Frame3,orient=VERTICAL)
            scroll_y.pack(fill=Y,side=RIGHT)

            self.txt_salary_receipt=Text(sal_Frame3,font=("times new roman",12),bg='lightyellow',yscrollcommand=scroll_y.set)
            self.txt_salary_receipt.pack(fill=BOTH,expand=1)
            scroll_y.config(command=self.txt_salary_receipt.yview)
            self.txt_salary_receipt.insert(END,self.sample)
            try:
                con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
                cur=con.cursor()
                cur.execute("select * from epms_salary where name=%s",(self.username))
                rows=cur.fetchone()
                print("empst")
                print(rows)
                self.var_emp_code2.set(rows[0])
                self.var_designation2.set(rows[1])
                self.var_name2.set(rows[2])
                self.var_age2.set(rows[3])
                self.var_gender2.set(rows[4])
                self.var_email2.set(rows[5])
                self.var_hr_location2.set(rows[6])
                self.var_dob2.set(rows[7])
                self.var_doj2.set(rows[8])
                self.var_experience2.set(rows[9])
                self.var_contact_no2.set(rows[10])
                self.var_proof_id2.set(rows[11])
                self.var_status2.set(rows[12])
                self.txt_address.insert(END,rows[13])
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')








#========all function start here=======
    def search(self):
        try:
            con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
            cur=con.cursor()
            cur.execute("select * from epms_salary where e_id=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            # print(rows)
            if row==None:
               messagebox.showerror("Error","Invalid Employee Id ,please try with another employee ID",parent=self.root)
            else:
                print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact_no.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[13])

                self.var_salary.set(row[14])
                self.var_absent.set(row[15])
                self.var_medical.set(row[16])
                self.var_pf.set(row[17])
                self.var_convence.set(row[18])
                self.var_net_salary.set(row[19])
                file_=open('salary_receipt/'+str(row[20]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert(END,i)
                file_.close()
                #self.btn_Save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')



        except Exception as ex:
              messagebox.showerror("Error",f'Error due to: {str(ex)}')



    def clear(self):
        self.btn_Save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof_id.set('')
        self.var_contact_no.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)
        self.var_salary.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_salary.set('')
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.sample)


    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee Id must be required")
        else:
            try:
                con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
                cur=con.cursor()
                cur.execute("select * from epms_salary where E_ID=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
            # print(rows)
                if row==None:
                   messagebox.showerror("Error","Invalid Employee Id ,please try with another employee ID",parent=self.root)
                else:
                   op=messagebox.askyesno("Confirm","Do you really want to delete?")
                print(op)
                if op==True:
                    cur.execute("delete from epms_salary where E_ID=%s",(self.var_emp_code.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                    self.clear()
            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to: {str(ex)}')



    def add(self):
        if self.var_emp_code.get()==''or self.var_net_salary.get()==''or self.var_name.get()=='':
            messagebox.showerror("Error","Employee Details are Required")
        else:
            try:
                con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
                cur=con.cursor()
                cur.execute("select * from epms_salary where E_ID=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
            # print(rows)
                if row!=None:
                   messagebox.showerror("Error","This Employee is already Available in record ,try again with ID",parent=self.root)
                else:
                    cur.execute("insert into epms_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact_no.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+".txt"


                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully")

            except Exception as ex:
              messagebox.showerror("Error",f'Error due to: {str(ex)}')


    def update(self):
        if self.var_emp_code.get()==''or self.var_net_salary.get()==''or self.var_name.get()=='':
            messagebox.showerror("Error","Employee Details are Required")
        else:
            try:
                con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
                cur=con.cursor()
                cur.execute("select * from epms_salary where E_ID=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
            # print(rows)
                if row==None:
                   messagebox.showerror("Error","This Employee Id is invalid,try again with valid Employee ID",parent=self.root)
                else:
                    cur.execute("UPDATE `epms_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`basic_salary`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_ salary`=%s,`salary_receipt`=%s WHERE E_ID=%s",
                    (

                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact_no.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp_code.get()+".txt",
                        self.var_emp_code.get()


                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_receipt/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record updated Successfully")

            except Exception as ex:
              messagebox.showerror("Error",f'Error due to: {str(ex)}')



    def calculate(self):
        if  self.var_salary.get()=='' or self.var_absent.get()=='' or self.var_medical=='' or self.var_pf.get()=='' or self.var_convence.get()=='' or self.txt_address.get('1.0',END)=='':
           messagebox.showerror('Error','All fields are required')
        else:
            #self.var_net_salary.set("RESULT")
            #35000/31==1752
            #31-10=21*1752
            per_day=int(self.var_salary.get())//30
           # work_day=int(self.var_t_days.get())-int(self.var_absent.get())
           # print ("date_of_join", (self.var_doj))
            date_of_join = datetime.strptime(str(self.var_doj.get()), "%d-%m-%Y")
            now = datetime.now()
            time_interval = now - date_of_join
            num_days = time_interval.days
            work_day=num_days-int(self.var_absent.get())

            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_-deduct+addition
            self.var_net_salary.set(str(round(net_sal,2)))
            new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------
Employee ID\t\t:    {self.var_emp_code.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
------------------------------------------
Total Absent\t\t:  {int(self.var_absent.get())}
Total Present\t\t:{num_days}
Convence\t\t:  Rs.{self.var_convence.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:  Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_salary.get()}
Net Salary\t\t:  Rs.{self.var_net_salary.get()}
------------------------------------------
This is computer generated slip, not
required any signature
'''
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
            cur=con.cursor()
            cur.execute("select * from epms_salary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

    def show(self):
        try:
            con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
            cur=con.cursor()
            cur.execute("select * from epms_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
               self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

    # def showEmployeeDetails(self):
    #     try:
    #         con=pymysql.connect(host='localhost', user='root',password='',db='employee payroll management system')
    #         cur=con.cursor()
    #         cur.execute("select * from epms_salary where name=%f".format(self.txt_user))
    #         rows=cur.fetchall()
    #         #print(rows)
    #         self.employee_tree.delete(*self.employee_tree.get_children())
    #         for row in rows:
    #            self.employee_tree.insert('',END,values=row)
    #         con.close()
    #     except Exception as ex:
    #         messagebox.showerror("Error",f'Error due to: {str(ex)}')




    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System  | by Anshika")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee's Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('E_ID', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'basic_salary', 'absent_days', 'medical', 'pf', 'convence', 'net_ salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('E_ID',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='HR LOC.')
        self.employee_tree.heading('doj',text='Doj')
        self.employee_tree.heading('dob',text='Dob')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('absent_days',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_ salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('E_ID',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_ salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()




        self.root2.mainloop()

    def Print_data(self):
    # Create a temporary text file
     with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".txt") as file_:
        file_name = file_.name
        file_.write(self.txt_salary_receipt.get('1.0', 'end-1c'))

    # Open the file with the default associated application
     os.startfile(file_name, 'Print')


if __name__ == "__main__":
        root=Tk()
        obj=Login(root)
        root.mainloop()
