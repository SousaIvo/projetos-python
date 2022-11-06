
import tkinter
from tkinter import *
from tkinter import ttk

# Importando o Pillow

from PIL import Image, ImageTk

import random

# cores ....................................
cor0 = '#ffffff'  # white
cor1 = '#333333'  # branca
cor2 = '#fcc058'  # laranja
cor3 = '#38576b'  # valor
cor4 = '#3297a8'  # Azul
cor5 = '#fff873'  # Amarelo
cor6 = '#fcc058'  #Laranja
cor7 = '#e85151'  # Vermelho
cor8 = '#34eb3d'  # Verde
fundo = '#3b3b3b'

# Configurando a Janela
janela = Tk()
janela.title('Game')
janela.geometry('260x280')
janela.configure(bg=fundo)
janela.resizable(False, False)


# Dividindo a Janela
frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando o frame cima
app_1 = Label(frame_cima, text='Voce', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0 )
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0 )
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0 )
app_1_pontos.place(x=50, y=20)


app_ = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0 )
app_.place(x=125, y=20)


app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0 )
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0 )
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0 )
app_2_linha.place(x=255, y=0)


app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'), bg=cor0, fg=cor0 )
app_linha.place(x=0, y=95)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor0 )
app_pc.place(x=190, y=10)


# Variaveis globais

global voce 
global pc 
global rodadas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
rodadas = 5

# Função lógica do jogo
def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_pc

    if rodadas > 0:
        print(rodadas)
        opçoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opçoes)
        voce = i 

        app_pc['text'] = pc
        app_pc['fg'] = cor1
       
        # caso for igual
        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor5

        elif voce == 'Papel' and pc == 'Papel':
             print('Empate')
             app_1_linha['bg'] = cor0
             app_2_linha['bg'] = cor0
             app_linha['bg'] = cor5
        
        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor5

            # Caso vitoria [você/pc]
        elif voce == 'Pedra' and pc == 'Papel':
            print('PC Ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_pc += 10
        
        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Você Ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_voce += 10
        
        elif voce == 'Papel' and pc == 'Pedra':
            print('Você Ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_voce += 10
        
        elif voce == 'Papel' and pc == 'Tesoura':
            print('PC Ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_pc += 10
        
        elif voce == 'Tesoura' and pc == 'Papel':
            print('Você Ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_voce += 10
        
        elif voce == 'Tesoura' and pc == 'Pedra':
            print('PC Ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_pc += 10

        # Atualizando a Pontuação
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # Atualizando número de Rodadas
        rodadas -= 1
    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # Chamando a Função fim de jogo

        fim_do_jogo()

# Função iniciar o jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT, overrelief=RIDGE)
    b_icon_1.place(x=15, y=60)


    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT, overrelief=RIDGE)
    b_icon_2.place(x=95, y=60)


    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=cor0, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT, overrelief=RIDGE)
    b_icon_3.place(x=170, y=60)

# Função terminar o jogo
def fim_do_jogo():
    global rodadas
    global pontos_voce
    global pontos_pc

    # Reiniciando as variaveis para zero
    pontos_voce = 0
    pontos_pc = 0
    rodadas = 5

    # Destruindo os botões de opções
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # Definindo o vencedor
    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text='Parabéns você venceu!!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor8 )
        app_vencedor.place(x=5, y=60)
    elif jogador_voce < jogador_pc:
        app_vencedor = Label(frame_baixo, text='Infelizmente você perdeu!!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor7 )
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text='EMPATOU!!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1 )
        app_vencedor.place(x=5, y=60)

     # Jogar novamente
    def jogar_novamente():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()
        b_jogar_novamente.destroy()

        iniciar_jogo()

    b_jogar_novamente = Button(frame_baixo, command=jogar_novamente, width=30, text='Jogar novamente', bg=fundo, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_novamente.place(x=5, y=151)


b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=cor0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


janela.mainloop()