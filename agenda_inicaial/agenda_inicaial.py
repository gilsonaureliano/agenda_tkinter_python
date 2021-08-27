from tkinter import *
import ctypes
ctypes.windll.kernel32.FreeConsole()



def novoContato():
    app1 = Tk()
    app1.title('Cadastro  Novo')
    app1.geometry("500x450+570+50")
    app1.configure(background='#dde')
    app1.iconbitmap('cadastro_novo.ico')

    # anchor => N=norte, S=sul, E=leste, W=oeste
    # NE= nordeste, SE=sudeste, SO=sudoeste, NO=noroeste
    Label(app1, text='CPF', background='#dde', foreground='#009', anchor='w').place(x=10, y=10, width=100)

    # vcmd = app1.register(func=validar_numero.tam_CPF)  # limita a quantidade de numeros do CPF
    # tb_CPF = Entry(app1, validate='key', validatecommand=(vcmd, '%P'))  # entrar com um box simples texto
    tb_CPF = Entry(app1)  # entrar com um box simples texto
    tb_CPF.place(x=10, y=30, width=80, height=20)

    Label(app1, text='Nome', background='#dde', foreground='#009', anchor='w').place(x=10, y=60, width=100)
    tb_nome = Entry(app1)  # entrar com um box simples texto
    tb_nome.place(x=10, y=80, width=200, height=20)

    Label(app1, text='Telefone', background='#dde', foreground='#009', anchor='w').place(x=10, y=110, width=100)
    tb_fone = Entry(app1)  # entrar com um box simples texto
    tb_fone.place(x=10, y=130, width=100, height=20)

    Label(app1, text='E-mail', background='#dde', foreground='#009', anchor='w').place(x=10, y=160, width=100)
    tb_email = Entry(app1)  # entrar com um box simples texto
    tb_email.place(x=10, y=180, width=200, height=20)

    Label(app1, text='Observacoes:', background='#dde', foreground='#009', anchor='w').place(x=10, y=210, width=100)
    tb_obs = Text(app1)  # entrar com um box multiplo texto
    tb_obs.place(x=10, y=240, width=200, height=80)

    btn1 = Button(app1, text='Gravar', font='arial 12', background='#00FA9A')
    btn1.place(x=10, y=410, width=100, height=30)

    app1.mainloop()


def pesquisar():
    app2 = Tk()
    app2.title('Consultar Cadastro')
    app2.geometry('500x450+570+50')
    app2.configure(background='#dde')
    app2.iconbitmap('lupa.ico')

    # anchor => N=norte, S=sul, E=leste, W=oeste
    # NE= nordeste, SE=sudeste, SO=sudoeste, NO=noroeste

    Label(app2, text='CPF - consulta', background='#dde', foreground='#009', anchor='w').place(x=10, y=10, width=200)

    # vcmd = app2.register(func=validar_numero.tam_CPF)  # limita a quantidade de numeros do CPF
    tb_VERCPF = Entry(app2)  # entrar com um box simples texto
    tb_VERCPF.place(x=10, y=30, width=80, height=20)

    Label(app2, text='CPF', background='#dde', foreground='#009', anchor='w').place(x=10, y=60, width=100)

    tb_CPF = Entry(app2, background='#dde')  # entrar com um box simples texto
    tb_CPF.place(x=10, y=80, width=200, height=20)

    Label(app2, text='Nome', background='#dde', foreground='#009', anchor='w').place(x=10, y=110, width=100)
    tb_nome = Entry(app2, background='#dde')  # entrar com um box simples texto
    tb_nome.place(x=10, y=130, width=200, height=20)

    Label(app2, text='Telefone', background='#dde', foreground='#009', anchor='w').place(x=10, y=160, width=100)
    tb_fone = Entry(app2, background='#dde')  # entrar com um box simples texto
    tb_fone.place(x=10, y=180, width=100, height=20)

    Label(app2, text='E-mail', background='#dde', foreground='#009', anchor='w').place(x=10, y=210, width=100)
    tb_email = Entry(app2, background='#dde')  # entrar com um box simples texto
    tb_email.place(x=10, y=230, width=200, height=20)

    Label(app2, text='Observacoes:', background='#dde', foreground='#009', anchor='w').place(x=10, y=260, width=100)
    tb_obs = Text(app2, background='#dde')  # entrar com um box multiplo texto
    tb_obs.place(x=10, y=280, width=200, height=80)

    # --------------------------------------------------------------------------------------------------------

    btn = Button(app2, text='CONSULTAR', font='arial 10', background='#FFDAB9')
    btn.place(x=180, y=30, width=100, height=20)

    btn = Button(app2, text='NOME CONSULTA', font='arial 10', background='#E6E6FA')
    btn.place(x=300, y=30, width=180, height=20)

    app2.mainloop()


