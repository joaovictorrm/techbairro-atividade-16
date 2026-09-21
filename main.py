# Importa a biblioteca Tkinter e cria o apelido "tk"
# O Tkinter é utilizado para criar interfaces gráficas em Python
import tkinter as tk


# ============================================================
# JANELA PRINCIPAL
# ============================================================

# Cria a janela principal da aplicação
janela = tk.Tk()

# Define o título exibido na parte superior da janela
janela.title("TechBairro — Cadastro de Cliente")

# Define o tamanho da janela: largura x altura
janela.geometry("480x460")

# Impede que o usuário redimensione a janela
janela.resizable(False, False)


# ============================================================
# CLASSE CLIENTE
# ============================================================

# A classe Cliente representa um cliente dentro do sistema
# Cada objeto criado a partir dessa classe terá seus próprios dados
class Cliente:

    # Método construtor
    # É executado automaticamente quando criamos um novo Cliente
    def __init__(self, nome, telefone, email, endereco):
        # self representa o próprio objeto que está sendo criado

        # Armazena os dados recebidos nos atributos do objeto
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    # Método que retorna os principais dados do cliente
    # em uma única string
    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

    # Método que retorna as iniciais do nome do cliente
    # Exemplo: "João Victor Mendes" -> "JVM"
    def iniciais(self):

        # split() divide o nome em partes utilizando os espaços
        partes = self.nome.split()

        # Percorre cada parte do nome, pega a primeira letra
        # e transforma em maiúscula
        return "".join(parte[0].upper() for parte in partes if parte)


# ============================================================
# CLASSE GERENCIADOR DE CLIENTES
# ============================================================

# Essa classe será responsável por administrar os clientes
# cadastrados no sistema
class GerenciadorClientes:

    # Método construtor do gerenciador
    def __init__(self):

        # Lista que armazenará os objetos da classe Cliente
        # Agora a lista pertence ao objeto gerenciador
        # e não fica mais como uma variável global separada
        self.clientes = []

    # CREATE
    # Recebe um objeto Cliente e adiciona na lista
    def adicionar(self, cliente):
        self.clientes.append(cliente)

    # READ
    # Retorna a lista de clientes cadastrados
    def listar(self):
        return self.clientes

    # UPDATE
    # Receberá a posição do cliente e os novos dados
    def atualizar(self, indice, novo_cliente):

        # Funcionalidade ainda não implementada
        print("Atualizar cliente: funcionalidade ainda não implementada.")

    # DELETE
    # Receberá a posição do cliente que deverá ser removido
    def remover(self, indice):

        # Funcionalidade ainda não implementada
        print("Remover cliente: funcionalidade ainda não implementada.")

    # Retorna a quantidade de clientes cadastrados
    def total(self):
        return len(self.clientes)


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# Cria um objeto da classe GerenciadorClientes
# Ele será responsável por armazenar e administrar os clientes
gerenciador = GerenciadorClientes()


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

# Cria um Frame para funcionar como cabeçalho
# Frame é um "container" usado para organizar outros componentes
cabecalho = tk.Frame(janela, bg="#2c3e50")

# Coloca o cabeçalho no topo da janela
# fill="x" faz o Frame ocupar toda a largura disponível
cabecalho.pack(side="top", fill="x")


# Cria o texto do cabeçalho
tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",                    # Cor do texto
    bg="#2c3e50",                  # Cor de fundo
    font=("Arial", 14, "bold"),    # Fonte, tamanho e estilo
    pady=12                        # Espaçamento vertical interno
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

# Cria um Frame para organizar os campos do formulário
form = tk.Frame(janela)

# Adiciona o formulário na janela
form.pack(pady=20)


# Lista contendo os nomes dos campos que serão criados
campos = ["Nome", "Telefone", "E-mail", "Endereço"]

# Dicionário que armazenará os campos Entry
# Exemplo:
# entradas["Nome"] -> Entry correspondente ao nome
entradas = {}


# Percorre a lista de campos
# enumerate() fornece o índice e o valor
#
# Exemplo:
# i = 0 / campo = "Nome"
# i = 1 / campo = "Telefone"
for i, campo in enumerate(campos):

    # Cria o texto que identifica o campo
    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )

    # Cria o campo onde o usuário poderá digitar
    entrada = tk.Entry(form, width=30)

    # Posiciona o campo na coluna 1
    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )

    # Guarda o Entry dentro do dicionário
    # utilizando o nome do campo como chave
    entradas[campo] = entrada


# ============================================================
# STATUS DO SISTEMA
# ============================================================

# Label utilizada para mostrar mensagens para o usuário
# Exemplo: erro, sucesso ou informações
status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(pady=(0, 5))


# Label responsável por mostrar a quantidade de clientes
contador = tk.Label(
    janela,
    text="Clientes cadastrados: 0"
)

contador.pack()


# ============================================================
# FUNÇÃO PARA LIMPAR OS CAMPOS
# ============================================================

