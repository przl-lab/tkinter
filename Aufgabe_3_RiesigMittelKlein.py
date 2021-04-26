from tkinter import *

# Erzeugung des Fensters
root = Tk()
root.geometry('360x150')

# Label für die Anzeige der Daten
labelRiesig = Label(root, text='riesig', font=('Arial', 38))
labelRiesig.place(x=5, y=5, width=350, height=60)
labelMittel = Label(root, text='mittel', font=('Arial', 18))
labelMittel.place(x=5, y=80, width=350, height=20)
labelKlein = Label(root, text='klein', font=('Arial', 9))
labelKlein.place(x=5, y=110, width=350, height=20)

# Aktivierung des Fensters
root.mainloop()