def deletar():
    app4 = Tk()
    app4.title('DELETAR')
    app4.geometry('500x450+570+50')
    app4.configure(background='#dde')
    app4.iconbitmap('deletar.ico')

    # anchor => N=norte, S=sul, E=leste, W=oeste
    # NE= nordeste, SE=sudeste, SO=sudoeste, NO=noroeste

    Label(app4, text='CPF - consulta', background='#dde', foreground='#009', anchor='w').place(x=10, y=10, width=200)

    # vcmd = app4.register(func=validar_numero.tam_CPF)  # limita a quantidade de numeros do CPF
    tb_VERCPF = Entry(app4)  # entrar com um box simples texto
    tb_VERCPF.place(x=10, y=30, width=80, height=20)

    Label(app4, text='CPF', background='#dde', foreground='#009', anchor='w').place(x=10, y=60, width=100)

    tb_CPF = Entry(app4, background='#dde')  # entrar com um box simples texto
    tb_CPF.place(x=10, y=80, width=200, height=20)

    Label(app4, text='Nome', background='#dde', foreground='#009', anchor='w').place(x=10, y=110, width=100)
    tb_nome = Entry(app4, background='#dde')  # entrar com um box simples texto
    tb_nome.place(x=10, y=130, width=200, height=20)

    Label(app4, text='Telefone', background='#dde', foreground='#009', anchor='w').place(x=10, y=160, width=100)
    tb_fone = Entry(app4, background='#dde')  # entrar com um box simples texto
    tb_fone.place(x=10, y=180, width=100, height=20)

    Label(app4, text='E-mail', background='#dde', foreground='#009', anchor='w').place(x=10, y=210, width=100)
    tb_email = Entry(app4, background='#dde')  # entrar com um box simples texto
    tb_email.place(x=10, y=230, width=200, height=20)

    Label(app4, text='Observacoes:', background='#dde', foreground='#009', anchor='w').place(x=10, y=260, width=100)
    tb_obs = Text(app4, background='#dde')  # entrar com um box multiplo texto
    tb_obs.place(x=10, y=280, width=200, height=80)

    # --------------------------------------------------------------------------------------------------------

    btn = Button(app4, text='CONSULTAR', font='arial 10', background='#FFDAB9')
    btn.place(x=220, y=30, width=100, height=20)

    btn = Button(app4, text='DELETAR', font='arial 12', background='#ff0000', foreground='#009')
    btn.place(x=260, y=400, width=100, height=30)

    app4.mainloop()


def alterar():
    app3 = Tk()
    app3.title('Alterar Cadastro')
    app3.geometry('500x450+570+50')
    app3.configure(background='#dde')
    app3.iconbitmap('favicon.ico')

    # anchor => N=norte, S=sul, E=leste, W=oeste
    # NE= nordeste, SE=sudeste, SO=sudoeste, NO=noroeste

    Label(app3, text='CPF - consulta', background='#dde', foreground='#009', anchor='w').place(x=10, y=10, width=200)

    # vcmd = app3.register(func=validar_numero.tam_CPF)  # limita a quantidade de numeros do CPF
    tb_VERCPF = Entry(app3)  # entrar com um box simples texto
    tb_VERCPF.place(x=10, y=30, width=80, height=20)

    Label(app3, text='CPF', background='#dde', foreground='#009', anchor='w').place(x=10, y=60, width=100)

    tb_CPF = Entry(app3)  # entrar com um box simples texto
    tb_CPF.place(x=10, y=80, width=200, height=20)

    Label(app3, text='Nome', background='#dde', foreground='#009', anchor='w').place(x=10, y=110, width=100)
    tb_nome = Entry(app3)  # entrar com um box simples texto
    tb_nome.place(x=10, y=130, width=200, height=20)

    Label(app3, text='Telefone', background='#dde', foreground='#009', anchor='w').place(x=10, y=160, width=100)
    tb_fone = Entry(app3)  # entrar com um box simples texto
    tb_fone.place(x=10, y=180, width=100, height=20)

    Label(app3, text='E-mail', background='#dde', foreground='#009', anchor='w').place(x=10, y=210, width=100)
    tb_email = Entry(app3)  # entrar com um box simples texto
    tb_email.place(x=10, y=230, width=200, height=20)

    Label(app3, text='Observacoes:', background='#dde', foreground='#009', anchor='w').place(x=10, y=260, width=100)
    tb_obs = Text(app3)  # entrar com um box multiplo texto
    tb_obs.place(x=10, y=280, width=200, height=80)

    btn = Button(app3, text='ALTERAR CADASTRO', font='arial 10', background='#FFFF00')
    btn.place(x=130, y=370, width=200, height=40)

    # --------------------------------------------------------------------------------------------------------

    btn = Button(app3, text='CONSULTAR', font='arial 10', background='#6495ED')
    btn.place(x=220, y=30, width=100, height=20)

    app3.mainloop()


# ------------------------------------------------------------------------------------------------------


app = Tk()
app.title('Agenda')
app.geometry('500x350+50+50')
app.configure(background='#dde')
app.iconbitmap('favicon.ico')

barraDeMenu = Menu(app)  # abaixo itens do menu
menuContatos = Menu(barraDeMenu, tearoff=0)
menuContatos.add_command(label="Novo", command=novoContato)
menuContatos.add_command(label="Pesquisar", command=pesquisar)
menuContatos.add_command(label="Alterar", command=alterar)
menuContatos.add_command(label="Deletar", command=deletar)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)

barraDeMenu.add_cascade(label='Contatos', menu=menuContatos)
app.configure(menu=barraDeMenu)

img = PhotoImage(file='agenda2_0.png')
label_imagem = Label(app, image=img)

btn = Button(app, text='Novo', font='arial 10', background='#00FA9A', command=novoContato)
btn.place(x=290, y=70, width=100, height=20)

btn = Button(app, text='Pesquisar', font='arial 10', background='#87CEFA', command=pesquisar)
btn.place(x=290, y=130, width=100, height=20)

btn = Button(app, text='Alterar', font='arial 10', background='#FFFF00', command=alterar)
btn.place(x=290, y=190, width=100, height=20)

btn = Button(app, text='Deletar', font='arial 10', background='#FF6347', command=deletar)
btn.place(x=290, y=250, width=100, height=20)

label_imagem.pack()

app.mainloop()
