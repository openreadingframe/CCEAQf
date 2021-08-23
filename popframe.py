from savepdf import save_pdf
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Scrollbar, Checkbutton, Label, Button

from pdf2png import pyMuPDF_fitz


def open_file(path, event=None):
    input_file = filedialog.askopenfilename(
        filetypes=[("pdf文档", "*.pdf"), ("所有文件", "*.*")])
    path.set(input_file) # 把路径名放在entry里


def open_folder(path, event=None):
    output_file = filedialog.askdirectory()
    path.set(output_file)


def pdf2png(input_path, output_path):
    if (input_path.get()=='' and output_path.get()==''):
        # print("请输入两个路径!")
        messagebox.showwarning("温馨提示", "请输入两个路径!")
    elif (input_path.get()==''):
        # print("请输入pdf路径!")
        messagebox.showwarning("温馨提示", "请输入pdf路径!")
    elif (output_path.get()==''):
        # print("请输入目标路径!")
        messagebox.showwarning("温馨提示", "请输入目标路径!")
    else:
        try:
            pyMuPDF_fitz(input_path.get(), output_path.get())
            messagebox.showinfo("有情况", "输出成功到%s!" % output_path.get())
        except:
            messagebox.showwarning("额", "出错了!")


def savepdf(input_path, output_path):
    if (input_path.get()=='' and output_path.get()==''):
        # print("请输入两个路径!")
        messagebox.showwarning("温馨提示", "请输入两个路径!")
    elif (input_path.get()==''):
        # print("请输入pdf路径!")
        messagebox.showwarning("温馨提示", "请输入网页链接!")
    elif (output_path.get()==''):
        # print("请输入目标路径!")
        messagebox.showwarning("温馨提示", "请输入目标路径!")
    else:
        try:
            state = save_pdf(input_path.get(), output_path.get())
            if (state == 0):
                messagebox.showwarning("额", "出错了!")
            elif (state == 1):
                messagebox.showwarning("温馨提示", "文件已存在!")
            elif (state == 2):
                messagebox.showinfo("有情况", "输出成功到%s!" % output_path.get())
            else:
                raise Exception
        except:
            messagebox.showwarning("额", "出错了!")
            

def pop_frame(self, frame_name):
    """a small pop frame"""
    new_toplevel = Toplevel(self)
    new_toplevel.title(frame_name)
    new_toplevel.transient(self)  # 总是让搜索框显示在其父窗体之上
    new_toplevel.resizable(False, False)

    if frame_name == "pdf转图片":
        Label(new_toplevel, text="pdf源文件路径").grid(row=0, column=0, sticky='e')
        input_path = StringVar()
        input_path_entry_widget = Entry(new_toplevel, width=25, textvariable=input_path)
        input_path_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        input_path_entry_widget.focus_set() # 光标
        Button(new_toplevel, text="打开pdf文件", command=lambda: open_file(input_path)
        ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

        Label(new_toplevel, text="png图片输出路径").grid(row=1, column=0, sticky='e')
        output_path = StringVar()
        output_path_entry_widget = Entry(new_toplevel, width=25, textvariable=output_path)
        output_path_entry_widget.grid(row=1, column=1, padx=2, pady=2, sticky='we')
        Button(new_toplevel, text="选择输出文件夹", command=lambda: open_folder(output_path)
        ).grid(row=1, column=2, sticky='e' + 'w', padx=2, pady=2)

        # 命令按钮
        Button(new_toplevel, text="输出!", command=lambda: pdf2png(input_path, output_path)
        ).grid(row=2, column=1, sticky='n', padx=2, pady=2)
    
    elif frame_name == "下载pdf":
        Label(new_toplevel, text="pdf网页链接").grid(row=0, column=0, sticky='e')
        input_path = StringVar()
        input_path_entry_widget = Entry(new_toplevel, width=25, textvariable=input_path)
        input_path_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        input_path_entry_widget.focus_set() # 光标
        Button(new_toplevel, text="选择已有链接",
        ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

        Label(new_toplevel, text="下载到本地路径").grid(row=1, column=0, sticky='e')
        output_path = StringVar()
        output_path_entry_widget = Entry(new_toplevel, width=25, textvariable=output_path)
        output_path_entry_widget.grid(row=1, column=1, padx=2, pady=2, sticky='we')
        Button(new_toplevel, text="选择输出文件夹", command=lambda: open_folder(output_path)
        ).grid(row=1, column=2, sticky='e' + 'w', padx=2, pady=2)

        # 命令按钮
        Button(new_toplevel, text="下载!", command=lambda: savepdf(input_path, output_path)
        ).grid(row=2, column=1, sticky='n', padx=2, pady=2)


    ## 窗体的位置,使之在中间
    new_toplevel.update_idletasks() ## 更新窗口大小,确保当前获得的宽度和高度是最新的
    wgt_width, wgt_height = new_toplevel.winfo_width(), new_toplevel.winfo_height() ## 获取
    ## print(wgt_width, wgt_height)
    root_width, root_height = self.winfo_width(), self.winfo_height() ## 获取根窗口大小
    ## print(root_width, root_height)
    root_locx, root_locy = self.winfo_rootx(), self.winfo_rooty() ## 获取根窗口位置
    ## print(root_locx, root_locy)
    wm_val = '%dx%d+%d+%d' % (wgt_width, wgt_height, 
    root_locx+(root_width-wgt_width)/2, root_locy+(root_height-wgt_height)/2)
    new_toplevel.geometry(wm_val) ## 设定窗口大小和位置

    def close_new_window():
        new_toplevel.destroy()

    new_toplevel.protocol('WM_DELETE_WINDOW', close_new_window)
    return "break"
