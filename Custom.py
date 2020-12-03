import random
import tkinter as tk
import tkinter.colorchooser
from PIL import Image,ImageTk
root = tk.Tk()
root.geometry('370x300')
root.resizable(False,False)
root.title('Sherman Gen')
icondat = [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (196, 55, 53, 255), (196, 55, 53, 255), (196, 55, 53, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (196, 55, 53, 255), (196, 55, 53, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 255), (238, 195, 154, 255), (229, 200, 152, 255), (236, 102, 52, 255), (0, 0, 0, 255), (229, 200, 152, 255), (236, 102, 52, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (0, 0, 0, 255), (140, 78, 41, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (140, 78, 41, 255), (140, 78, 41, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (251, 198, 123, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (112, 61, 34, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (140, 78, 41, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (236, 102, 52, 255), (140, 78, 41, 255), (112, 61, 34, 255), (140, 78, 41, 255), (140, 78, 41, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 255), (236, 102, 52, 255), (251, 198, 123, 255), (236, 102, 52, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (112, 61, 34, 255), (112, 61, 34, 255), (112, 61, 34, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (112, 61, 34, 255), (112, 61, 34, 255), (112, 61, 34, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (140, 78, 41, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (140, 78, 41, 255), (112, 61, 34, 255), (140, 78, 41, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (0, 0, 0, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (251, 198, 123, 255), (0, 0, 0, 255), (251, 198, 123, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (0, 0, 0, 255), (251, 198, 123, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 255), (229, 200, 152, 255), (0, 0, 0, 255), (229, 200, 152, 255), (229, 200, 152, 255), (251, 198, 123, 255), (0, 0, 0, 255), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
icon_img = Image.new('RGBA',(16,16),(0,0,0,0))
pix = icon_img.load()
counter = -1
for y in range(icon_img.size[0]):
    for x in range(icon_img.size[1]):
        counter += 1
        pix[x,y] = icondat[counter]
root.iconphoto(False, ImageTk.PhotoImage(image=icon_img,size=(16,16)))
pa_b = ['4,0', '5,0', '6,0', '7,0', '3,1', '7,1', '2,2', '5,2', '6,2', '1,3', '7,3', '1,4', '4,4', '7,4', '13,4', '14,4', '0,5', '4,5', '7,5', '11,5', '12,5', '15,5', '1,6', '8,6', '9,6', '10,6', '15,6', '1,7', '15,7', '0,8', '14,8', '0,9', '15,9', '0,10', '15,10', '0,11', '14,11', '1,12', '13,12', '2,13', '3,13', '9,13', '11,13', '12,13', '4,14', '5,14', '6,14', '7,14', '8,14', '10,14', '4,15', '6,15', '10,15']
pa_1 = ['2,3', '3,3', '4,3', '5,3', '6,3', '2,4', '3,4', '5,4', '6,4', '3,5', '6,5', '2,6', '3,6', '4,6', '5,6', '6,6', '7,6', '2,7', '3,7', '4,7', '5,7', '6,7', '7,7', '1,8', '2,8', '3,8', '4,8', '5,8', '6,8', '1,9', '2,9', '3,9', '4,9', '5,9', '1,10', '3,10']
pa_2 = ['8,7', '9,7', '8,8', '9,8', '10,8', '10,9', '2,10', '4,10', '10,10', '1,11', '2,11', '3,11', '4,11', '10,11', '2,12', '3,12', '4,12', '5,12', '7,12', '8,12', '9,12', '4,13', '5,13', '6,13', '7,13', '8,13', '10,13', '9,14', '9,15']
pa_3 = ['13,5', '14,5', '11,6', '12,6', '14,6', '10,7', '14,7', '7,8', '11,8', '13,8', '6,9', '8,9', '9,9', '11,9', '14,9', '5,10', '11,10', '14,10', '5,11', '11,11', '13,11', '6,12', '10,12', '12,12']
pa_4 = ['1,5', '2,5', '5,5', '5,15', '7,15', '8,15']
pa_5 = ['4,1', '5,1', '6,1', '3,2', '4,2']
pa_6 = ['13,6', '11,7', '12,7', '13,7', '12,8', '7,9', '12,9', '13,9', '6,10', '7,10', '8,10', '9,10', '12,10', '13,10', '6,11', '7,11', '8,11', '9,11', '12,11', '11,12']
patterns = {'pa_1':'head','pa_2':'body','pa_3':'fea2','pa_4':'acce','pa_5':'comb','pa_6':'fea1','pa_b':'base'}
head,body,fea2,acce,comb,fea1,base = (0,0,0,255),(0,0,0,255),(0,0,0,255),(0,0,0,255),(0,0,0,255),(0,0,0,255),(0,0,0,255)
base_img = Image.new('RGBA',(16,16),(0,0,0,0))
base_pix = base_img.load()
for coords in pa_b:
    base_pix[int(coords.split(',')[0]),int(coords.split(',')[1])] = (0,0,0,255)
display = tk.Canvas(root,height=256,width=256)
display.grid(column=1,row=1)
labels = tk.Frame(root,height=256,width=48)
labels.grid(column=2,row=1,sticky='w')
pickers = tk.Frame(root,height=256,width=256)
pickers.grid(column=3,row=1,sticky='w')
def generate():
    global head,body,fea2,acce,comb,fea1,base
    global img
    global photoimg
    img = Image.new('RGBA',(16,16),(0,0,0,0))
    for key in patterns.keys():
        construction = Image.new('RGBA',(16,16),(0,0,0,0))
        construction_pix = construction.load()
        for coord in eval(key):
            construction_pix[int(coord.split(',')[0]),int(coord.split(',')[1])] = (round(eval(patterns[key])[0]),round(eval(patterns[key])[1]),round(eval(patterns[key])[2]),255)
        img.paste(construction, (0, 0), construction)
    photoimg=ImageTk.PhotoImage(img.resize((256,256),resample=Image.BOX))
    update()
    root.after(100,generate)
def update():
    global photoimg
    display.delete("all")
    display.create_image(2, 2, image=photoimg, anchor='nw')
def save():
    global img
    img.save('output_16.png')
    img.resize((64,64),resample=Image.BOX).save('output_64.png')
    img.resize((128,128),resample=Image.BOX).save('output_128.png')
    img.resize((256,256),resample=Image.BOX).save('output_256.png')
tk.Button(root,text='Save',command=save).grid(column=1,row=2)
def select1():
    global selector1,head
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector1.configure(bg=color_code[1])
    head = color_code[0]
def select2():
    global selector2,body
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector2.configure(bg=color_code[1])
    body = color_code[0]
def select3():
    global selector3,fea2
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector3.configure(bg=color_code[1])
    fea2 = color_code[0]
def select4():
    global selector4,acce
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector4.configure(bg=color_code[1])
    acce = color_code[0]
def select5():
    global selector5,comb
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector5.configure(bg=color_code[1])
    comb = color_code[0]
def select6():
    global selector6,fea1
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector6.configure(bg=color_code[1])
    fea1 = color_code[0]
def select7():
    global selector7,base
    color_code = tkinter.colorchooser.askcolor(title="Choose color")
    if color_code == (None, None): return
    selector7.configure(bg=color_code[1])
    base = color_code[0]
label1=tk.Label(labels,text='Head'       , pady=3.5); label1.grid(column=0,row=0,sticky='e')
label2=tk.Label(labels,text='Body'       , pady=3.5); label2.grid(column=0,row=1,sticky='e')
label3=tk.Label(labels,text='Feathers 2' , pady=3.5); label3.grid(column=0,row=2,sticky='e')
label4=tk.Label(labels,text='Accents'    , pady=3.5); label4.grid(column=0,row=3,sticky='e')
label5=tk.Label(labels,text='Comb'       , pady=3.5); label5.grid(column=0,row=4,sticky='e')
label6=tk.Label(labels,text='Feathers 1' , pady=3.5); label6.grid(column=0,row=5,sticky='e')
label7=tk.Label(labels,text='Base'       , pady=3.5); label7.grid(column=0,row=6,sticky='e')
selector1=tk.Button(pickers,text='Select', command=select1); selector1.grid(column=0,row=0,sticky='w')
selector2=tk.Button(pickers,text='Select', command=select2); selector2.grid(column=0,row=1,sticky='w')
selector3=tk.Button(pickers,text='Select', command=select3); selector3.grid(column=0,row=2,sticky='w')
selector4=tk.Button(pickers,text='Select', command=select4); selector4.grid(column=0,row=3,sticky='w')
selector5=tk.Button(pickers,text='Select', command=select5); selector5.grid(column=0,row=4,sticky='w')
selector6=tk.Button(pickers,text='Select', command=select6); selector6.grid(column=0,row=5,sticky='w')
selector7=tk.Button(pickers,text='Select', command=select7); selector7.grid(column=0,row=6,sticky='w')
root.after(100,generate)
root.mainloop()