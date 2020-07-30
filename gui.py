import sys
from tkinter import *
from tkinter.filedialog import *
from tkinter import font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image
import decrypt
import crypt
import os
import sys

class FilePathFrame(Frame):
    

    def __init__(self, master, *args, **kwargs):
        
        global item_file
        
        item_file = StringVar()
        
        super(FilePathFrame, self).__init__(master, *args, **kwargs)

        def entry_set(entry, text):
            entry.delete(0, 'end')
            entry.insert(END, text)
        
        helv36 = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)
        # ROW 1
        Label(self).grid(row=1, column = 0)
        # ROW 2
        Label(self).grid(row=2, column = 0)

        item_button = Button(self, text="Seleccionar archivo",bg="gray88", font=helv36,width=17,command=lambda: (entry_set(item_entry, askopenfilename(title="Seleccionar archivo")), item_entry.configure(fg="black")))
        item_button.grid(row=2,column=1)
        
        Label(self).grid(row=2, column = 2)
        
        item_entry = Entry(self, textvariable=item_file,width=45)
        item_entry.grid(row=2,column=3)

        Label(self).grid(row=2, column = 4)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def command_desencriptar(window):

    global decryptPassword
    global decryptLabel
    fileInput = item_file.get()

    if(fileInput == ""):
        mainResult.configure(text = "No se ha seleccionado ningún archivo para desencriptar.",fg="red4")

    elif (not os.path.exists(fileInput) and not os.path.isfile(fileInput)):
        mainResult.configure(text = 'Archivo seleccionado no existe o es inaccesible.',fg="red4")

    elif (not (".aes" in fileInput)):
        mainResult.configure(text = 'Archivo seleccionado no posee el formato adecuado (.aes).', fg="red4")

    else:
        
        resultFont = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)

        wind_decrypt = Toplevel(window)

        windowWidth = 350
        windowHeight = 200
        screenWidth = wind_decrypt.winfo_screenwidth()
        screenHeight = wind_decrypt.winfo_screenheight()
        # Gets both half the screen width/height and window width/height
        positionRight = (screenWidth/2) - (windowWidth/2)
        positionDown = (screenHeight/3) - (windowHeight/2)
        wind_decrypt.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,positionRight,positionDown))

        window.withdraw()
        wind_decrypt.title("Desencriptar")
        wind_decrypt.resizable(width=False, height=False)

        decryptPassword = StringVar()
        titleFont = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
        
        Label(wind_decrypt,bg='#003399',fg="white",text="",font=titleFont).pack(side=TOP, fill=BOTH, expand=0)

        topWind_decrypt = Frame(wind_decrypt)
        bottomWind_decrypt = Frame(wind_decrypt)

        Label(topWind_decrypt).grid(row=1, column = 0)

        Label(topWind_decrypt).grid(row=2, column = 0)
        Label(topWind_decrypt,text="Ingresa la contraseña:").grid(row=2, column = 1)
        Label(topWind_decrypt).grid(row=2, column = 2)

        Label(topWind_decrypt).grid(row=3, column = 0)
        Entry(topWind_decrypt, textvariable=decryptPassword,width=40,show='*').grid(row=3,column = 1)
        Label(topWind_decrypt).grid(row=3, column = 2)

        Label(topWind_decrypt).grid(row=4, column = 0)
        
        decryptLabel = Label(topWind_decrypt,text="", fg = "red4", font = resultFont)
        decryptLabel.grid(row=5, column = 1)

        Label(bottomWind_decrypt).grid(row=0, column = 0)
        Button(bottomWind_decrypt,text="Cancelar",width = "10",command= lambda: (window.deiconify(),wind_decrypt.destroy(),mainResult.configure(text = ""))).grid(row=1,column = 1)
        Label(bottomWind_decrypt).grid(row=0, column = 2)
        Button(bottomWind_decrypt,text="OK",width = "10",command= lambda:command_decrypt(decryptPassword.get(),wind_decrypt,window)).grid(row=1,column = 3)
        Label(bottomWind_decrypt).grid(row=0, column = 4)

        Label(bottomWind_decrypt).grid(row=1, column = 0)

        topWind_decrypt.pack(side=TOP, expand=0)
        bottomWind_decrypt.pack(side=BOTTOM, expand=1)

