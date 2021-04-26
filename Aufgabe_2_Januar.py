from tkinter import *

# Erzeugung des Fensters
root = Tk()
root.title('Kalender')
root.geometry('130x145')

# Label für die Anzeige der Daten
labelMonat = Label(root, text='Januar', font=('Arial', 10))
labelMonat.place(x=5, y=5, width=60, height=20)
labelWoche = Label(root, text='4. Woche',font=('Arial', 10))
labelWoche.place(x=60, y=5, width=60, height=20)
labelTag = Label(root, text='21', fg='red', bg='#FFCFC9', font=('Arial', 72))
labelTag.place(x=5, y=30, width=120, height=80)
labelWochentag = Label(root, text='Montag')
labelWochentag.place(x=35, y=115, width=60, height=30)

# Aktivierung des Fensters
root.mainloop()
