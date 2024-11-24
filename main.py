import tkinter as tk
from tkinter import ttk
import controle_acesso
import gestao_recursos
import dashboard


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Segurança - Indústrias Wayne")

        # Estilos para tema escuro
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('.', background='#282c34', foreground='#2b020c')
        style.configure('TButton', background='#424850', foreground='#2b020c')
        style.configure('TEntry', background='#383c44', foreground='#2b020c', fieldbackground='#383c44')
        style.configure('TLabel', background='#282c34', foreground='#2b020c')

        # Configurar estilo da aba (TNotebook)
        style.configure('TNotebook.Tab', background='#2b020c', foreground='#2b020c', padding=[10, 5])
        style.configure('TNotebook.Tab', borderwidth=0, highlightthickness=0)  # Remover bordas das abas

        # Menu
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        # Abas
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Tela de Controle de Acesso
        controle_acesso_frame = tk.Frame(notebook)
        controle_acesso.criar_interface(controle_acesso_frame)
        notebook.add(controle_acesso_frame, text="Controle de Acesso")

        # Tela de Gerenciamento de Recursos
        gestao_recursos_frame = tk.Frame(notebook)
        gestao_recursos.criar_interface(gestao_recursos_frame)
        notebook.add(gestao_recursos_frame, text="Gerenciamento de Recursos")

        # Tela de Dashboard
        dashboard_frame = tk.Frame(notebook)
        dashboard.criar_interface(dashboard_frame)
        notebook.add(dashboard_frame, text="Dashboard")

        self.config(menu=menubar)

        # Tamanho da janela
        self.geometry("900x450")

        # Definir o background da janela principal
        self.configure(background='#282c34')


if __name__ == "__main__":
    app = App()
    app.mainloop()
