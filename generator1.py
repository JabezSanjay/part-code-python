
import pickle
import sys
import os
import imageio
from subprocess import call
import PIL.Image
import PIL.ImageTk

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
    myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }

    fo=open("recipt.txt","w+")
    for h in range(0,5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])
    restart_program()




new = ["hi","hello"]

u = list()

def stream(label):
 
  try:
    image = video.get_next_data()
  except:
    video.close()
    return
  label.after(delay, lambda: stream(label))
  frame_image = ImageTk.PhotoImage(Image.fromarray(image))
  label.config(image=frame_image)
  label.image = frame_image

def restart_program():
    """Restarts the current program.

    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO



class HOTEL_MANGMENT_checkin:
    
    

    def __init__(self):

        def image_show():
            part_2 = self.Entry1.get()
            print(part_2)
            if part_2 == StainlessSteel_1[0]:
                fp = open("images.png","rb")
                img = PIL.Image.open(fp)
                img.show()
                    
                    
                    
                    
                    

       
        
        
            
         

            
            
        def bill(self):

            
            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)

                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a:
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            file_save()

        
            


            





        root = Tk()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1069x742")
        root.title("PART CODE GENERATION")
        root.configure(background="#2D65A2")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        def enter(event):
            self.Button4.configure(foreground="red")

        def leave(event):
            self.Button4.configure(foreground="#000000")    
        


        video_name = str(Path().absolute()) + '/../part-code/video.mp4'
        video = imageio.get_reader(video_name)
        delay = int(1000 / video.get_meta_data()['fps'])
        

        
        
        
        
        
        
        

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#2D65A2")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        
        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.24, rely=0.11, relheight=0.79, relwidth=0.60)
        self.Message3.configure(background="#2D65A2")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="gray10")
        self.Message3.configure(highlightbackground="#ffffff")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''BUS BODY BUILDING''')
        self.Message3.configure(width=1000)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#2D65A2")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)





        root.mainloop()


if __name__ == '__main__':
    hotel=HOTEL_MANGMENT_checkin()