def command_encriptar(window):

    global cryptPassword
    global cryptLabel
    global confirmPassword

    fileInput = item_file.get()

    if(fileInput == ""):
        mainResult.configure(text = "No se ha seleccionado ningún archivo para encriptar.",fg="red4")

    elif (not os.path.exists(fileInput) and  not os.path.isfile(fileInput)):
        mainResult.configure(text = 'Archivo seleccionado no existe o es inaccesible.',fg="red4")

    else:
        
        resultFont = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)

        wind_crypt = Toplevel(window)

        windowWidth = 350
        windowHeight = 300
        screenWidth = wind_crypt.winfo_screenwidth()
        screenHeight = wind_crypt.winfo_screenheight()
        # Gets both half the screen width/height and window width/height
        positionRight = (screenWidth/2) - (windowWidth/2)
        positionDown = (screenHeight/3) - (windowHeight/2)
        wind_crypt.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,positionRight,positionDown))

        window.withdraw()

        wind_crypt.title("Encriptar")
        wind_crypt.resizable(width=False, height=False)

        cryptPassword = StringVar()
        confirmPassword = StringVar()
        titleFont = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)

        Label(wind_crypt,bg='#003399',fg="white",text="",font=titleFont).pack(side=TOP, fill=BOTH, expand=0)

        topWind_crypt = Frame(wind_crypt)
        bottomWind_crypt = Frame(wind_crypt)

        Label(topWind_crypt).grid(row=1, column = 0)

        Label(topWind_crypt).grid(row=2, column = 0)
        Label(topWind_crypt,text="Ingresa la contraseña:").grid(row=2, column = 1)
        Label(topWind_crypt).grid(row=2, column = 2)

        Label(topWind_crypt).grid(row=3, column = 0)
        Entry(topWind_crypt, textvariable=cryptPassword,width=40,show='*').grid(row=3,column = 1)
        Label(topWind_crypt).grid(row=3, column = 2)

        Label(topWind_crypt).grid(row=4, column = 2)
        
        Label(topWind_crypt).grid(row=5, column = 0)
        Label(topWind_crypt,text="Vuelve a ingresar la contraseña:").grid(row=5, column = 1)
        Label(topWind_crypt).grid(row=5, column = 2)

        Label(topWind_crypt).grid(row=6, column = 0)
        Entry(topWind_crypt, textvariable=confirmPassword,width=40,show='*').grid(row=6,column = 1)
        Label(topWind_crypt).grid(row=6, column = 2)

        Label(topWind_crypt).grid(row=7, column = 0)

        cryptLabel = Label(topWind_crypt,text="", fg = "red4", font = resultFont)
        cryptLabel.grid(row=8, column = 1)

        Label(bottomWind_crypt).grid(row=0, column = 0)
        Button(bottomWind_crypt,text="Cancelar",width = "10",command= lambda: (window.deiconify(),wind_crypt.destroy(),mainResult.configure(text = ""))).grid(row=1,column = 1)
        Label(bottomWind_crypt).grid(row=0, column = 2)
        Button(bottomWind_crypt,text="OK",width = "10",command= lambda:command_crypt(cryptPassword.get(),confirmPassword.get(),wind_crypt,window)).grid(row=1,column = 3)
        Label(bottomWind_crypt).grid(row=0, column = 4)

        Label(bottomWind_crypt).grid(row=1, column = 0)

        topWind_crypt.pack(side=TOP, expand=0)
        bottomWind_crypt.pack(side=BOTTOM, expand=1)

def command_decrypt(password,promt,window):
    
    decryptResult = decrypt.DecryptFile(item_file,password,64 * 1024)
    mainResult.configure(text = "")

    if (decryptResult):
        item_file.set("")
        mainResult.configure(text = "")
        messagebox.showinfo('Info',"Archivo desencriptado correctamente.")
        promt.destroy()
        window.deiconify()
    else:
        decryptLabel.configure(text = "Contraseña incorrecta.")
    

def command_crypt(password,password2,promt,window):

    mainResult.configure(text = "")
    if (password != password2):
        cryptLabel.configure(text ="Las contraseñas no coinciden entre sí.")
    elif (len(password) < 5):
        cryptLabel.configure(text ="La contraseña debe tener al menos 5 caracteres.")
    else:
        cryptResult = crypt.CryptFile(item_file,password,password2,64 * 1024)
        if (cryptResult):
            item_file.set("")
            mainResult.configure(text = "")
            messagebox.showinfo('Info',"Archivo encriptado correctamente.")
            promt.destroy()
            window.deiconify()
        else:
            cryptLabel.configure(text ="Error al encriptar el archivo.")
    

