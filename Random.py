import random
import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.geometry('260x300')
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
patterns = {'base.png':'pa_b', '1.png':'pa_1', '2.png':'pa_2', '3.png':'pa_3', '4.png':'pa_4', '5.png':'pa_5', '6.png':'pa_6'}
base = Image.new('RGBA',(16,16),(0,0,0,0))
base_pix = base.load()
for coords in pa_b:
    base_pix[int(coords.split(',')[0]),int(coords.split(',')[1])] = (0,0,0,255)
display = tk.Canvas(root,height=256,width=256) # ,bg='#ff2020'
display.grid(column=1,row=1,columnspan=2)
def generate():
    global img
    global photoimg
    img = Image.new('RGBA',(16,16),(0,0,0,0))
    for key in patterns.keys():
        if key == 'base.png':
            continue
        # repeat for each pattern
        r,g,b = (random.randint(1, 225)),(random.randint(1, 225)),(random.randint(1, 225))
        construction = Image.new('RGBA',(16,16),(0,0,0,0))
        construction_pix = construction.load()
        coordinates = eval(patterns[key])
        for coord in coordinates:
            construction_pix[int(coord.split(',')[0]),int(coord.split(',')[1])] = (r,g,b,255)
        img.paste(construction, (0, 0), construction)
    img.paste(base, (0, 0), base)
    photoimg=ImageTk.PhotoImage(img.resize((256,256),resample=Image.BOX))
    update()
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
tk.Button(root,text='Generate',command=generate).grid(column=1,row=2,sticky='e')
tk.Button(root,text='Save',command=save).grid(column=2,row=2,sticky='w')
root.mainloop()