import pyautogui as pg
import webbrowser
from time import sleep
import tkinter as tk

def check_class(quantity_class):
    while quantity_class > 0:
        for i in range(1,19):
            pg.hotkey('tab')
            
        pg.hotkey('enter')
        quantity_class -= 1
        sleep(10)
        
def begin(url, quantity):
    webbrowser.open(url)
    sleep(10)
    check_class(quantity)
    
root = tk.Tk()
root.title = 'Bot para marcar as aulas ONE BIT CODE'
root.geometry('500x400')

label = tk.Label(root, text="Link da primeira aula do curso que deseja marcar aulas como concluidas")
label.pack()

input = tk.Entry(root)
input.pack()

labelQtd = tk.Label(root, text='Digite a quantidade de aulas que serão concluídas')
labelQtd.pack()

inputQtd = tk.Entry(root)
inputQtd.pack()

button = tk.Button(root, text="Iniciar", command=lambda: begin(input.get(), int(inputQtd.get())))
button.pack()

root.mainloop()