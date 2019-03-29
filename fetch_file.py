# -*- coding: utf-8 -*-

# GUIでpdf、jpgファイル取ってこられるようにしたやつ
# 今は探索フォルダの直下しか探せないので、探索フォルダ以下すべてのフォルダを探せるようにしたい（やり方がわからん）


import wx, glob, tkinter, os, glob, shutil
from datetime import datetime
from tkinter import messagebox

dir_path = datetime.now().strftime("%Y.%m.%d_%H%M-%S")
if not os.path.isdir(dir_path):
    os.mkdir(dir_path)    


app = wx.App()

dialog = wx.DirDialog(None, u'フォルダを選択してください')

dialog.ShowModal()
print(dialog.GetPath())


namedialog = tkinter.Tk()
namedialog.title(u"ファイル名を入力")
namedialog.geometry("920x480")

pdfcheck = tkinter.BooleanVar()
pdfcheck.set(False)

jpgcheck = tkinter.BooleanVar()
jpgcheck.set(False)

def fetch_files(event):
    result = text_box.get('1.0', 'end -1c')
    result = result.splitlines()
    filename_list = []
    for i in result:
        if pdfcheck.get():
            filename_list.append(i + '.pdf')
        if jpgcheck.get():
            filename_list.append(i + '.jpg')

    counter = 0

    for i in filename_list:
        print(dialog.GetPath() + '\\' + i)
        aaaaa = glob.glob(dialog.GetPath() + '\\' + i)
        print(aaaaa)
        for j in aaaaa:
            shutil.copyfile(j, dir_path + '\\' + i)
            print(i + 'をコピーした')
            counter += 1
    messagebox.showinfo('確認', str(counter) + '個のファイルを' + dir_path + 'にコピーしました')


def directory_change(event):
    dialog.ShowModal()
    print(dialog.GetPath())
    nowdirectory_label["text"] = "探索ディレクトリ：" + dialog.GetPath()


text_box = tkinter.Text()
text_box.pack()

check_pdf = tkinter.Checkbutton(text='.pdf', variable = pdfcheck)
check_pdf.pack()

check_jpg = tkinter.Checkbutton(text='.jpg', variable = jpgcheck)
check_jpg.pack()

button = tkinter.Button(text=u'取ってくる')
button.bind("<Button-1>",fetch_files) 
button.pack()

button2 = tkinter.Button(text=u'探索ディレクトリ変更')
button2.bind("<Button-1>",directory_change) 
button2.pack()

nowdirectory_label = tkinter.Label(text="探索ディレクトリ：" + dialog.GetPath())
nowdirectory_label.pack()


namedialog.mainloop()

