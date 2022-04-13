# GUI-calculator.py
'''
******************************************
                 เกมส์ทายตัวเลข
                   V 0.2
                   13/04/2022
            by Jirapong Chintanet

******************************************
'''
from tkinter import *
from tkinter import ttk, messagebox
import random
import time
new_game = 0
check_ans =0
rand_num =0




    
GUI = Tk()  #เข้าโหมด กราฟฟิก
GUI.title('Guess Random Number')#ตั้งชื่อ
GUI.geometry('800x800')#กำหนดขนาด

if rand_num ==0: #สุ่มตัวเลข
    a = b =c =d = random.randint(0,9)
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        correct = location = 0
    gameover = 0  
    ts = time.time()
    rand_num = 1

'''   
    print ("first random") #for debug
    print (a , b , c ,d)
    print ("new_game = ",new_game)
    print ("check_ans = ",check_ans)
    print ("rand_num = ",rand_num)
'''




bg = PhotoImage(file='lucky_num.png') #แสดง รูป background
BG = Label(GUI, image=bg)
BG.pack()

L1 = Label(GUI,text = 'เกมส์ทายตัวเลข 4 หลัก',font=(None,20)) #แสดงข้อความเข้าเกมส์
L1.pack() # ให้ Label ไปติดกับโปรแกรม
L2 = Label(GUI,text ='ทายตัวเลข 4 ตัว ที่ไม่ซ้ำกัน จาก 0-9 ให้ถูกตามตำแหน่ง\n หากทายถูกตำแหน่ง จะได้ +1 correct  หากตัวเลขถูก แต่ไม่ถูกตำแหน่ง จะได้ +1 location\n หากต้องการยอมแพ้ กด 0000',font=(None,12))
L2.pack()          

frame= Frame(GUI)#สร้าง frame text ไว้แสดงผล
frame.config()
frame.place(width=300,height=250,x=0,y=350)

def Showerr():
    messagebox.showinfo('ERROR','กรุณาใส่แค่ตัวเลข 4 หลักเท่านั้น')
def Giveup():
    messagebox.showinfo('ยอมแพ้','พยายามต่อไป\n คำตอบคือ '+ str(a)+str(b)+str(c)+str(d))
def Start(): #สร้าง function คำนวน
#    messagebox.showinfo('xxxxxxx','yyyyyyyy')
    new_game = 0
    check_ans =0
    rand_num =0
    
    print ('New Game') #for debug
    print ("new_game = ",new_game)
    print ("check_ans = ",check_ans)
    print ("rand_num = ",rand_num)

   

def Finish(): #สร้าง function คำนวน
    messagebox.showinfo('Finish','ยินดีด้วย คุณทายตัวเลขถูกทั้ง 4 หลัก\nใช้เวลาไป'+ str(time.time() - ts )+' วินาที')

def Answer(event = None): #สร้าง function คำนวน event = None
    try:
        
        ans=int(ans_txt.get()) #แปลงตัวอักษรเป็นตัวเลข
        correct = location = 0
        a_ans = ans // 1000
        b_ans = ((ans - (ans // 1000) * 1000)) // 100
        c_ans = ((ans - (ans // 100) * 100)) // 10
        d_ans = ((ans - (ans // 10) *10))

    #    print (a_ans,b_ans,c_ans,d_ans)  #for debug
        if ans > 9999:
            Showerr()
        #check a
        if a_ans == a:
            correct = correct+1
        elif a_ans == b or a_ans == c or a_ans == d:
            location = location+1
        #check b
        if b_ans == b:
            correct = correct+1
        elif b_ans == a or b_ans == c or b_ans == d:
            location = location+1
        #check c
        if c_ans == c:
            correct = correct+1
        elif c_ans == a or c_ans == b or c_ans == d:
            location = location+1
        #check d
        if d_ans == d:
            correct = correct+1
        elif d_ans == a or d_ans == b or d_ans == c:
            location = location+1
        if a_ans == b_ans == c_ans == d_ans == 0:
            Giveup()
            
     #   print (a_ans , b_ans , c_ans ,d_ans , ':>',correct ,'correct' , location , 'location') #for debug
        text3.insert(INSERT,a_ans)
        text3.insert(INSERT,b_ans)
        text3.insert(INSERT,c_ans)
        text3.insert(INSERT,d_ans)
        text3.insert(INSERT," :> ")
        text3.insert(INSERT,correct)
        text3.insert(INSERT," C")
        text3.insert(INSERT," | ")
        text3.insert(INSERT,location)
        text3.insert(INSERT," L\n")

        
        if correct == 4:
            Finish()
        correct = location = 0
    except:
        Showerr()
        
        

#สร้างปุ่ม New Game
B1 = ttk.Button(GUI, text = 'NEW GAME',command = Start)
B1.pack(ipadx=10,ipady=5) #ipadx size of button

    
#สร้าง การป้อนข้อมูล
Label(GUI,text="เลขที่ทาย ",font =('Calibri 10')).pack()
ans_txt= ttk.Entry(GUI, width=30)
ans_txt.pack()
    
#สร้าง ปุ่ม Answer
B2 = ttk.Button(GUI, text = 'Answer',command = Answer)
B2.pack(padx=30 ,pady=10 ,ipadx=30,ipady=20) #ipadx size of button
B2.bind('<Return>',Answer)

#สร้างช่องแสดงผลลัพท์
text3 = Text(frame, width =20)
text3.pack(side=RIGHT,padx=10,pady=10)
text3.insert(INSERT,"Number "+" Result\n")
text3.insert(INSERT,"====== "+" ======\n")


'''
print ("new_game = ",new_game) #for debug
print ("check_ans = ",check_ans)
print ("rand_num = ",rand_num)
'''
GUI.mainloop() #run loop

