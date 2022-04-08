#import 

from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np 


#fucntion one_bath 
def one_bath():
    cap = cv2.VideoCapture(0)
    while (cap.read()):
        check , frame = cap.read()
        roi=frame[:1080,0:1920]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray scale
        gb = cv2.GaussianBlur(gray,(15,15),2) # gaussian blur
        result =  cv2.adaptiveThreshold(gb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1) #adaptive thres
        kernel = np.ones((1,1),np.uint8) # kernel
        dilation = cv2.dilate(result,kernel,iterations=5) # dilation
        closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel,iterations=1) #Morph Closing 
        
        result_img = closing.copy() #clone
        
        contours , hierachy = cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #contour and hierachy
        counter = 0 #count interface
        price = 0
        task = 0
        my_entry = []
        word = []
        print(task)
        for contour in contours: # check
            area = cv2.contourArea(contour)  #area in contour from Contours check
            (x,y,w,h) = cv2.boundingRect(contour) 
            if area < 800: # if area
                continue
            # cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),3)  
            # cv2.drawContours(roi,contours,-1,(0,0,255),2)
            ellipse = cv2.fitEllipse(contour) # use value in contour
            cv2.ellipse(roi,ellipse,(0,255,0),2) # draw
            counter+=1 #count ++
            price = counter*1
            my_entry.append(price)
            task = my_entry[-1]
            print(task)
            print(my_entry[-1])
            if task == my_entry[-1]:
                word = ['มีเหรียญบาททั้งหมด %s บาท'%(my_entry[-1])]
                word2 = ['มีเหรียญบาทรวม %s เหรียญ'%counter]
                lb_one.insert(0,word[0])
                lb_one.insert(1,word2[0])
                                
        cv2.putText(roi,'Coin: '+ str(counter),(10,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        cv2.putText(roi,'Result: '+ str(price),(10,120),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        # cv2.imshow('B',closing)
        cv2.imshow('Coin', roi)
        
        if cv2.waitKey(1) & 0xFF == ord('0'):
            cv2.destroyAllWindows()
            return task
            break  

#fucntion two_bath
def two_bath():
    cap = cv2.VideoCapture(0)
    while (cap.read()):
        check , frame = cap.read()
        roi=frame[:1080,0:1920]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray scale
        gb = cv2.GaussianBlur(gray,(15,15),2) # gaussian blur
        result =  cv2.adaptiveThreshold(gb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1) #adaptive thres
        kernel = np.ones((1,1),np.uint8) # kernel
        dilation = cv2.dilate(result,kernel,iterations=5) # dilation
        closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel,iterations=1) #Morph Closing 
        
        result_img = closing.copy() #clone
        
        contours , hierachy = cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #contour and hierachy
        counter = 0 #count interface
        price = 0
        task = 0
        my_entry = []
        word = []
        for contour in contours: # check
            area = cv2.contourArea(contour)  #area in contour from Contours check
            (x,y,w,h) = cv2.boundingRect(contour) 
            if area < 1500 or area > 15000: # if area
                continue
            # cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),3)  
            # cv2.drawContours(roi,contours,-1,(0,0,255),2)
            ellipse = cv2.fitEllipse(contour) # use value in contour
            cv2.ellipse(roi,ellipse,(0,255,0),2) # draw
            counter+=1 #count ++
            price = counter*2 
            my_entry.append(price)
            task = my_entry[-1]
            print(task)
            print(my_entry[-1])
            if task == my_entry[-1]:
                word = ['มีเหรียญสองบาททั้งหมด %s บาท'%(my_entry[-1])]
                word2 = ['มีเหรียญสองบาทรวม %s เหรียญ'%counter]
                lb_two.insert(0,word[0])
                lb_two.insert(1,word2[0])
                                
        cv2.putText(roi,'Coin: '+ str(counter),(10,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        cv2.putText(roi,'Result: '+ str(price),(10,120),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        # cv2.imshow('B',closing)
        cv2.imshow('Coin', roi)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            cv2.destroyAllWindows()
            break



#fucntion five bath
def five_bath():
    cap = cv2.VideoCapture(0)
    while (cap.read()):
        check , frame = cap.read()
        roi=frame[:1080,0:1920]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray scale
        gb = cv2.GaussianBlur(gray,(15,15),2) # gaussian blur
        result =  cv2.adaptiveThreshold(gb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1) #adaptive thres
        kernel = np.ones((1,1),np.uint8) # kernel
        dilation = cv2.dilate(result,kernel,iterations=5) # dilation
        closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel,iterations=1) #Morph Closing 
        
        result_img = closing.copy() #clone
        
        contours , hierachy = cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #contour and hierachy
        counter = 0 #count interface
        price = 0
        task = 0
        my_entry = []
        word = []
        for contour in contours: # check
            area = cv2.contourArea(contour)  #area in contour from Contours check
            (x,y,w,h) = cv2.boundingRect(contour) 
            if area < 1500 or area > 15000: # if area
                continue
            # cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),3)  
            # cv2.drawContours(roi,contours,-1,(0,0,255),2)
            ellipse = cv2.fitEllipse(contour) # use value in contour
            cv2.ellipse(roi,ellipse,(0,255,0),2) # draw
            counter+=1 #count ++
            price = counter*5 
            my_entry.append(price)
            task = my_entry[-1]
            print(task)
            print(my_entry[-1])
            if task == my_entry[-1]:
                word = ['มีเหรียญห้าบาททั้งหมด %s บาท'%(my_entry[-1])]
                word2 = ['มีเหรียญห้าบาทรวม %s เหรียญ'%counter]
                lb_five.insert(0,word[0])
                lb_five.insert(1,word2[0])
                                
        
        
        
        
        cv2.putText(roi,'Coin: '+ str(counter),(10,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        cv2.putText(roi,'Result: '+ str(price),(10,120),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        # cv2.imshow('B',closing)
        cv2.imshow('Coin', roi)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            cv2.destroyAllWindows()
            break



#function ten bath
def ten_bath():
    cap = cv2.VideoCapture(0)
    while (cap.read()):
        check , frame = cap.read()
        roi=frame[:1080,0:1920]
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #gray scale
        gb = cv2.GaussianBlur(gray,(15,15),2) # gaussian blur
        result =  cv2.adaptiveThreshold(gb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1) #adaptive thres
        kernel = np.ones((1,1),np.uint8) # kernel
        dilation = cv2.dilate(result,kernel,iterations=5) # dilation
        closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel,iterations=1) #Morph Closing 
        
        result_img = closing.copy() #clone
        
        contours , hierachy = cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #contour and hierachy
        counter = 0 #count interface
        price = 0
        task = 0
        my_entry = []
        word = []
        for contour in contours: # check
            area = cv2.contourArea(contour)  #area in contour from Contours check
            (x,y,w,h) = cv2.boundingRect(contour) 
            if area < 1500 or area > 15000: # if area
                continue
            # cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),3)  
            # cv2.drawContours(roi,contours,-1,(0,0,255),2)
            ellipse = cv2.fitEllipse(contour) # use value in contour
            cv2.ellipse(roi,ellipse,(0,255,0),2) # draw
            counter+=1 #count ++
            price = counter*10
            
            
            my_entry.append(price)
            task = my_entry[-1]
            print(task)
            print(my_entry[-1])
            if task == my_entry[-1]:
                word = ['มีเหรียญสิบบาททั้งหมด %s บาท'%(my_entry[-1])]
                word2 = ['มีเหรียญสิบบาทรวม %s เหรียญ'%counter]
                lb_ten.insert(0,word[0])
                lb_ten.insert(1,word2[0])
                                 
                
                
        cv2.putText(roi,'Coin: '+ str(counter),(10,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        cv2.putText(roi,'Result: '+ str(price),(10,120),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2,cv2.LINE_AA) #text
        # cv2.imshow('B',closing)
        cv2.imshow('Coin', roi)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            cv2.destroyAllWindows()
            break



#function result
def result():
    txt1 = lb_one.get(0,None)
    txt2 = lb_two.get(0,None)
    txt3 = lb_five.get(0,None)
    txt4 = lb_ten.get(0,None)
    
    txt5 = lb_one.get(1,None)
    txt6 = lb_two.get(1,None)
    txt7 = lb_five.get(1,None)
    txt8 = lb_ten.get(1,None)
    
    val1 = [int(s) for s in txt1.split() if s.isdigit()]
    val2 = [int(s) for s in txt2.split() if s.isdigit()]
    val3 = [int(s) for s in txt3.split() if s.isdigit()]
    val4 = [int(s) for s in txt4.split() if s.isdigit()]
    
    val5 = [int(s) for s in txt5.split() if s.isdigit()]
    val6 = [int(s) for s in txt6.split() if s.isdigit()]
    val7 = [int(s) for s in txt7.split() if s.isdigit()]
    val8 = [int(s) for s in txt8.split() if s.isdigit()]
    
    all = val1+val2+val3+val4
    summary = val5+val6+val7+val8
    print(summary)
    
    summ = 0
    summ2 = 0
    
    for i in all:
        number = int(i)
        summ +=number
    
    for a in summary :
        number2 = int(a)
        summ2 +=number2
        
    display = ('มีเงินรวมทั้งหมดอยู่ %d บาท'%summ)
    stable = ('มีจํานวนเหรียญรวมทั้งหมด %d เหรียญ'%summ2)
    
    # print(summ)
    # print(val1)
    # print(val2)
    # print(val3)
    # print(val4)
    # print(all)
    
    # lb_result.insert(0,val1)
    # lb_result.insert(0,val2)
    # lb_result.insert(0,val3)
    lb_result.insert(0,display)
    lb_result.insert(0,stable)
                                 



#fucntion delTask 
def delTask():
      select1 = lb_one.curselection()
      select2 = lb_two.curselection()
      select3 = lb_five.curselection()
      select4 = lb_ten.curselection()
      for item in select1[::-1]:
          lb_one.delete(0,END)
      for item in select2[::-1]:
          lb_two.delete(0,END)
      for item in select3[::-1]:
          lb_five.delete(0,END)
      for item in select4[::-1]:
          lb_ten.delete(0,END)
    

#function Exit
def Exit():
    ws.destroy()   

#function DelAll
def DelAll():
    lb_one.delete(0,END)
    lb_two.delete(0,END)
    lb_five.delete(0,END)
    lb_ten.delete(0,END)


#window
ws = Tk()
ws.geometry('1000x800+500+200')
ws.title('Coin Detection and Counting')
ws.config(bg='#F1C0E8')
ws.resizable(width=False,height=False)

#frame
frame = Frame(ws)
frame2 = Frame(ws)
frame3 = Frame(ws)
frame4 = Frame(ws)
frame5 = Frame(ws)

frame5.pack(pady=20)
frame.pack(pady=10)
frame2.pack(pady=10)
frame3.pack(pady=10)
frame4.pack(pady=10)

#heading
var = StringVar()
label = Label(frame5,
              textvariable=var,
              relief=RAISED,
              bg = '#CFBAF0',
              font=('Times',15),
              highlightthickness=0,
              fg = '#413839'
                 
              )
var.set('''โปรแกรมนับเหรียญ และ คํานวณเหรียญ 
        วิธีใช้ เลือกค่าเหรียญที่ต้องการคํานวณ จากนั้นนํากล้องไปจับบริเวณที่ต้องการนับ จากนั้นกดปุ่ม 0 เพื่อจบการทํางาน
        การตรวจจับจะมีประสิทธิภาพมากก็ต่อเมื่อพื้นผิวเป็นสีพื้นเท่านั้น''')
label.pack(fill=BOTH,pady=2)

#listbox
lb_one = Listbox(
    frame,
    width=30,
    height=2,
    font=('Times',18),
    bg = '#FBF8CC',
    bd = 0,
    fg = '#2F4F4F',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
    justify=CENTER
)
lb_two = Listbox(
    frame2,
    width=30,
    height=2,
    font=('Times',18),
    bd = 0,
    bg = '#FBF8CC',
    fg = '#2F4F4F',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
    justify=CENTER
)
lb_five = Listbox(
    frame3,
    width=30,
    height=2,
    font=('Times',18),
    bd = 0,
    bg = '#FBF8CC',
    fg = '#2F4F4F',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
    justify=CENTER
)
lb_ten = Listbox(
    frame4,
    width=30,
    height=2,
    font=('Times',18),
    bd = 0,
    bg = '#FBF8CC',
    fg = '#2F4F4F',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none',
    justify=CENTER
)

lb_result = Listbox(
    ws,
    font = ('Times',20),
    width = 3,
    height = 2,
    bg = '#FDE4CF',
    fg = '#413839',
    highlightthickness=0,
    activestyle='none',
    justify=CENTER
)



lb_one.pack(side=LEFT,fill=BOTH)
lb_two.pack(side=LEFT,fill=BOTH)
lb_five.pack(side=LEFT,fill=BOTH)
lb_ten.pack(side=LEFT,fill=BOTH)
lb_result.pack(pady=10,fill=BOTH)


#button frame
button_frame = Frame(ws)
button_frame2 = Frame(ws)
button_frame.pack(pady=20)
button_frame2.pack(pady=10)

#button option 1 2 5 10 bath and result
one_btn = Button(
    button_frame,
    text = '1 บาท',
    font=('times 14'),
    bg='#B9FBC0',
    padx=5,
    pady=5,
    command = one_bath
)
one_btn.pack(fill=BOTH,expand=True,side=LEFT)

two_btn = Button(
    button_frame,
    text='2 บาท',
    font=('times 14'),
    bg='#98F5E1',
    padx=20,
    pady=5,
    command = two_bath
)
two_btn.pack(fill=BOTH,expand=True,side=LEFT)

five_btn = Button(
    button_frame,
    text='5 บาท',
    font=('times 14'),
    bg='#8EECF5',
    padx=20,
    pady=5,
    command = five_bath
)
five_btn.pack(fill=BOTH,expand=True,side=LEFT)

ten_btn = Button(
    button_frame,
    text='10 บาท',
    font=('times 14'),
    bg='#A3C4F3',
    padx=10,
    pady=5,
    command = ten_bath
)
ten_btn.pack(fill=BOTH,expand=True,side=LEFT)

all_btn = Button(
    button_frame,
    text='รวม',
    font=('times 14'),
    bg='#CFBAF0',
    padx=10,
    pady=5,
    command = result
)
all_btn.pack(fill=BOTH,expand=True,side=LEFT)

#button adding add/del

del_btn = Button(
    button_frame2,
    text='ลบข้อมูลเหรียญ',
    font=('times 14'),
    bg='#FFAE92',
    padx=10,
    pady=5,
    command = delTask
)
del_btn.pack(fill=BOTH,expand=True,side=LEFT)

delAll_btn = Button(
    button_frame2,
    text='ลบทั้งหมด',
    font=('times 14'),
    bg='#EDAB94',
    padx=20,
    pady=5,
    command = DelAll
)
delAll_btn.pack(fill=BOTH,expand=True,side=LEFT)

exit_btn = Button(
    button_frame2,
    text='ออก',
    font=('times 14'),
    bg='#FBD4AD',
    padx=20,
    pady=5,
    command = Exit
)
exit_btn.pack(fill=BOTH,expand=True,side=LEFT)

ws.mainloop()