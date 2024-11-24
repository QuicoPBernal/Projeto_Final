import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont

def criar_interface(parent):
    # Frame para a tela de Gerenciamento de Recursos
    gestao_recursos_frame = tk.Frame(parent, bg='#282c34')  # Fundo escuro
    gestao_recursos_frame.pack(expand=True, fill="both")

    # Lista de recursos
    recursos = []  # Lista para armazenar os recursos
    recursos_listbox = tk.Listbox(gestao_recursos_frame, bg='#383c44', fg='#dcdcdc', highlightthickness=0, highlightbackground='#383c44', selectbackground='#424850')
    recursos_listbox.pack(pady=10)

    # Botões para adicionar, remover e editar recursos
    def adicionar_recurso():
        def adicionar_recurso_listbox(recursos, recursos_listbox, nome_recurso_entry):
            novo_recurso = nome_recurso_entry.get()
            recursos.append(novo_recurso)
            recursos_listbox.insert(tk.END, novo_recurso)
            nome_recurso_entry.delete(0, tk.END)  # Limpa o campo de entrada
            popup_window.destroy()  # Fecha a janela pop-up

        criar_janela_recurso(parent, recursos, recursos_listbox, "Adicionar Recurso", "Adicionar", adicionar_recurso_listbox)

    def remover_recurso():
        selection = recursos_listbox.curselection()
        if selection:
            index = selection[0]
            recursos.pop(index)
            recursos_listbox.delete(index)
        else:
            messagebox.showwarning("Aviso", "Selecione um recurso para remover.")

    def editar_recurso():
        selection = recursos_listbox.curselection()
        if selection:
            index = selection[0]
            recurso_atual = recursos[index]
            def editar_recurso_listbox(index, recursos, recursos_listbox, recurso_atual, nome_recurso_entry):
                recurso_atualizado = nome_recurso_entry.get()
                recursos[index] = recurso_atualizado
                recursos_listbox.delete(index)
                recursos_listbox.insert(index, recurso_atualizado)
                nome_recurso_entry.delete(0, tk.END)
                popup_window.destroy()

            criar_janela_recurso(parent, recursos, recursos_listbox, "Editar Recurso", "Salvar", lambda: editar_recurso_listbox(index, recursos, recursos_listbox, recurso_atual, nome_recurso_entry), pre_filled_value=recurso_atual)
        else:
            messagebox.showwarning("Aviso", "Selecione um recurso para editar.")

    adicionar_button = ttk.Button(gestao_recursos_frame, text="Adicionar", command=adicionar_recurso)
    adicionar_button.pack(pady=5)
    remover_button = ttk.Button(gestao_recursos_frame, text="Remover", command=remover_recurso)
    remover_button.pack(pady=5)
    editar_button = ttk.Button(gestao_recursos_frame, text="Editar", command=editar_recurso)
    editar_button.pack(pady=5)

def criar_janela_recurso(parent, recursos, recursos_listbox, title, button_text, submit_function, pre_filled_value=None):
    # Get main window size
    main_window_width = parent.winfo_width()
    main_window_height = parent.winfo_height()

    # Calculate pop-up window size
    popup_width = main_window_width // 2
    popup_height = main_window_height // 2

    global popup_window  # Declare popup_window as global to access it from inner functions
    popup_window = tk.Toplevel(parent)
    popup_window.title(title)
    popup_window.geometry(f"{popup_width}x{popup_height}")  # Set the geometry
    popup_window.configure(background='#282c34')  # Set background color

    nome_recurso_label = tk.Label(popup_window, text="Nome do Recurso:", bg='#282c34', fg='#dcdcdc')
    nome_recurso_label.pack()

    global nome_recurso_entry  # Declare nome_recurso_entry as global to access it from inner functions
    nome_recurso_entry = tk.Entry(popup_window, bg='#383c44', fg='#dcdcdc')
    nome_recurso_entry.pack()

    if pre_filled_value:
        nome_recurso_entry.insert(0, pre_filled_value)

    submit_button = ttk.Button(popup_window, text=button_text, command=lambda: submit_function(recursos, recursos_listbox, nome_recurso_entry))
    submit_button.pack()
