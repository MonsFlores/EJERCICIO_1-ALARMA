from tkinter import*
import time
from tkinter import ttk
import pygame
from pygame.locals import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog



pygame.init()

root = Tk()
root.geometry("375x370")
root.title("ALARMA")
root.config(bg="#008080")
root.iconbitmap("relojsi.ico")


def AbrirArchivo():
    cancion= filedialog.askopenfilename() 
    print(cancion)
    pygame.mixer.music.load(cancion)
    
def Musica():
	pygame.mixer.music.play()
    

def clock():

	hora =  time.strftime('%H')
	minutos = time.strftime('%M')

	segundos = time.strftime('%S')

	horaActual = (hora + ' : '+ minutos+ ' : '+ segundos)
	textoHora.config(text=horaActual, font = ("TimesNewRoman", 20))

	hrs = combobox1.get()
	minu = combobox2.get()
	horaAlarma = hrs +' : '+ minu +' : '+ '00'
	
	alarma['text']= horaAlarma


	if int(hora) == int(hrs):
		if int(minutos) == int(minu):
			Musica()
			

	textoHora.after(1000, clock)

def guardaralarma():
	hrs = combobox1.get()
	minu = combobox2.get()
	horaAlarma = hrs +' : '+ minu +' : '+ '00'
	alarma['text']= horaAlarma
	MessageBox.showinfo(message=f'Alarma programada {horaAlarma}', title="Alarma")

def detenerAlarma():
    MessageBox.showinfo("ALARMA", "ALARMA DETENIDA")
    pygame.mixer.music.stop()
    root.destroy()

    
lista_horas = []
lista_minutos = []


for  i in range(0,24):
	lista_horas.append(i)
for  i in range(0,60):
	lista_minutos.append(i)


#------------------------------------------------------------------------------------------------------#
titulo = Label(root, text="ALARMA", font=("TimesNewRoman",18,"bold"), bg="#008080", fg="#fff")
titulo.grid(row=1,column=1, rowspan=2, columnspan=4)


titulo2 = Label(root, text="H:", font=("TimesNewRoman",18,"bold"), bg="#008080", fg="#fff")
titulo2.grid(row=9,column=1,)


titulo3 = Label(root, text="M:", font=("TimesNewRoman",18,"bold"), bg="#008080", fg="#fff")
titulo3.grid(row=11,column=1)


alarma = Label(root,  bg="#008080", fg="#fff", font = ('TimesNewRoman', 20))
alarma.grid(row=17, column=2)

titulo4=Label(root, font=("TimesNewRoman",18,"bold"), bg="#008080", fg="#fff", text="HORA")
titulo4.grid(row=13,column=1)

titulo5=Label(root, font=("TimesNewRoman",18,"bold"), bg="#008080", fg="#fff", text="ALARMA: ")
titulo5.grid(row=17,column=1)
#----------------------------------------------------------------------------------------------------------#

combobox1 = ttk.Combobox(root, values = lista_horas, justify='center',width='12', font=("TimesNewRoman",15))
combobox1.grid(row=9, column=2)
combobox1.current(0)
combobox2 = ttk.Combobox(root, values = lista_minutos, justify='center',width='12', font=("TimesNewRoman",15))
combobox2.grid(row=11, column=2)
combobox2.current(0)

#----------------------------------------------------------------------------------------------------------#


textoHora = Label(root,  bg="#008080", fg="#fff",)
textoHora.grid(row=13,column=2)


#----------------------------------------------------------------------------------------------------------#
boton1= Button(root, text="Guardar alarma", bg="#0000FF", fg="#fff", font=("TimesNewRoman", 12, "bold"), width=15, height=2, command=guardaralarma)
boton1.grid(row=15,column=1)

boton2= Button(root, text="Seleccionar sonido", bg="#0000FF", fg="#fff", font=("TimesNewRoman", 12, "bold"), width=15, height=1, command=AbrirArchivo)
boton2.grid(row=20,column=1)


boton3 = Button(root, text="Detener alarma",bg="#0000FF", fg="#fff", font=("TimesNewRoman",12, "bold") , command=detenerAlarma).grid(row=25, column=1)
#----------------------------------------------------------------------------------------------------------#

clock()
root.mainloop()