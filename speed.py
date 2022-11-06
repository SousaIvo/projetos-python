# Importando Tkinter
from tkinter import *

#importando o pillow

from PIL import Image, ImageTk

# Cores

cor0 = '#f0f3f5' # Preto /  Black
cor1 = '#feffff' # Branca / White
cor2 = '#3fb5a3' # Verde / Green
cor3 = '#fc766d' # Vermelho / Red
cor4 = '#403d3d' # Letra
cor5 = '#4a88e8' # Azul / Blue

# Criando Janela

janela = Tk()
janela.title('Speed')
janela.geometry('350x200')
janela.configure(background=cor0)
janela.resizable(False, False)

# Divindo a Janela em dois frames

frame_logo = Frame(janela, width=350, height=60, bg=cor1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
 
frame_corpo = Frame(janela, width=350, height=140, bg=cor1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando o frame_Logo

imagem = Image.open('images/speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 20 bold'), bg=cor1, fg=cor3)
l_logo_imagem.place(x=20, y=0)

l_logo_nome = Label(frame_logo, text='Internet speed test', height=60, padx=10, anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
l_logo_nome.place(x=70, y=10)

l_logo_nome = Label(frame_logo, width=350, anchor=NW, font=('Ivy 1 bold'), bg=cor2)
l_logo_nome.place(x=0, y=57)

# Configurando o frame_corpo
# Download
l_download = Label(frame_corpo, text='65.7', anchor=NW, font=('arial 28'), bg=cor1, fg=cor4)
l_download.place(x=44, y=25)
l_download = Label(frame_corpo, text='Mbps download', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_download.place(x=30, y=70)

imagem_down = Image.open('images/down.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)

l_logo_imagem = Label(frame_corpo, height=60, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 20 bold'), bg=cor1, fg=cor3)
l_logo_imagem.place(x=130, y=35)

# Upload
l_upload = Label(frame_corpo, text='65.7', anchor=NW, font=('arial 28'), bg=cor1, fg=cor4)
l_upload.place(x=235, y=25)
l_upload = Label(frame_corpo, text='Mbps upload', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_upload.place(x=230, y=70)

imagem_up = Image.open('images/up.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)

l_logo_imagem = Label(frame_corpo, height=60, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 20 bold'), bg=cor1, fg=cor3)
l_logo_imagem.place(x=170, y=35)

botao_testar = Button(frame_corpo, text='Iniciar teste', font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor5, fg=cor1)
botao_testar.place(x=135, y=100)

janela.mainloop()