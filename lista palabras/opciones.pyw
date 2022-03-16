#========IMPORTS========
from io import open
from tkinter import *

#___________________________INTERFAZ FRÁFICA________________________
root = Tk()
root.title("lISTA DE PALABRAS")

word = StringVar()
translates = StringVar()

def campos():
    try:
        datos = word.get(),translates.get()
        archivo_texto = open("archivo.txt","a")
        archivo_texto.write('\n{}  \t {}'.format(datos[0],datos[1]))
        archivo_texto.close()
    except:
        pass
    limpiarCampos()

def limpiarCampos():
	word.set("")
	translates.set("")

miFrame = Frame(root, width=500,height=200)
miFrame.pack()
#___________________________________________
placeWordord = Entry(miFrame,textvariable=word)
placeWordord.grid(row=0,column=1,padx=10,pady=10)
wordLabel= Label(miFrame, text="WORD:")
wordLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
#___________________________________________
placeTraduction = Entry(miFrame,textvariable=translates)
placeTraduction.grid(row=2,column=1,padx=10,pady=10)
traductionLabel= Label(miFrame, text="TRADUCTION:")
traductionLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)
#___________________________________________
b1=Button(miFrame, text="ADD",bg="blue",command=campos)
b1.grid(row=3,column=1,padx=10,pady=10)
b1.config(width=15)
#___________________________________________________________________

#============CIERRE DEL ROOT============
root.mainloop() 