def limpar_campos():

    # entradas.values() retorna todos os objetos Entry
    # armazenados no dicionário
    for entrada in entradas.values():

        # Apaga todo o conteúdo do campo
        # 0 representa o início
        # tk.END representa o final
        entrada.delete(0, tk.END)


# ============================================================
# VALIDAÇÃO DE E-MAIL
# ============================================================

def email_parece_valido(email):

    # Verifica se existe @ no e-mail
    if "@" not in email:
        return False

    # partition("@") divide a string em três partes:
    #
    # usuario  -> antes do @
    # _        -> o próprio @
    # dominio  -> depois do @
    usuario, _, dominio = email.partition("@")

    # Verifica se existe usuário antes do @
    # e se existe um ponto no domínio
    if usuario == "" or "." not in dominio:
        return False

    # Se passou pelas verificações, consideramos válido
    return True


# ============================================================
# FUNÇÃO SALVAR
# ============================================================

def salvar():

    # Cria um dicionário com os valores digitados pelo usuário
    #
    # .get() pega o conteúdo do Entry
    # .strip() remove espaços extras do início e do final
    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }


    # Cria uma lista contendo somente os campos que estão vazios
    vazios = [
        campo
        for campo in campos
        if valores[campo] == ""
    ]


    # Se existir algum campo vazio...
    if vazios:

        # Mostra quais campos precisam ser preenchidos
        status.config(
            text=f"Preencha o(s) campo(s): {', '.join(vazios)}",
            fg="red"
        )

        # Interrompe a função
        return


    # Verifica se o telefone contém somente números
    if not valores["Telefone"].isdigit():

        status.config(
            text="Telefone inválido: use somente números.",
            fg="red"
        )

        return


    # Chama nossa função de validação de e-mail
    if not email_parece_valido(valores["E-mail"]):

        status.config(
            text="E-mail inválido: use o formato nome@dominio.com",
            fg="red"
        )

        return


    # ========================================================
    # CRIAÇÃO DO OBJETO CLIENTE
    # ========================================================

    # Cria um objeto da classe Cliente utilizando
    # os valores digitados no formulário
    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )


    # Adiciona o objeto Cliente ao gerenciador
    gerenciador.adicionar(cliente)


    # Exibe mensagem de sucesso
    status.config(
        text=f"Cliente '{cliente.nome}' salvo com sucesso!",
        fg="green"
    )


    # Atualiza a quantidade de clientes cadastrados
    contador.config(
        text=f"Clientes cadastrados: {gerenciador.total()}"
    )


    # Limpa o formulário após salvar
    limpar_campos()


# ============================================================
# FUNÇÃO CANCELAR
# ============================================================

def cancelar():

    # Limpa todos os campos
    limpar_campos()

    # Atualiza a mensagem de status
    status.config(
        text="Formulário limpo",
        fg="gray"
    )


# ============================================================
# JANELA DE CONSULTA
# ============================================================

def abrir_consulta():

    # Toplevel cria uma nova janela
    # sem fechar a janela principal
    consulta = tk.Toplevel(janela)

    # Define o título da nova janela
    consulta.title("Consulta de Clientes")

    # Define o tamanho da janela
    consulta.geometry("420x300")


    # Listbox permite exibir uma lista de elementos
    lista = tk.Listbox(
        consulta,
        width=55
    )

    # Posiciona a lista do lado esquerdo
    lista.pack(
        side="left",
        padx=(10, 0),
        pady=10,
        fill="both",
        expand=True
    )


    # Cria uma barra de rolagem
    scrollbar = tk.Scrollbar(consulta)

    # Coloca a barra no lado direito
    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )


    # Liga a Listbox à barra de rolagem
    lista.config(
        yscrollcommand=scrollbar.set
    )

    # Liga a barra de rolagem à Listbox
    scrollbar.config(
        command=lista.yview
    )


    # Solicita ao gerenciador a lista de clientes
    clientes_cadastrados = gerenciador.listar()


    # Verifica se a lista está vazia
    if not clientes_cadastrados:

        # Mostra uma mensagem dentro da Listbox
        lista.insert(
            tk.END,
            "Nenhum cliente cadastrado"
        )

    else:

        # Percorre todos os clientes cadastrados
        for cliente in clientes_cadastrados:

            # Adiciona o resumo do cliente na Listbox
            lista.insert(
                tk.END,
                cliente.resumo()
            )


# ============================================================
# BOTÕES
# ============================================================

# Cria um Frame para organizar os botões
botoes = tk.Frame(janela)

botoes.pack(pady=10)


# Botão Salvar
# command=salvar indica qual função será executada no clique
tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
    row=0,
    column=0,
    padx=5
)


# Botão Cancelar
tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


# Botão Consultar
tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# VERSÃO DO SISTEMA
# ============================================================

# Exibe a versão no canto inferior direito
#
# place() permite posicionar elementos utilizando coordenadas
# relativas à janela
tk.Label(
    janela,
    text="v1.0",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# ============================================================
# INICIALIZAÇÃO DA INTERFACE
# ============================================================

# Mantém a aplicação aberta e aguardando eventos
# como cliques, digitação e fechamento da janela
janela.mainloop()
