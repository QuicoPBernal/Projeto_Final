import tkinter as tk
from tkinter import ttk, messagebox

def criar_interface(parent):
    # Frame para a tela de Controle de Acesso
    controle_acesso_frame = tk.Frame(parent, bg='#282c34')
    controle_acesso_frame.pack(expand=True, fill="both")

    # Estilos para tema escuro
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('.', background='#282c34', foreground='#dcdcdc')
    style.configure('TButton', background='#424850', foreground='#dcdcdc')
    style.configure('TEntry', background='#383c44', foreground='#dcdcdc', fieldbackground='#383c44')
    style.configure('TLabel', background='#282c34', foreground='#dcdcdc')

    # Label e Entry para o nome de usuário
    nome_usuario_label = tk.Label(controle_acesso_frame, text="Nome de Usuário:", background='#282c34', foreground='#dcdcdc')
    nome_usuario_label.pack()
    nome_usuario_entry = tk.Entry(controle_acesso_frame, background='#383c44', foreground='#dcdcdc')
    nome_usuario_entry.pack()

    # Label e Entry para a senha
    senha_label = tk.Label(controle_acesso_frame, text="Senha:", background='#282c34', foreground='#dcdcdc')
    senha_label.pack()
    senha_entry = tk.Entry(controle_acesso_frame, show="*", background='#383c44', foreground='#dcdcdc')
    senha_entry.pack()

    # Botão para login
    def login():
        nome_usuario = nome_usuario_entry.get()
        senha = senha_entry.get()
        print(f"Username: {nome_usuario}, Password: {senha}")

        # Verificar se o usuário existe e se a senha está correta
        if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
            # Verificar se o usuário tem acesso à tela
            if nome_usuario in acessos and "controle_acesso" in acessos[nome_usuario]:
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
                # Clear the entry fields
                nome_usuario_entry.delete(0, tk.END)
                senha_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Você não tem permissão para acessar esta tela.")
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha inválidos!")

    # Usuários e senhas
    usuarios = {
        "admin": "admin123",
        "Bruno": "1234",
        "Ana": "logicamente",
        "Carlos": "secure"
    }
    # Permissões de acesso
    acessos = {
        "admin": ["controle_acesso", "gestao_recursos", "dashboard"],
        "Bruno": ["controle_acesso", "gestao_recursos", "dashboard"],
        "Ana": ["controle_acesso","dashboard"],
        "Carlos": ["controle_acesso", "dashboard"]
    }

    login_button = ttk.Button(controle_acesso_frame, text="Login", command=login)
    login_button.pack()
