import tkinter as tk
from tkinter.constants import MOVETO


#1.实例化object,建立窗口
window = tk.Tk()

#2.name
window.title('My Window')

#3.set length & width
window.geometry('800x600')

#4.set three canva

canvas1 = tk.Canvas(window, bg='red', width=200)
canvas2 = tk.Canvas(window, bg='blue', height=200)
canvas3 = tk.Canvas(window, bg='green', height=200, width=500)

canvas1.pack(side='left' , expand='no' , anchor='w', fill='y')
canvas2.pack(side='top'  , expand='no' , anchor='n', fill='x')
canvas3.pack(side='right', expand='yes', anchor='n', fill='both')



#5.loop
window.mainloop()
