import mysql.connector as mysql
from mysql.connector import Error
from config import db_config
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

directory = "PROJECT_HOSPITAL/"

def create_connection(db_host, db_user, db_passwd, db_name = None):
    connection_db = None
    try:
        connection_db = mysql.connect(
            host = db_host,
            user = db_user,
            passwd = db_passwd,
            database= db_name
        )
        print("successful connection")
    except Error as bd_connection_error:
        print("Error with connetion to db", bd_connection_error)
    return connection_db
    
def create_db_if_not_exists():
    conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'])
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS HOSPITAL")
    cursor.close()
    conn.close()
    conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')

def create_patient_registration_table_ine():
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        create_registration_table_query = '''
        CREATE TABLE IF NOT EXISTS patients (
        login VARCHAR(255),
        password TEXT,
        name TEXT,
        surname TEXT,
        adress TEXT,
        age INT,
        email TEXT,
        phone_number TEXT,
        diagnosis TEXT,
        allergy TEXT,
        PRIMARY KEY (login)
        )'''
        cursor.execute(create_registration_table_query)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def create_doctor_registration_table_ine():
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        create_registration_table_query_d = '''
        CREATE TABLE IF NOT EXISTS doctors (
        login VARCHAR(255),
        password TEXT,
        name TEXT,
        surname TEXT,
        email TEXT,
        phone_number TEXT,
        appointments_time TEXT,
        salary TEXT,
        profile TEXT,
        surgery_time TEXT,
        PRIMARY KEY (login)
        )'''
        cursor.execute(create_registration_table_query_d)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def create_appointment_table_ine():
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        create_appointment_table_query = '''
        CREATE TABLE IF NOT EXISTS appointments (
        login VARCHAR(255),
        name TEXT,
        surname TEXT,
        doctor TEXT,
        appointment_date TEXT,
        appointment_time TEXT,
        PRIMARY KEY (login)
        )'''
        cursor.execute(create_appointment_table_query)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def create_diagnosis_table_ine():
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        create_diagnosis_table_query = '''
        CREATE TABLE IF NOT EXISTS diagnosis (
        login VARCHAR(255),
        name TEXT,
        surname TEXT,
        doctor TEXT,
        diagnosis TEXT,
        PRIMARY KEY (login)
        )'''
        cursor.execute(create_diagnosis_table_query)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def create_surgeries_table_ine():
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        create_surgeries_table_query = '''
        CREATE TABLE IF NOT EXISTS surgeries (
        login VARCHAR(255),
        name TEXT,
        surname TEXT,
        surgery TEXT,
        PRIMARY KEY (login)
        )'''
        cursor.execute(create_surgeries_table_query)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_data_for_appointment():
    global data_appointment_list
    data_appointment_list = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_appointments_query = '''
        SELECT * FROM HOSPITAL.APPOINTMENTS;
        '''
        cursor.execute(select_appointments_query)
        result = cursor.fetchall()
        for data in result:
            data_appointment_list.append(data)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_data_patients():
    global data_patients_list
    data_patients_list = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_patients_query = '''
        SELECT * FROM HOSPITAL.PATIENTS;
        '''
        cursor.execute(select_patients_query)
        result = cursor.fetchall()
        for data in result:
            data_patients_list.append(data)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_data_doctors():
    global data_doctors_list
    data_doctors_list = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_doctors_query = '''
        SELECT * FROM HOSPITAL.DOCTORS;
        '''
        cursor.execute(select_doctors_query)
        result = cursor.fetchall()
        for data in result:
            data_doctors_list.append(data)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_login_passwd():
    global login_passwd_list
    login_passwd_list = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_login_passwd_query = '''
        SELECT login, password FROM HOSPITAL.PATIENTS;
        '''
        cursor.execute(select_login_passwd_query)
        result = cursor.fetchall()
        for login_passwd in result:
            login_passwd_list.append(login_passwd)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_login_passwd_d():
    global login_passwd_list_d
    login_passwd_list_d = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_login_passwd_query = '''
        SELECT login, password FROM HOSPITAL.DOCTORS;
        '''
        cursor.execute(select_login_passwd_query)
        result = cursor.fetchall()
        for login_passwd in result:
            login_passwd_list_d.append(login_passwd)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_diagnosis():
    global Diagnosis
    Diagnosis = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_diagnosis_query = '''
        SELECT * FROM HOSPITAL.DIAGNOSIS;
        '''
        cursor.execute(select_diagnosis_query)
        result = cursor.fetchall()
        for diag in result:
            Diagnosis.append(diag)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def select_surgeries():
    global Surgeries
    Surgeries = []
    try:
        conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
        cursor = conn.cursor()
        select_Surgeries_query = '''
        SELECT * FROM HOSPITAL.SURGERIES;
        '''
        cursor.execute(select_Surgeries_query)
        result = cursor.fetchall()
        for surg in result:
            Surgeries.append(surg)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

