from tkinter import*


class fitness:

    def __init__(self, root):

        self.f=Frame(root, height=640, width=800, bg='pink', cursor='',borderwidth = '1')
        self.f.propagate(0)
        self.f.pack()#for frame
        
        self.m=Message(self.f, text='Fitness',width=200,font=('Calbri', 20, 'bold'), fg='white', bg='dark blue')
        
        self.m.pack(side=TOP)#for message
            
        self.l1=Label(text='Name:',font=('Calbri', 14,'bold'), fg='dark blue' ,bg='sky blue')
        self.l2=Label(text='Age:',font=('Calbri', 14,'bold'), fg='dark blue', bg='sky blue')
        
        self.e1=Entry(self.f, width=14, fg='black', bg='yellow',font=('Arial', 14,'italic'))
        self.e2=Entry(self.f, width=14, fg='black', bg='yellow',font=('Arial', 14,'italic'))
        
        self.l1.place(x=50,y=100) #Name
        self.l2.place(x=510,y=100) #Age
        self.e1.place(x=120,y=100) #Name_entry
        self.e2.place(x=570,y=100) #Age_entry
        
        self.l3=Label(text='Gender:',font=('Calbri', 14,'bold'), fg='dark blue', bg='sky blue')
        
        self.var = IntVar()
        
        self.r1=Radiobutton(self.f, font=('Calbri', 13),text='Male',cursor='hand2', variable=self.var, value=1)
        self.r2=Radiobutton(self.f, font=('Calbri', 13),text='Female',cursor='hand2', variable=self.var, value=2)
        
        self.l3.place(x=50,y=180) #Gender
        self.r1.place(x=230,y=180) #Male
        self.r2.place(x=430,y=180) #Female
        
        
        self.lb1=Label(self.f, text='Weight(kg):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb2=Label(self.f, text='Height(m):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb3=Label(self.f, text='BP Low:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb4=Label(self.f, text='BP High:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb5=Label(self.f, text='Pulse Rate(b/m):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb6=Label(self.f, text='RBC Count(cells/mcL):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb7=Label(self.f, text='WBC Count(cells/mcL):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb8=Label(self.f, text='Platelets:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb9=Label(self.f, text='HB(g/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb10=Label(self.f, text='Uric Acid(mg/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.lb11=Label(self.f, text='Cholesterol(mg/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")

        self.lb1.place(x=50,y=280) #weight
        self.lb2.place(x=50,y=308) #height
        self.lb3.place(x=50,y=336) #BP low
        self.lb4.place(x=50,y=359) #BP high
        self.lb5.place(x=50,y=387) #pulse rate
        self.lb6.place(x=50,y=415) #rbc count
        self.lb7.place(x=50,y=443) #wbc count
        self.lb8.place(x=50,y=471) #platelets
        self.lb9.place(x=50,y=499) #HB
        self.lb10.place(x=50,y=527) #Uric acid
        self.lb11.place(x=50,y=554) #cholesterol
        
        self.eb1=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb2=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb3=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb4=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb5=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb6=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb7=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb8=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb9=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb10=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        self.eb11=Entry(self.f, width=13, fg='black', bg='white',font=('calbri', 14),borderwidth = 2,relief="ridge")
        
        
        self.eb1.place(x=254,y=280) #entry for weight
        self.eb2.place(x=254,y=308) #entry for height
        self.eb3.place(x=254,y=336) #entry for BP low
        self.eb4.place(x=254,y=359) #entry for BP high
        self.eb5.place(x=254,y=387) #entry for pulse rate
        self.eb6.place(x=254,y=415) #entry for rbc count
        self.eb7.place(x=254,y=443) #entry for wbc count
        self.eb8.place(x=254,y=471) #entry for platelets
        self.eb9.place(x=254,y=499) #entry for HB
        self.eb10.place(x=254,y=527) #entry for Uric acid
        self.eb11.place(x=254,y=554) #entry for cholesterol
        
        self.b1=Button(self.f, text='Generate Report',font=('Calbri', 15, 'bold'), width=15, height=1,bg='dark red', fg='white', activebackground='dark blue',activeforeground='white',relief='raised',borderwidth = 2,cursor='hand2', command=self.buttonclick)
        self.b1.place(x=490,y=520)#, width=20, height=4)
        
    
    
    def buttonclick(self):
        root1=Tk()
        root1.title('Report')
        self.f1=Frame(root1, height=500, width=750, bg='pink',borderwidth = '1')
        self.f1.propagate(0)
        self.f1.pack()#for frame
        
        self.m1=Message(self.f1, text='Report',width=200,font=('Calbri', 20, 'bold'), fg='white', bg='dark blue')
        self.m1.pack(side=TOP)#for message
        
        #name and age for the frame 2
        self.ll1=Label(self.f1,text='Name:',font=('Calbri', 14,'bold'), fg='dark blue' ,bg='sky blue')
        self.ll2=Label(self.f1,text='Age:',font=('Calbri', 14,'bold'), fg='dark blue' ,bg='sky blue')
        self.ll3=Label(self.f1,text='Gender:',font=('Calbri', 14,'bold'), fg='dark blue' ,bg='sky blue')
        
        self.ll1.place(x=70,y=75)
        self.ll2.place(x=310,y=75)
        self.ll3.place(x=490,y=75)
        
        x=self.var.get()
        str0=''
        if x==1:
            str0+= 'Male'

        if x==2:
            str0+= 'Female'
            
        self.ll4=Label(self.f1,text=str0,font=('Calbri', 14,'bold italic'), fg='dark blue' ,bg='yellow') #gender-checkbutton
        self.ll5=Label(self.f1,text=self.e1.get(),font=('Calbri', 15,'bold italic'), fg='dark blue' ,bg='yellow') #name-entry
        self.ll6=Label(self.f1,text=self.e2.get(),font=('Calbri', 14,'bold italic'), fg='dark blue' ,bg='yellow') #age-entry
        self.ll5.place(x=145,y=75)
        self.ll6.place(x=370,y=75)
        self.ll4.place(x=585,y=75)
        
        self.l1=Label(self.f1, text='Parameter', width=18, height=1, font=('calbri', 14,'bold'), fg='white', bg='dark red',borderwidth = 2,relief="ridge")
        self.l2=Label(self.f1, text="Patient's Value", width=12, height=1, font=('calbri', 14,'bold'), fg='white', bg='dark red',borderwidth = 2,relief="ridge")
        self.l3=Label(self.f1, text='Ideal Value', width=12, height=1, font=('calbri', 14,'bold'), fg='white', bg='dark red',borderwidth = 2,relief="ridge")
        self.l4=Label(self.f1, text='Remark', width=12, height=1, font=('calbri', 14,'bold'), fg='white', bg='dark red',borderwidth = 2,relief="ridge")
        
        self.l1.place(x=70,y=140) #for Parameter
        self.l2.place(x=274,y=140) #for Patient's Value
        self.l3.place(x=423,y=140) #for Ideal Value
        self.l4.place(x=565,y=140) #for Remark
        
        self.la1=Label(self.f1, text='BMI:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la2=Label(self.f1, text='BP:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la3=Label(self.f1, text='Pulse Rate(b/m):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la4=Label(self.f1, text='RBC Count(cells/mcL):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la5=Label(self.f1, text='WBC Count(cells/mcL):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la6=Label(self.f1, text='Platelets:', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la7=Label(self.f1, text='HB(g/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la8=Label(self.f1, text='Uric Acid(mg/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        self.la9=Label(self.f1, text='Cholesterol(mg/dl):', width=18, height=1, font=('calbri', 14), fg='black', bg='light grey',borderwidth = 2,relief="ridge")
        
        self.la1.place(x=70,y=168)
        self.la2.place(x=70,y=196)
        self.la3.place(x=70,y=219)
        self.la4.place(x=70,y=247)
        self.la5.place(x=70,y=275)
        self.la6.place(x=70,y=303)
        self.la7.place(x=70,y=331)
        self.la8.place(x=70,y=353)
        self.la9.place(x=70,y=381)
        
        weight=float(self.eb1.get())
        height=float(self.eb2.get())
        BMI=(weight/height**2)
        BPlow=float(self.eb3.get())
        BPhigh=float(self.eb4.get())
        BP=((BPlow+BPhigh)/2)
        Pulserate=float(self.eb5.get())
        RBCcount=float(self.eb6.get())
        WBCcount=float(self.eb7.get())
        Platelets=int(self.eb8.get())
        HB=float(self.eb9.get())
        Uricacid=float(self.eb10.get())
        Cholestrol=float(self.eb11.get())
        
        
        self.lb1=Label(self.f1, text=round(BMI,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb2=Label(self.f1, text=round(BP,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb3=Label(self.f1, text=round(Pulserate,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb4=Label(self.f1, text=round(RBCcount,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb5=Label(self.f1, text=round(WBCcount,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb6=Label(self.f1, text=Platelets, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb7=Label(self.f1, text=round(HB,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb8=Label(self.f1, text=round(Uricacid,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lb9=Label(self.f1, text=round(Cholestrol,3), width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        
        self.lb1.place(x=274,y=168)
        self.lb2.place(x=274,y=196)
        self.lb3.place(x=274,y=219)
        self.lb4.place(x=274,y=247)
        self.lb5.place(x=274,y=275)
        self.lb6.place(x=274,y=303)
        self.lb7.place(x=274,y=331)
        self.lb8.place(x=274,y=353)
        self.lb9.place(x=274,y=381)
        
        
        self.lc1=Label(self.f1, text='24.5', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc2=Label(self.f1, text='100', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc3=Label(self.f1, text='77.5', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc4=Label(self.f1, text='5.4', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc5=Label(self.f1, text='7.75', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc6=Label(self.f1, text='250,000', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc7=Label(self.f1, text='15.5', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc8=Label(self.f1, text='5.2', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.lc9=Label(self.f1, text='162.5', width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        
        self.lc1.place(x=423,y=168)
        self.lc2.place(x=423,y=196)
        self.lc3.place(x=423,y=219)
        self.lc4.place(x=423,y=247)
        self.lc5.place(x=423,y=275)
        self.lc6.place(x=423,y=303)
        self.lc7.place(x=423,y=331)
        self.lc8.place(x=423,y=353)
        self.lc9.place(x=423,y=381)
        
        if(BMI>=28):
            r1='High'
        elif(BMI>=19):
            r1='Medium'
        else:
            r1='Low'
            
        if(BP>=110):
            r2='High'
        elif(BP>=85):
            r2='Medium'
        else:
            r2='Low'
        
        if(Pulserate>=80):
            r3='High'
        elif(Pulserate>=70):
            r3='Medium'
        else:
            r3='Low'
        
        if(RBCcount>=6):
            r4='High'
        elif(RBCcount>=5):
            r4='Medium'
        else:
            r4='Low'
        
        if(WBCcount>=9):
            r5='High'
        elif(WBCcount>=6):
            r5='Medium'
        else:
            r5='Low'
            
        
        if(Platelets>=340000):
            r6='High'
        elif(Platelets>=180000):
            r6='Medium'
        else:
            r6='Low'
            
        if(HB>=17):
            r7='High'
        elif(HB>=14):
            r7='Medium'
        else:
            r7='Low'
            
        if(Uricacid>=7):
            r8='High'
        elif(Uricacid>=4):
            r8='Medium'
        else:
            r8='Low'
        
        
        if(Cholestrol>=199):
            r9='High'
        elif(Cholestrol>=130):
            r9='Medium'
        else:
            r9='Low'
        
        
        self.ld1=Label(self.f1, text=r1, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld2=Label(self.f1, text=r2, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld3=Label(self.f1, text=r3, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld4=Label(self.f1, text=r4, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld5=Label(self.f1, text=r5, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld6=Label(self.f1, text=r6, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld7=Label(self.f1, text=r7, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld8=Label(self.f1, text=r8, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        self.ld9=Label(self.f1, text=r9, width=13, height=1, font=('calbri', 14), fg='black', bg='white',borderwidth = 2,relief="ridge")
        
        self.ld1.place(x=565,y=168)
        self.ld2.place(x=565,y=196)
        self.ld3.place(x=565,y=219)
        self.ld4.place(x=565,y=247)
        self.ld5.place(x=565,y=275)
        self.ld6.place(x=565,y=303)
        self.ld7.place(x=565,y=331)
        self.ld8.place(x=565,y=353)
        self.ld9.place(x=565,y=381)
        
        root1.mainloop()
        

root=Tk()
root.title('Fitness')

mb=fitness(root)
root.mainloop()
