#João Victor de Jesus Augusto
import tkinter as tk
from tkinter import messagebox
import csv

# Criação de um usuário Joao como inicial, que vem com a função gerente
usuarios = {
    "Joao": {"senha": "2024", "permissao": "gerente"}
}

# Armazenar produtos/serviços
produtos = []

# Função para carregar usuários de um arquivo Excel(csv)
def carregar_usuarios():
    try:
        with open('usuarios.csv', mode='r') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                usuarios[rows[0]] = {"senha": rows[1], "permissao": rows[2]}
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar usuários: {e}")

# Função para salvar usuários em um arquivo
def salvar_usuarios():
    try:
        with open('usuarios.csv', mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            for user, info in usuarios.items():
                writer.writerow([user, info["senha"], info["permissao"]])
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar usuários: {e}")

# Função para carregar os produtos
def carregar_produtos():
    global produtos
    try:
        with open('produtos.csv', mode='r') as infile:
            reader = csv.reader(infile)
            produtos = list(reader)
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar produtos: {e}")

# Função para salvar produtos em um arquivo
def salvar_produtos():
    try:
        with open('produtos.csv', mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(produtos)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar produtos: {e}")

# Área de login
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")
        
        tk.Label(self, text="Usuário:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        
        tk.Label(self, text="Senha:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(self, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = usuarios.get(username)
        
        if user and user["senha"] == password:
            self.destroy()
            if user["permissao"] == "gerente":
                app = MainApp(username)
                app.mainloop()
            else:
                app = MainApp(username, limited=True)
                app.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

# Parte principal
class MainApp(tk.Tk):
    def __init__(self, username, limited=False):
        super().__init__()
        self.title(f"Bem-vindo, {username}")
        self.geometry("500x400")
        
        menubar = tk.Menu(self)
        
        product_menu = tk.Menu(menubar, tearoff=0)
        product_menu.add_command(label="Adicionar Produto", command=self.add_product)
        product_menu.add_command(label="Visualizar Produtos", command=self.view_products)
        product_menu.add_command(label="Buscar Produto", command=self.search_product)
        product_menu.add_command(label="Ordenar por Nome", command=self.sort_by_name)
        product_menu.add_command(label="Ordenar por Preço", command=self.sort_by_price)
        product_menu.add_command(label="Remover Produto", command=self.remove_product)
        menubar.add_cascade(label="Produtos", menu=product_menu)
        
        if not limited:
            user_menu = tk.Menu(menubar, tearoff=0)
            user_menu.add_command(label="Adicionar Usuário", command=self.add_user)
            user_menu.add_command(label="Visualizar Usuários", command=self.view_users)
            user_menu.add_command(label="Atualizar Usuário", command=self.update_user)
            user_menu.add_command(label="Remover Usuário", command=self.remove_user)
            menubar.add_cascade(label="Usuários", menu=user_menu)
        
        self.config(menu=menubar)
        carregar_produtos()
        
    # Adicionar Produtos CRUD
    def add_product(self):
        def save_product():
            nome = nome_entry.get()
            preco = preco_entry.get()
            quantidade = quantidade_entry.get()
            produtos.append([nome, preco, quantidade])
            salvar_produtos()
            add_window.destroy()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
        
        add_window = tk.Toplevel(self)
        add_window.title("Adicionar Produto")
        
        tk.Label(add_window, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(add_window)
        nome_entry.pack(pady=5)
        
        tk.Label(add_window, text="Preço:").pack(pady=5)
        preco_entry = tk.Entry(add_window)
        preco_entry.pack(pady=5)
        
        tk.Label(add_window, text="Quantidade:").pack(pady=5)
        quantidade_entry = tk.Entry(add_window)
        quantidade_entry.pack(pady=5)
        
        tk.Button(add_window, text="Salvar", command=save_product).pack(pady=20)
    
    def view_products(self):
        view_window = tk.Toplevel(self)
        view_window.title("Produtos")
        
        for produto in produtos:
            tk.Label(view_window, text=f"Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}").pack(pady=5)
    
    def search_product(self):
        def perform_search():
            search_term = search_entry.get()
            for produto in produtos:
                if search_term.lower() in produto[0].lower():
                    messagebox.showinfo("Produto Encontrado", f"Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")
                    return
            messagebox.showinfo("Não Encontrado", "Produto não encontrado")
        
        search_window = tk.Toplevel(self)
        search_window.title("Buscar Produto")
        
        tk.Label(search_window, text="Nome:").pack(pady=5)
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)
        
        tk.Button(search_window, text="Buscar", command=perform_search).pack(pady=20)
    
    def sort_by_name(self):
        sorted_products = sorted(produtos, key=lambda x: x[0])
        self.show_sorted_products(sorted_products)

    def sort_by_price(self):
        sorted_products = sorted(produtos, key=lambda x: float(x[1]))
        self.show_sorted_products(sorted_products)
    
    def show_sorted_products(self, sorted_products):
        sorted_window = tk.Toplevel(self)
        sorted_window.title("Produtos Ordenados")
        
        for produto in sorted_products:
            tk.Label(sorted_window, text=f"Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}").pack(pady=5)
    
    def remove_product(self):
        def perform_remove():
            nome = nome_entry.get()
            global produtos
            produtos = [produto for produto in produtos if produto[0] != nome]
            salvar_produtos()
            remove_product_window.destroy()
            messagebox.showinfo("Sucesso", "Produto removido com sucesso")
        
        remove_product_window = tk.Toplevel(self)
        remove_product_window.title("Remover Produto")
        
        tk.Label(remove_product_window, text="Nome do Produto:").pack(pady=5)
        nome_entry = tk.Entry(remove_product_window)
        nome_entry.pack(pady=5)
        
        tk.Button(remove_product_window, text="Remover", command=perform_remove).pack(pady=20)
    
    # Adicionar Usuários CRUD
    def add_user(self):
        def save_user():
            nome = nome_entry.get()
            senha = senha_entry.get()
            permissao = permissao_entry.get()
            usuarios[nome] = {"senha": senha, "permissao": permissao}
            salvar_usuarios()
            add_user_window.destroy()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso")
        
        add_user_window = tk.Toplevel(self)
        add_user_window.title("Adicionar Usuário")
        
        tk.Label(add_user_window, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(add_user_window)
        nome_entry.pack(pady=5)
        
        tk.Label(add_user_window, text="Senha:").pack(pady=5)
        senha_entry = tk.Entry(add_user_window)
        senha_entry.pack(pady=5)
        
        tk.Label(add_user_window, text="Permissão:").pack(pady=5)
        permissao_entry = tk.Entry(add_user_window)
        permissao_entry.pack(pady=5)
        
        tk.Button(add_user_window, text="Salvar", command=save_user).pack(pady=20)
    
    def view_users(self):
        view_user_window = tk.Toplevel(self)
        view_user_window.title("Usuários")
        
        for user, info in usuarios.items():
            tk.Label(view_user_window, text=f"Nome: {user}, Permissão: {info['permissao']}").pack(pady=5)
    
    def update_user(self):
        def perform_update():
            nome = nome_entry.get()
            if nome in usuarios:
                usuarios[nome] = {"senha": senha_entry.get(), "permissao": permissao_entry.get()}
                salvar_usuarios()
                update_user_window.destroy()
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado")
        
        update_user_window = tk.Toplevel(self)
        update_user_window.title("Atualizar Usuário")
        
        tk.Label(update_user_window, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(update_user_window)
        nome_entry.pack(pady=5)
        
        tk.Label(update_user_window, text="Nova Senha:").pack(pady=5)
        senha_entry = tk.Entry(update_user_window)
        senha_entry.pack(pady=5)
        
        tk.Label(update_user_window, text="Nova Permissão:").pack(pady=5)
        permissao_entry = tk.Entry(update_user_window)
        permissao_entry.pack(pady=5)
        
        tk.Button(update_user_window, text="Atualizar", command=perform_update).pack(pady=20)
    
    def remove_user(self):
        def perform_remove():
            nome = nome_entry.get()
            if nome in usuarios:
                del usuarios[nome]
                salvar_usuarios()
                remove_user_window.destroy()
                messagebox.showinfo("Sucesso", "Usuário removido com sucesso")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado")
        
        remove_user_window = tk.Toplevel(self)
        remove_user_window.title("Remover Usuário")
        
        tk.Label(remove_user_window, text="Nome:").pack(pady=5)
        nome_entry = tk.Entry(remove_user_window)
        nome_entry.pack(pady=5)
        
        tk.Button(remove_user_window, text="Remover", command=perform_remove).pack(pady=20)

if __name__ == "__main__":
    carregar_usuarios()
    carregar_produtos()
    login_window = LoginWindow()
    login_window.mainloop()

