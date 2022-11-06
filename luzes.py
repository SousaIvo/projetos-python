# Importando Tkinter................................

from tkinter import *
import random

# Importando Pillow.................................

from PIL import Image, ImageTk

# Cores.............................................

cor0 = '#f0f3f5' # Cinza / grey
cor1 = '#feffff' # Branco / White
cor2 = '#3fb5a3' # Verde / Green
cor3 = '#38576b' # valor
cor4 = '#403d3b' # Preta / Black

# Criando Janela..................................... 

janela = Tk()
janela.title('Luzes')
janela.geometry('400x260')
janela.configure(background=cor1)
janela.resizable(False, False)

# Dividindo a janela em dois frames
# Frame cima............................................

frame_cima = Frame(janela, width=500, height=50, bg=cor2)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Frame baixo.............................................

frame_baixo = Frame(janela, width=400, height=210, bg=cor4 )
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame cima..................................

l_app = Label(frame_cima, text='Acenda as lâmpadas', anchor=NE, font=('Ivy 20 bold'), bg=cor2, fg=cor1)
l_app.place(x=5, y=5)

# Configurando frame baixo..................................

img_choro =  Image.open('images/choro.png')
img_choro = img_choro.resize((40, 40))
img_choro = ImageTk.PhotoImage(img_choro)

img_please =  Image.open('images/please.png')
img_please = img_please.resize((40, 40))
img_please = ImageTk.PhotoImage(img_please)

img_feliz =  Image.open('images/feliz.png')
img_feliz = img_feliz.resize((40, 40))
img_feliz = ImageTk.PhotoImage(img_feliz)

img_satisfeito =  Image.open('images/satisfeito.png')
img_satisfeito = img_satisfeito.resize((40, 40))
img_satisfeito = ImageTk.PhotoImage(img_satisfeito)

l_img = Label(frame_baixo, image=img_choro, bg=cor4, fg=cor1)
l_img.place(x=30, y=10)
l_estado = Label(frame_baixo, text='Estou com medo!', anchor=NW, font=('Ivy 13'), bg=cor4, fg=cor1)
l_estado.place(x=80, y=20)

global control

def ligar_lampada(i):
    global control
    lista = i

    # Desabilitando botão que foi clicado.................................
    if lista[1] == 'Interruptor-1':
        b_interruptor_1['state'] = 'disable'
    elif lista[1] == 'Interruptor-2':
        b_interruptor_2['state'] = 'disable'
    elif lista[1] == 'Interruptor-3':
        b_interruptor_3['state'] = 'disable'
    elif lista[1] == 'Interruptor-4':
        b_interruptor_4['state'] = 'disable'
    else:
        b_interruptor_5['state'] = 'disable'

    def substituir_valor(i):
        global control
        nova_lista = []
        for string in control:
            novo_valor = string.replace(i[0],i[1])
            nova_lista.append(novo_valor)
        control = nova_lista

    # Selecionar valor aleatoriamente.......................................

    valor_selecionado = random.sample(lista[0],1)[0]
    if int(valor_selecionado) == 1:
        if control[0] == 'lampada_1':
            l_img_1['image'] = img_luzon
            l_img['image'] = img_please
            l_estado['text'] = 'Ok, obrigado!'
            substituir_valor(['lampada_1',str(1)])
        else:
            if control[1] == 'lampada_2':
                l_img_2['image'] = img_luzon
                l_img['image'] = img_feliz
                l_estado['text'] = 'Por favor, acenda a ultima!'
                substituir_valor(['lampada_2',str(2)])
            else:
                if control[2] == 'lampada_3':
                    l_img_3['image'] = img_luzon
                    l_img['image'] = img_satisfeito
                    l_estado['text'] = 'Muito obrigado!!!'
                    substituir_valor(['lampada_3',str(3)])

    
control = ['lampada_1', 'lampada_2', 'lampada_3']

img_luzon =  Image.open('images/luzon.png')
img_luzon = img_luzon.resize((110, 110))
img_luzon = ImageTk.PhotoImage(img_luzon)

img_luzoff =  Image.open('images/luzoff.png')
img_luzoff = img_luzoff.resize((110, 110))
img_luzoff = ImageTk.PhotoImage(img_luzoff)

l_img_1 = Label(frame_baixo, image=img_luzoff, bg=cor4)
l_img_1.place(x=5, y=70)

l_img_2 = Label(frame_baixo, image=img_luzoff, bg=cor4)
l_img_2.place(x=105, y=70)

l_img_3 = Label(frame_baixo, image=img_luzoff, bg=cor4)
l_img_3.place(x=205, y=70)

lista = [0,1,0,1,0]

b_interruptor_1 = Button(frame_baixo, command=lambda i=[lista,'Interruptor-1']:ligar_lampada(i), text='Interruptor-1', anchor=NW, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1)
b_interruptor_1.place(x=300, y=50)

b_interruptor_2 = Button(frame_baixo, command=lambda i=[lista,'Interruptor-2']:ligar_lampada(i), text='Interruptor-2', anchor=NW, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1)
b_interruptor_2 .place(x=300, y=80)

b_interruptor_3 = Button(frame_baixo, command=lambda i=[lista,'Interruptor-3']:ligar_lampada(i), text='Interruptor-3', anchor=NW, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1)
b_interruptor_3.place(x=300, y=110)

b_interruptor_4 = Button(frame_baixo, command=lambda i=[lista,'Interruptor-4']:ligar_lampada(i), text='Interruptor-4', anchor=NW, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1)
b_interruptor_4.place(x=300, y=140)

b_interruptor_5 = Button(frame_baixo, command=lambda i=[lista,'Interruptor-5']:ligar_lampada(i), text='Interruptor-5', anchor=NW, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE, bg=cor4, fg=cor1)
b_interruptor_5.place(x=300, y=170)


janela.mainloop()