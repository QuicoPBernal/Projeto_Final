import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def criar_interface(parent):
    # Configurar estilo escuro
    style = ttk.Style()
    style.theme_use('clam')  # Escolhendo um tema que permite personalizar cores
    style.configure('.', background='#282c34', foreground='#dcdcdc')  # Cor de fundo e fonte padrão
    style.configure('TButton', background='#424850', foreground='#dcdcdc')  # Cor dos botões
    style.configure('TEntry', background='#383c44', foreground='#dcdcdc', fieldbackground='#383c44')  # Cor das entradas de texto
    style.configure('TLabel', background='#282c34', foreground='#dcdcdc')  # Cor das labels

    # Frame para a tela de Dashboard
    dashboard_frame = tk.Frame(parent, bg='#282c34')  # Fundo escuro
    dashboard_frame.pack(expand=True, fill="both")

    # Labels para exibir informações do dashboard
    label1 = tk.Label(dashboard_frame, text="Dashboard - Indústrias Wayne", bg='#282c34', fg='#dcdcdc')
    label1.pack(pady=10)
    label2 = tk.Label(dashboard_frame, text="Número de Usuários: 4", bg='#282c34', fg='#dcdcdc')
    label2.pack(pady=5)
    label3 = tk.Label(dashboard_frame, text="Número de Recursos: 0", bg='#282c34', fg='#dcdcdc')
    label3.pack(pady=5)
    label4 = tk.Label(dashboard_frame, text="Eventos de Acesso Recentes:", bg='#282c34', fg='#dcdcdc')
    label4.pack(pady=5)

    # Lista de eventos de acesso recentes
    eventos_listbox = tk.Listbox(dashboard_frame, bg='#383c44', fg='#dcdcdc', highlightthickness=0, highlightbackground='#383c44', selectbackground='#424850')
    eventos_listbox.pack(pady=10)

    # Placeholder data for now (in a real application, this would come from your data source)
    acessos_funcionarios = {
        "Bruno": 5,  # Number of accesses
        "Ana": 3,
        "Carlos": 7
    }
    recursos_adicionados = {
        "Semana 1": 10,
        "Semana 2": 15,
        "Semana 3": 8
    }
    recursos_excluidos = {
        "Semana 1": 2,
        "Semana 2": 1,
        "Semana 3": 3
    }

    # Create a figure and axes
    fig, ax1 = plt.subplots(figsize=(6, 3))

    # Accesses Chart
    ax1.bar(acessos_funcionarios.keys(), acessos_funcionarios.values())
    ax1.set_xlabel("Funcionários")
    ax1.set_ylabel("Número de Acessos")
    ax1.set_title("Acessos de Funcionários")

    # Create a second axes for the resource charts
    ax2 = ax1.twinx()

    # Resources Added Chart
    ax2.plot(recursos_adicionados.keys(), recursos_adicionados.values(), color="red", label="Recursos Adicionados")
    ax2.set_ylabel("Recursos Adicionados")

    # Resources Removed Chart
    ax2.plot(recursos_excluidos.keys(), recursos_excluidos.values(), color="blue", label="Recursos Excluídos")
    ax2.set_ylabel("Recursos Excluídos")

    # Legend
    plt.legend(loc='upper left')

    # Create a canvas for the figure
    canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(pady=20)

    # Aqui você deve implementar a lógica para atualizar as informações do dashboard
    # Consultar o banco de dados para obter os dados necessários
    # Atualizar as labels e a lista de eventos