def main():


    global mainResult
    # Set Main Window
    window = Tk()

    windowWidth = 550
    windowHeight = 450
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = (screenWidth/2) - (windowWidth/2)
    positionDown = (screenHeight/3) - (windowHeight/2)

    window.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,positionRight,positionDown))
    # Positions the window in the center of the page.
    
    window.title("Encriptador de Archivos")

    window.resizable(width=False, height=False)

    inptu_dir = resource_path("input.txt")
    fileReco = open(inptu_dir,"r",encoding='utf-8')
    textReco = fileReco.read()

    titleFont = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
    defaultFont = tkFont.Font(family='Helvetica', size=8, weight=tkFont.BOLD)


    # Set frames
    frameTop1 = Frame(window)
    frameTop2 = Frame(window)
    frameCenter1 = Frame(window)
    frameCenter2 = Frame(window)
    frameBottom = Frame(window)

    frameTop1.config(background = '#003399')
    frameTop2.config()
    frameCenter1.config()
    frameCenter2.config()
    frameBottom.config(background = '#003399')
    
    # Frame Top 1
    Label(frameTop1,text="",font=titleFont,bg='#003399',fg="white").pack(side = TOP,expand=0)
    # Frame Top 2

    f = FilePathFrame(frameTop2)
    f.pack()

    # Frame Center1
    frameCenter1.columnconfigure(0,minsize=150)
    frameCenter1.columnconfigure(3,minsize=15)
    frameCenter1.columnconfigure(6,minsize=15)
    # ROW 0
    Label(frameCenter1).grid(row=0)
    # ROW 1
    Label(frameCenter1).grid(row=1)
    # ROW 2
    Label(frameCenter1).grid(row=2,column=0)
    Button(frameCenter1,text= "Encriptar",bg = "DarkSeaGreen2",width= 15,font=defaultFont, command=lambda :command_encriptar(window)).grid(row=2,column=2)
    Label(frameCenter1).grid(row=2,column=3)
    Button(frameCenter1,text= "Desencriptar",bg = "Wheat2",width= 15,font=defaultFont, command=lambda :command_desencriptar(window)).grid(row=2,column=4)
    Label(frameCenter1).grid(row=2,column=6)
    # ROW 3
    Label(frameCenter1).grid(row=3)

    # Frame Center 2

    mainResult = Label(frameCenter2,text="",bg="gray80",font=defaultFont)
    mainResult.pack(side = TOP, fill=BOTH, expand=1)
    Label(frameCenter2,text="").pack(side = TOP, fill=BOTH, expand=1)
    # Canvas
    textboxCanvas = Canvas(frameCenter2)
    textboxCanvas.pack(side = TOP,fill=NONE,expand=1)

    # Top Label
    Label(textboxCanvas,text= "Guía de uso:",font=defaultFont).pack(side = TOP,expand=0)

    # TextBox and Scrollbar
    scrollbar = Scrollbar(textboxCanvas)
    scrollbar.pack(side=RIGHT, fill=Y, expand=0)

    textbox = Text(textboxCanvas,width=60, height = 8,spacing1=2,spacing2=3,spacing3=1,wrap=WORD)
    textbox.pack(fill=BOTH, expand=1)
    textbox.insert(INSERT,textReco)


    textbox.config(yscrollcommand=scrollbar.set, state = "disabled")
    scrollbar.config(command=textbox.yview)

    Label(frameCenter2).pack(side = BOTTOM,expand=0)

    #Frame Bottom
    Label(frameBottom,text= "  Version 1.0  ",font=defaultFont,bg='#003399',fg="white").pack(side=RIGHT, expand=0)
    Label(frameBottom,text= " ",bg='#003399',fg="white",font=defaultFont).pack(side=LEFT, expand=0)
    #PACK FRAMES
    frameTop1.pack(side=TOP, fill=BOTH, expand=0)
    frameTop2.pack(side=TOP, fill=BOTH, expand=0)
    frameCenter1.pack(side=TOP, fill=BOTH, expand=1)
    frameCenter2.pack(side=TOP, fill=BOTH, expand=1)
    frameBottom.pack(side=BOTTOM, fill=BOTH, expand=0)
    window.mainloop()


