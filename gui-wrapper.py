from Tkinter import *
from PIL import Image, ImageTk
import os.path
import tkMessageBox



#create class window and inherit from Frame
class Window(Frame):
    #variable initialization
    isLogin = False

    #Gui initialization
    def __init__(self, master=None):
        #parameter that you want for Frame class, param master as root of window tkinter
        Frame.__init__(self, master)
        #reference to the master widget, which is tkinter window
        self.master = master
        self.init_window()


    #GUI config and widget 
    def init_window(self):
        #set size of window
        self.master.geometry("480x320")

        if (self.isLogin is False):
            self.loginPage()

    #login page
    def loginPage(self):

        #local variable initialization 
        vcmd = self.master.register(self.validate)

        #event for response if return hit and focus to other widget
        def inputHandlerNim(event):
            if (str(event.char) == '\r'):
                entPwd.focus()
            elif (str(event.char) == '-'):
                print("reset config")
                entNIM.delete(0, 'end')
                entPwd.delete(0, 'end')

        def inputHandlerPass(event):
            if (str(event.char) == '\r'):
                print("Login")
                loginMessage()
            elif (str(event.char) == '-'):
                print("reset config")
                entNIM.focus()
                entNIM.delete(0, 'end')
                entPwd.delete(0, 'end')

        def loginMessage():
            tkMessageBox.showinfo("Login Status","Login Successfully")


        #title of window
        self.master.title("LOGIN PAGE")
        
        #set icon window
        
        #show image in center of window
        #get absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        #load image
        load = Image.open(os.path.join(script_dir,"img/uisi-1.png"))
        photo = ImageTk.PhotoImage(load)
        w = Label(self.master, image=photo)
        w.image = photo
        w.pack()

        #create a label for the instructions
        lblInstruc = Label(self.master, text="Please Input NIM and Password")
        #and pack it into the window
        lblInstruc.pack()

        #create the widgets for entering a NIM
        lblNIM = Label(self.master, text="NIM")
        entNIM = Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))

        #and pack the into the window
        lblNIM.pack()
        entNIM.pack()
        #focust to entry NIM in start of program
        entNIM.focus()
        entNIM.bind('<Key>', inputHandlerNim)

        #create widgets for entering password
        lblPwd = Label(self.master, text="Password")
        entPwd = Entry(self.master, validate="key", validatecommand=(vcmd, '%P'))
        #and pack the into the window
        lblPwd.pack()
        entPwd.pack()
        entPwd.bind('<Key>', inputHandlerPass)

        lblInfo = Label(self.master, text="Press Enter to next, Press '-' for Reset input")
        lblInfo.pack()

        
    
    #validate input
    def validate(self,newtext):
        print('validate: {}'.format(newtext))
        if ('-' in newtext):
            return False
        else:
            return True

    

#create instance from Tkinter
root = Tk()
#create instance from Window class
app = Window(root)
#run program
app.mainloop()


