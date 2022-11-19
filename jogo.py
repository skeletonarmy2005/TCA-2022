import tkinter
from tkinter import *
from tkinter import ttk

# cores -------------
co0 = "#FFFFFF" # white
co1 = "#333333" # branca
co2 = "#fcc058" # orange
co3 = "#38576b" # valor
co4 = "#3297a8" # blue
co5 = "#fff873" # yellow
co6 = "#fcc058" # orange
co7 = "#e85151" # vermelha
co8 = "#34eb3d" # + verde
fundo = "#3b3b3b"


# configuração janela------
janela = tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)


# divisão janela------

frame_cima = frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo = frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.style(janela)
estilo.the_use('clam')

# configuração frame cima

app_1 = label(frame_cima, text="voce", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1.place(x=50, y=20)

app_ = label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)



app_2_pontos = label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2.place(x=170, y=20)
app_2 = label(frame_cima, text="computador", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = label(frame_cima, text="", widht=255 anchor='center', font=('Ivy 1 bold'), bg=co1, fg=co0)
app_linha.place(x=0, y=95)



janela.mainloop()