create_db_if_not_exists()
create_patient_registration_table_ine()
create_doctor_registration_table_ine()
create_appointment_table_ine()
create_diagnosis_table_ine()
create_surgeries_table_ine()

class Registration_patient:
    def create_w(self):
        self.reg_window = Tk()
        self.reg_window.resizable(False,False)
        self.reg_window.geometry('600x600+300+100')
        self.reg_window['background']='#8FBC8F'
        self.labels = [Label(self.reg_window, text = 'Create Login', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Create Password', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Name', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Surname', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Adress', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Age', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Email', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Phone number', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Diagnosis', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Allergy', bg = '#8FBC8F')]
        yy = 200
        for label in self.labels:
            label.place(x = 200, y = yy)
            yy += 30
        self.E1 = Entry(self.reg_window)
        self.E2 = Entry(self.reg_window)
        self.E3 = Entry(self.reg_window)
        self.E4 = Entry(self.reg_window)
        self.E5 = Entry(self.reg_window)
        self.E6 = Entry(self.reg_window)
        self.E7 = Entry(self.reg_window)
        self.E8 = Entry(self.reg_window)
        self.E9 = Entry(self.reg_window)
        self.E10 = Entry(self.reg_window)
        self.entries = [self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9, self.E10]
        yy = 200
        for entry in self.entries:
            entry.place(x = 300, y = yy)
            yy += 30

        
        self.canvas = Canvas(self.reg_window, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.finish_button= PhotoImage(file= directory + "finish.png")
        self.finish_button= self.finish_button.subsample(10,10)
        self.B = Button(self.reg_window, image=self.finish_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B.place(x = 300, y = 500)

        self.back_button= PhotoImage(file= directory + "back.png")
        self.back_button= self.back_button.subsample(10,10)
        self.B1 = Button(self.reg_window, image=self.back_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B1.place(x = 0, y = 500)
        self.back()

    def finish_reg(self):
        self.reg_window.destroy()
        logon.create_w()
        logon.button_to_reg_w()
        logon.button_to_reg_w_d()
        logon.button_to_appointment_w()
        
    def insert_reg_data(self, event):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()
            insert_data = '''
            INSERT INTO PATIENTS (login, password, name, surname, adress, age, email, phone_number, diagnosis, allergy)
            VALUES ('{log}', '{pas}', '{nam}', '{sname}', '{ad}', '{ag}', '{em}', '{pn}', '{diag}', '{aller}');
            '''.format(log = self.E1.get(), pas = self.E2.get(), nam = self.E3.get(), sname = self.E4.get(), ad = self.E5.get(), ag = self.E6.get(), em = self.E7.get(), pn = self.E8.get(), diag = self.E9.get(), aller = self.E10.get())
            cursor.execute(insert_data)
            conn.commit()
            self.finish_reg()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    
    def back_to_w(self, event):
        self.reg_window.destroy()
        logon.create_w()
        logon.button_to_reg_w()
        logon.button_to_reg_w_d()
        logon.button_to_appointment_w()

    def fin_reg_button(self):
        self.B.bind('<Button-1>', self.insert_reg_data)

    def back(self):
            self.B1.bind('<Button-1>', self.back_to_w)

    def mainloop(self):
        self.reg_window.mainloop()

class Registration_doctor:
    def create_w(self):
        self.reg_window = Tk()
        self.reg_window.resizable(False,False)
        self.reg_window.geometry('600x600+300+100')
        self.reg_window['background']='#8FBC8F'
        self.labels = [Label(self.reg_window, text = 'Create Login', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Create Password', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Name', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Surname', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Email', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Phone number', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Appointments time table', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Salary', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Profile', bg = '#8FBC8F'),
        Label(self.reg_window, text = 'Surgery time table', bg = '#8FBC8F')]
        yy = 200
        for label in self.labels:
            label.place(x = 150, y = yy)
            yy += 30
        self.E1 = Entry(self.reg_window)
        self.E2 = Entry(self.reg_window)
        self.E3 = Entry(self.reg_window)
        self.E4 = Entry(self.reg_window)
        self.E5 = Entry(self.reg_window)
        self.E6 = Entry(self.reg_window)
        self.E7 = Entry(self.reg_window)
        self.E8 = Entry(self.reg_window)
        self.E9 = Entry(self.reg_window)
        self.E10 = Entry(self.reg_window)
        self.entries = [self.E1, self.E2, self.E3, self.E4, self.E5, self.E6, self.E7, self.E8, self.E9, self.E10]
        yy = 200
        for entry in self.entries:
            entry.place(x = 300, y = yy)
            yy += 30
        self.canvas = Canvas(self.reg_window, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.finish_button= PhotoImage(file= directory + "finish.png")
        self.finish_button= self.finish_button.subsample(10,10)
        self.B = Button(self.reg_window, image=self.finish_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B.place(x = 300, y = 500)

        self.back_button= PhotoImage(file= directory + "back.png")
        self.back_button= self.back_button.subsample(10,10)
        self.B1 = Button(self.reg_window, image=self.back_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B1.place(x = 0, y = 500)
        self.back()

    def finish_reg(self):
        self.reg_window.destroy()
        logon.create_w()
        logon.button_to_reg_w()
        logon.button_to_reg_w_d()
        logon.button_to_appointment_w()
        
    def insert_reg_data(self, event):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()
            insert_data = '''
            INSERT INTO DOCTORS (login, password, name, surname, email, phone_number, appointments_time, salary, profile, surgery_time)
            VALUES ('{log}', '{pas}', '{nam}', '{sname}', '{em}', '{pn}', '{at}', '{sal}', '{prof}', '{st}');
            '''.format(log = self.E1.get(), pas = self.E2.get(), nam = self.E3.get(), sname = self.E4.get(), em = self.E5.get(), pn = self.E6.get(), at = self.E7.get(), sal = self.E8.get(), prof = self.E9.get(), st = self.E10.get())
            cursor.execute(insert_data)
            conn.commit()
            self.finish_reg()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def back_to_w(self, event):
        self.reg_window.destroy()
        logon.create_w()
        logon.button_to_reg_w()
        logon.button_to_reg_w_d()
        logon.button_to_appointment_w()
    
    def fin_reg_button(self):
        self.B.bind('<Button-1>', self.insert_reg_data)

    def back(self):
        self.B1.bind('<Button-1>', self.back_to_w)

    def mainloop(self):
        self.reg_window.mainloop()

class Logon:
    def create_w(self):
        self.logon_window = Tk()
        self.logon_window.resizable(False,False)
        self.logon_window.geometry('600x600+300+100')
        self.logon_window['background']='#8FBC8F'

        image1 = Image.open(directory + "title.png")
        test = ImageTk.PhotoImage(image1)

        label1 = Label(image=test, bg = '#8FBC8F')
        label1.image = test
        label1.place(x = 10, y = 10)

        self.L1 = Label(self.logon_window, text = 'Login', bg = '#8FBC8F')
        self.L2 = Label(self.logon_window, text = 'Password', bg = '#8FBC8F')
        self.L1.place(x = 200, y = 200)
        self.L2.place(x = 200, y = 250)
        self.E1 = Entry(self.logon_window)
        self.E2 = Entry(self.logon_window)
        self.E1.place(x = 270, y = 200)
        self.E2.place(x = 270, y = 250)

        self.canvas = Canvas(self.logon_window, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.enter_button= PhotoImage(file= directory + "enter.png")
        self.enter_button= self.enter_button.subsample(10,10)
        self.B1 = Button(self.logon_window, image=self.enter_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B1.place(x = 220, y = 300)

        self.regp_button= PhotoImage(file= directory + "patient.png")
        self.regp_button= self.regp_button.subsample(10,10)
        self.B2 = Button(self.logon_window, image=self.regp_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B2.place(x = 400, y = 500)
        
        self.regd_button= PhotoImage(file= directory + "doctor.png")
        self.regd_button= self.regd_button.subsample(10,10)
        self.B3 = Button(self.logon_window, image=self.regd_button, highlightthickness=0, bd=0, bg = '#8FBC8F')
        self.B3.place(x = 0, y = 500)
        select_login_passwd()
        select_login_passwd_d()
        select_data_patients()
        select_data_doctors()
        select_data_for_appointment()
        select_diagnosis()
        select_surgeries()

    def open_appointment_w(self):
        self.logon_window.destroy()
        appointment_p.create_w()  
    def open_appointment_w_d(self):
        self.logon_window.destroy()
        appointment_d.create_w()
        appointment_d.button_to_diagnosis_d()
        appointment_d.button_to_surgeries_d()

    def not_success_enter(self):
        self.L3 = Label(self.logon_window, text = 'wrong login or password')
        self.L3.pack(side = LEFT)

    def check_log_pass(self, event):
        self.inner_log_name_sname_list = []
        for data in data_patients_list:
            if data[0] == self.E1.get():
                self.inner_log_name_sname_list = [data[0], data[2], data[3]]

        for data in login_passwd_list:
            if data[0] == self.E1.get() and data[1] == self.E2.get():
                self.open_appointment_w()
            else:
                for data in login_passwd_list_d:
                    if data[0] == self.E1.get() and data[1] == self.E2.get():
                        self.open_appointment_w_d()
                    else:
                        self.not_success_enter()

    def open_reg_w(self, event):
        self.logon_window.destroy()
        reg.create_w()
        reg.fin_reg_button()
    def open_reg_w_d(self, event):
        self.logon_window.destroy()
        reg_d.create_w()
        reg_d.fin_reg_button()  

    def button_to_appointment_w(self):
        self.B1.bind('<Button-1>', self.check_log_pass)
    def button_to_reg_w(self):
        self.B2.bind('<Button-1>', self.open_reg_w)    
    def button_to_reg_w_d(self):
        self.B3.bind('<Button-1>', self.open_reg_w_d)

    def mainloop(self):
        self.logon_window.mainloop()

class Appointment_d:
    def create_w(self):
        self.appointment_window_d = Tk()
        self.appointment_window_d.resizable(False,False)
        self.appointment_window_d.geometry('600x600+300+100')
        self.show_appointments()
        self.appointment_window_d['background']='#87CEFA'

    def show_appointments(self):
        L = Label(self.appointment_window_d, text = 'Appointments', font = ('Cambria', 20, 'bold'), bg = '#87CEFA')
        L.pack(padx = 1, pady = 1)
        labels = []
        for i in range(len(data_appointment_list)):
            labels.append((data_appointment_list[i][1], data_appointment_list[i][2], data_appointment_list[i][3], data_appointment_list[i][4], data_appointment_list[i][5]))

        self.canvas = Canvas(self.appointment_window_d, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.diag_button= PhotoImage(file= directory + "diag.png")
        self.diag_button= self.diag_button.subsample(10,10)
        self.B1 = Button(self.appointment_window_d, image=self.diag_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B1.place(x = 0, y = 500)
        self.surg_button= PhotoImage(file= directory + "sur.png")
        self.surg_button= self.surg_button.subsample(10,10)
        self.B2 = Button(self.appointment_window_d, image=self.surg_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B2.place(x = 400, y = 500)

        frame = Frame(self.appointment_window_d)
        frame.pack()
        appointment_table = ttk.Treeview(frame)
        appointment_table['columns'] = ("Patient's name", "Patient's surname", 'Doctor', 'Date', 'Time')

        appointment_table.column("#0", width=0,  stretch=NO)
        appointment_table.column("Patient's name",anchor=CENTER, width=90)
        appointment_table.column("Patient's surname",anchor=CENTER,width=105)
        appointment_table.column("Doctor",anchor=CENTER,width=220)
        appointment_table.column("Date",anchor=CENTER,width=70)
        appointment_table.column("Time",anchor=CENTER,width=50)

        appointment_table.heading("#0",text="",anchor=CENTER)
        appointment_table.heading("Patient's name",text="Patient's name",anchor=CENTER)
        appointment_table.heading("Patient's surname",text="Patient's surname",anchor=CENTER)
        appointment_table.heading("Doctor",text="Doctor",anchor=CENTER)
        appointment_table.heading("Date",text="Date",anchor=CENTER)
        appointment_table.heading("Time",text="Time",anchor=CENTER)

        for i in range(len(labels)):
            appointment_table.insert(parent='',index='end',iid=i,text='',
            values=(labels[i][0], labels[i][1], labels[i][2], labels[i][3], labels[i][4]))
        appointment_table.pack()

    def open_diagnosis_w_d(self, event):
        self.appointment_window_d.destroy()
        diagnosis_d.create_w()
        diagnosis_d.button_to_surgeries_d()
        
    def open_surgeries_w_d(self, event):
        self.appointment_window_d.destroy()
        surgery_d.create_w()

    def button_to_diagnosis_d(self):
        self.B1.bind('<Button-1>', self.open_diagnosis_w_d)
    
    def button_to_surgeries_d(self):
        self.B2.bind('<Button-1>', self.open_surgeries_w_d)
        
class Appointment_p:
    def create_w(self):
        self.appointment_window = Tk()
        self.appointment_window.resizable(False,False)
        self.appointment_window.geometry('600x600+300+100')
        self.appointment_window['background'] = '#FFE4E1'
        self.canvas = Canvas(self.appointment_window, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.frame = Frame(self.appointment_window)
        self.frame.pack()
        self.vlist = ["01","02","03","04","05","06","07","08","09","10","11","12"]

        self.vlist2 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18",'19',"20","21","22","23","24","25","26",'27',"28","29","30","31"]

        self.vlist3 = ["2021","2022","2023","2024","2025"]
        
        self.vlist4 = []
        for doctor in data_doctors_list:
            self.vlist4.append(doctor[8] +" "+ doctor[2] +" "+ doctor[3])
        self.vlist4.sort()

        self.vlist5 = ["00", "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18",'19',"20","21","22","23"]

        self.vlist6 = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18",'19',"20","21","22","23","24","25","26",'27',"28","29","30","31",
                "32",'33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']

        self.vlist7 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18",'19',"20","21","22","23","24","25","26",'27',"28"]

        self.Combo4 = ttk.Combobox(self.frame, values = self.vlist4, state='readonly')
        self.Combo4.set("Pick a doctor")
        self.Combo4.pack(padx = 5, pady = 5)

        self.Combo = ttk.Combobox(self.frame, values = self.vlist, state='readonly')
        self.Combo.set("Pick a month")
        self.Combo.pack(padx = 5, pady = 5)

        self.Combo2 = ttk.Combobox(self.frame, values = self.vlist2, state='readonly')
        self.Combo2.set("Pick a day")
        self.Combo2.pack(padx = 5, pady = 5)

        self.Combo3 = ttk.Combobox(self.frame, values = self.vlist3, state='readonly')
        self.Combo3.set("Pick a year")
        self.Combo3.pack(padx = 5, pady = 5)

        self.Combo5 = ttk.Combobox(self.frame, values = self.vlist5, state='readonly')
        self.Combo5.set("Pick a hour")
        self.Combo5.pack(padx = 5, pady = 5)

        self.Combo6 = ttk.Combobox(self.frame, values = self.vlist6, state='readonly')
        self.Combo6.set("Pick a minute")
        self.Combo6.pack(padx = 5, pady = 5)

        self.diag_button= PhotoImage(file= directory + "diag.png")
        self.diag_button= self.diag_button.subsample(10,10)
        self.B1 = Button(self.appointment_window, image=self.diag_button, highlightthickness=0, bd=0, bg = '#FFE4E1')
        self.B1.place(x = 400, y = 500)
        self.sur_button= PhotoImage(file= directory + "sur.png")
        self.sur_button= self.sur_button.subsample(10,10)
        self.B2 = Button(self.appointment_window, image=self.sur_button, highlightthickness=0, bd=0, bg = '#FFE4E1')
        self.B2.place(x = 0, y = 500)

        self.retrieve_appointment()
        self.cancel_appointment()
        self.button_to_diag_w()
        self.button_to_surg_w()

    def insert_data_appointment(self):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()
            insert_data = '''
            INSERT INTO APPOINTMENTS (login, name, surname, doctor, appointment_date, appointment_time)
            VALUES ('{log}', '{nam}', '{sname}', '{doc}', '{app_dat}', '{app_tim}');
            '''.format(log = logon.inner_log_name_sname_list[0], nam = logon.inner_log_name_sname_list[1], sname = logon.inner_log_name_sname_list[2], doc = str(self.Combo4.get()), app_dat = (str(self.Combo.get()) +"."+ str(self.Combo2.get()) +"."+ str(self.Combo3.get())), app_tim = (str(self.Combo5.get()) +":"+ str(self.Combo6.get())))

            cursor.execute(insert_data)
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def delete_data_appointment(self):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()
            insert_data = '''
            DELETE FROM APPOINTMENTS
            WHERE login = "{log}";
            '''.format(log = logon.inner_log_name_sname_list[0])

            cursor.execute(insert_data)
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def retrieve(self):
        if self.Combo.get() == "04":
            self.Combo2["values"] = (self.vlist7)
        else:
            self.Combo2["values"] = (self.vlist2)         
        self.insert_data_appointment()

    def retrieve_appointment(self):
        self.sub_button= PhotoImage(file= directory + "sub.png")
        self.sub_button= self.sub_button.subsample(10,10)
        self.Button = Button(self.appointment_window, image=self.sub_button, highlightthickness=0, bd=0, bg = '#FFE4E1', command = self.retrieve)
        self.Button.pack(padx = 5, pady = 5)
    
    def cancel_appointment(self):
        self.cancel_button= PhotoImage(file= directory + "cancel.png")
        self.cancel_button= self.cancel_button.subsample(15,15)
        self.Button1 = Button(self.appointment_window, image=self.cancel_button, highlightthickness=0, bd=0, bg = '#FFE4E1', command = self.delete_data_appointment)
        self.Button1.pack(padx = 3, pady = 3)

    def open_diag_w_p(self, event):
        self.appointment_window.destroy()
        diagnosis_p.create_w()
    
    def open_surg_w_p(self, event):
        self.appointment_window.destroy()
        surgeries_p.create_w()

    def button_to_diag_w(self):
        self.B1.bind('<Button-1>', self.open_diag_w_p)

    def button_to_surg_w(self):
        self.B2.bind('<Button-1>', self.open_surg_w_p)    

class Diagnosis_d:
    def create_w(self):
        self.diagnosis_w_d = Tk()
        self.diagnosis_w_d.resizable(False,False)
        self.diagnosis_w_d.geometry('600x600+300+100')
        self.diagnosis_w_d['background']='#87CEFA'
        L = Label(self.diagnosis_w_d, text = 'Diagnosis', font = ('Cambria', 20, 'bold'), bg = '#87CEFA')
        L.pack(padx = 1, pady = 1)
        
        self.canvas = Canvas(self.diagnosis_w_d, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.enter_button= PhotoImage(file= directory + "save.png")
        self.enter_button= self.enter_button.subsample(10,10)
        self.B = Button(self.diagnosis_w_d, image=self.enter_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B.place(x = 250, y = 500)
        self.surg_button= PhotoImage(file= directory + "back.png")
        self.surg_button= self.surg_button.subsample(10,10)
        self.B1 = Button(self.diagnosis_w_d, image=self.surg_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B1.place(x = 0, y = 500)
        self.back()
        
        yy = 200
        for i in range(len(data_appointment_list)):
            L = Label(self.diagnosis_w_d, text = data_appointment_list[i][1] +" "+ data_appointment_list[i][2] +"      "+ data_appointment_list[i][3], bg = '#87CEFA')
            L.place(x = 100, y = yy)
            yy += 30

        yy = 200
        self.entries = []
        for i in range(len(data_appointment_list)):
            self.entries.append(Entry(self.diagnosis_w_d))
            self.entries[i].place(x = 400, y = yy)
            yy += 30

    def take_entry(self, i):
        return self.entries[i].get()
    
    def insert_diagnosis_data(self, event):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()

            for i in range(len(data_appointment_list)):
                insert_data = '''
                INSERT INTO DIAGNOSIS (login, name, surname, doctor, diagnosis)
                VALUES ('{log}', '{nam}', '{sname}', '{doc}', '{diag}')
                ON DUPLICATE KEY UPDATE diagnosis = "{diag}"'''.format(log = data_appointment_list[i][0],
                nam = data_appointment_list[i][1],
                sname = data_appointment_list[i][2],
                doc = data_appointment_list[i][3],
                diag = self.take_entry(i)
                )
                cursor.execute(insert_data)

            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def back_to_w(self, event):
        self.diagnosis_w_d.destroy()
        appointment_d.create_w()
        appointment_d.button_to_diagnosis_d()
        appointment_d.button_to_surgeries_d()
    def back(self):
        self.B1.bind('<Button-1>', self.back_to_w)   
    
    def button_to_surgeries_d(self):
        self.B.bind('<Button-1>', self.insert_diagnosis_data)

class Surgery_d:
    def create_w(self):
        self.surgery_w_d = Tk()
        self.surgery_w_d.resizable(False,False)
        self.surgery_w_d.geometry('600x600+300+100')
        self.surgery_w_d['background']='#87CEFA'
        L = Label(self.surgery_w_d, text = 'Surgeries', font = ('Cambria', 20, 'bold'), bg =  '#87CEFA')
        L.pack(padx = 1, pady = 1)
        self.canvas = Canvas(self.surgery_w_d, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.save_button= PhotoImage(file= directory + "save.png")
        self.save_button= self.save_button.subsample(10,10)
        self.B = Button(self.surgery_w_d, image=self.save_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B.place(x = 250, y = 500)
        self.button_to_surgeries_d()
        self.back_button= PhotoImage(file= directory + "back.png")
        self.back_button= self.back_button.subsample(10,10)
        self.B1 = Button(self.surgery_w_d, image=self.back_button, highlightthickness=0, bd=0, bg = '#87CEFA')
        self.B1.place(x = 0, y = 500)
        self.back()

        yy = 200
        for i in range(len(data_appointment_list)):
            L = Label(self.surgery_w_d, text = data_appointment_list[i][1] +" "+ data_appointment_list[i][2] +"      "+ data_appointment_list[i][3], bg = '#87CEFA') 
            L.place(x = 100, y = yy)
            yy += 30

        yy = 200
        self.surgeries = []
        for i in range(len(data_appointment_list)):
            n = StringVar()
            self.surgery_choose = ttk.Combobox(self.surgery_w_d, width = 15, textvariable = n)
            self.surgery_choose['values'] = (' on Leg', 
                                    ' on Arm',
                                    ' on Hand',
                                    ' on Brain',
                                    ' on Chest',
                                    ' on Back')
            self.surgery_choose.place(x = 400, y = yy)
            self.surgeries.append(self.surgery_choose)
            yy += 30
    
    def get_surg(self, i):
        return self.surgeries[i].get()

    def insert_surgery_data(self, event):
        try:
            conn = create_connection(db_config['mysql']['host'], db_config['mysql']['user'], db_config['mysql']['passwd'], 'Hospital')
            cursor = conn.cursor()

            for i in range(len(data_appointment_list)):
                insert_data = '''
                INSERT INTO SURGERIES (login, name, surname, surgery)
                VALUES ('{log}', '{nam}', '{sname}', '{surg}')
                ON DUPLICATE KEY UPDATE surgery = "{surg}"'''.format(log = data_appointment_list[i][0],
                nam = data_appointment_list[i][1],
                sname = data_appointment_list[i][2],
                surg = self.get_surg(i)
                )
                cursor.execute(insert_data)
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def back_to_w(self, event):
        self.surgery_w_d.destroy()
        appointment_d.create_w()
        appointment_d.button_to_diagnosis_d()
        appointment_d.button_to_surgeries_d()
        
    
    def back(self):
        self.B1.bind('<Button-1>', self.back_to_w)
    
    def button_to_surgeries_d(self):
        self.B.bind('<Button-1>', self.insert_surgery_data)

class Diagnosis_p:
    def create_w(self):
        self.surgery_w_p = Tk()
        self.surgery_w_p.resizable(False,False)
        self.surgery_w_p.geometry('600x600+300+100')
        self.surgery_w_p['background'] = '#FFE4E1'
        L = Label(self.surgery_w_p, text = 'Diagnosis', font = ('Cambria', 20, 'bold'), bg = '#FFE4E1')
        L.pack(padx = 1, pady = 1)
        self.canvas = Canvas(self.surgery_w_p, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.back_button= PhotoImage(file= directory + "back.png")
        self.back_button= self.back_button.subsample(10,10)
        self.B1 = Button(self.surgery_w_p, image=self.back_button, highlightthickness=0, bd=0, bg = '#FFE4E1')
        self.B1.place(x = 0, y = 500)
        self.back()
        labels = []
        for i in range(len(Diagnosis)):
            labels.append((Diagnosis[i][1], Diagnosis[i][2], Diagnosis[i][4]))

        frame = Frame(self.surgery_w_p)
        frame.pack()
        surgeries_table = ttk.Treeview(frame)
        surgeries_table['columns'] = ("Patient's name", "Patient's surname", 'Diagnosis')

        surgeries_table.column("#0", width=0,  stretch=NO)
        surgeries_table.column("Patient's name",anchor=CENTER, width=90)
        surgeries_table.column("Patient's surname",anchor=CENTER,width=105)
        surgeries_table.column("Diagnosis",anchor=CENTER,width=220)

        surgeries_table.heading("#0",text="",anchor=CENTER)
        surgeries_table.heading("Patient's name",text="Patient's name",anchor=CENTER)
        surgeries_table.heading("Patient's surname",text="Patient's surname",anchor=CENTER)
        surgeries_table.heading("Diagnosis",text="Diagnosis",anchor=CENTER)

        for i in range(len(labels)):
            surgeries_table.insert(parent='',index='end',iid=i,text='',
            values=(labels[i][0], labels[i][1], labels[i][2]))
        surgeries_table.pack()
    
    def back_to_w(self, event):
        self.surgery_w_p.destroy()
        appointment_p.create_w()

    def back(self):
        self.B1.bind('<Button-1>', self.back_to_w)

class Surgeries_p:
    def create_w(self):
        self.surgery_w_p = Tk()
        self.surgery_w_p.resizable(False,False)
        self.surgery_w_p.geometry('600x600+300+100')
        self.surgery_w_p['background'] = '#FFE4E1'
        L = Label(self.surgery_w_p, text = 'Surgeries', font = ('Cambria', 20, 'bold'), bg = '#FFE4E1')
        L.pack(padx = 1, pady = 1)
        self.canvas = Canvas(self.surgery_w_p, width=2, height=2, highlightthickness=0)
        self.canvas.pack()
        self.back_button= PhotoImage(file= directory + "back.png")
        self.back_button= self.back_button.subsample(10,10)
        self.B1 = Button(self.surgery_w_p, image=self.back_button, highlightthickness=0, bd=0, bg = '#FFE4E1')
        self.B1.place(x = 0, y = 500)
        self.back()
        labels = []
        for i in range(len(Surgeries)):
            labels.append((Surgeries[i][1], Surgeries[i][2], Surgeries[i][3]))

        frame = Frame(self.surgery_w_p)
        frame.pack()
        surgeries_table = ttk.Treeview(frame)
        surgeries_table['columns'] = ("Patient's name", "Patient's surname", 'Surgeries')

        surgeries_table.column("#0", width=0,  stretch=NO)
        surgeries_table.column("Patient's name",anchor=CENTER, width=90)
        surgeries_table.column("Patient's surname",anchor=CENTER,width=105)
        surgeries_table.column("Surgeries",anchor=CENTER,width=220)

        surgeries_table.heading("#0",text="",anchor=CENTER)
        surgeries_table.heading("Patient's name",text="Patient's name",anchor=CENTER)
        surgeries_table.heading("Patient's surname",text="Patient's surname",anchor=CENTER)
        surgeries_table.heading("Surgeries",text="Surgeries",anchor=CENTER)

        for i in range(len(labels)):
            surgeries_table.insert(parent='',index='end',iid=i,text='',
            values=(labels[i][0], labels[i][1], labels[i][2]))
        surgeries_table.pack()

    def back_to_w(self, event):
        self.surgery_w_p.destroy()
        appointment_p.create_w() 

    def back(self):
        self.B1.bind('<Button-1>', self.back_to_w)
    
logon = Logon()
reg = Registration_patient()
appointment_p = Appointment_p()
appointment_d = Appointment_d()
diagnosis_d = Diagnosis_d()
surgery_d = Surgery_d()
diagnosis_p = Diagnosis_p()
surgeries_p = Surgeries_p()
reg_d = Registration_doctor()
logon.create_w()
logon.button_to_reg_w()
logon.button_to_reg_w_d()
logon.button_to_appointment_w()
logon.mainloop()