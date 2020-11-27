import subprocess
import os
import tkinter as tk

root = tk.Tk()
root.title('Desky')
root.wm_attributes("-alpha",0.95)
canvas1 = tk.Canvas(root,bg="#444", width = 500, height = 400)
canvas1.create_line(10, 0, 50, 400, fill="#d3d3d3")
canvas1.create_line(50, 20, 500, 20, fill="#d3d3d3")
canvas1.create_line(20, 0, 60, 400, fill="#d3d3d3")
canvas1.create_line(250, 120, 500, 120, fill="#d3d3d3")
canvas1.create_line(30, 0, 70, 400, fill="#d3d3d3")
canvas1.create_line(40, 0, 80, 400, fill="#d3d3d3")
canvas1.create_line(130, 320, 500, 320, fill="#d3d3d3")
canvas1.create_line(50, 0, 90, 400, fill="#d3d3d3")

canvas1.pack()

def start_batch(): 
       subprocess.call([r'Junkclean.bat'])
def start_batch2():
       os.startfile("C:\Windows\System32\dxdiag.exe")
def start_batch3():
       os.startfile("C:\Windows\System32\compmgmt.msc")
def start_batch4():
       os.startfile("C:\Windows\System32\diskmgmt.msc")
def start_batch5():
       subprocess.call([r'regedt.bat'])
def start_batch6():
       subprocess.call([r'makefolder.bat'])
       root= tk.Tk()  
       canvas2 = tk.Canvas(root,bg="#444", width = 400, height = 400)
       canvas2.create_line(10, 0, 50, 400, fill="#d3d3d3")
       canvas2.create_line(70, 80, 500, 420, fill="#d3d3d3")
       canvas2.create_line(20, 0, 60, 400, fill="#d3d3d3")
       canvas2.create_line(250, 120, 500, 120, fill="#d3d3d3")
       canvas2.create_line(30, 0, 70, 400, fill="#d3d3d3")
       canvas2.create_line(40, 0, 80, 400, fill="#d3d3d3")
       canvas2.create_line(130, 320, 500, 320, fill="#d3d3d3")
       canvas2.create_line(50, 0, 90, 400, fill="#d3d3d3")
       canvas2.pack()
       button17 = tk.Button (root, text='Input Folder is Generated on the Desktop\n Please copy all the files into it then click on sort now',bg='#444',fg='red')
       canvas2.create_window(190,50, window=button17)
       button16 = tk.Button (root, text='Sort Now',command=start_batch16,bg='#d3d3d3',fg='#13024f')
       canvas2.create_window(190,190, window=button16)
       
def start_batch8():
       os.startfile("C:\Windows\System32\devmgmt.msc")
def start_batch9():
       os.startfile("C:\Windows\System32\SystemPropertiesPerformance.exe")
def start_batch10():
       import webbrowser
       webbrowser.open('https://rufus.ie/', new=2)
def start_batch11():
       import webbrowser
       webbrowser.open('https://grill2010.github.io/droidJoy.html', new=2)
def start_batch12():
       os.startfile("C:\Windows\System32\Bubbles.scr")
def start_batch13():
       os.startfile("C:\Windows\System32\cleanmgr.exe")
def start_batch14():
       os.startfile("C:\Windows\System32\colorcpl.exe")
def start_batch15():
       os.startfile("C:\Windows\System32\dfrgui.exe")
def start_batch16():
       subprocess.call([r'sort.bat'])

       
button1 = tk.Button (root, text='Clear Junk',command=start_batch,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130, 100, window=button1)

button2 = tk.Button (root, text='Direct X version',command=start_batch2,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350, 100, window=button2)

button3 = tk.Button (root, text='Computer Management',command=start_batch3,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130, 130, window=button3)

button4 = tk.Button (root, text='Disk Management',command=start_batch4,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350, 130, window=button4)

button5 = tk.Button (root, text='Rigistry editor',command=start_batch5,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130, 160, window=button5)

button6 = tk.Button (root, text='File Sorting',command=start_batch6,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350, 160, window=button6)

button8 = tk.Button (root, text='Device Manager',command=start_batch8,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130, 190, window=button8)

button9 = tk.Button (root, text='Performance(System)',command=start_batch9,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350, 190, window=button9)

button10 = tk.Button (root, text='Rufus(Make bootable media)',command=start_batch10,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130,220, window=button10)

button11 = tk.Button (root, text='Use android as gamepad for pc',command=start_batch11,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350,220, window=button11)

button12 = tk.Button (root, text='Animation screen saver',command=start_batch12,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130,250, window=button12)

button13 = tk.Button (root, text='Disk cleanup',command=start_batch13,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350,250, window=button13)

button14 = tk.Button (root, text='color management',command=start_batch14,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(130,280, window=button14)

button15 = tk.Button (root, text='Defragmentation',command=start_batch15,bg='#d3d3d3',fg='#13024f')
canvas1.create_window(350,280, window=button15)


root.mainloop()
