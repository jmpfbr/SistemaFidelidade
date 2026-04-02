import hashlib
from datetime import datetime

clientes = []  
pontos = []    
historico = [] 
regras = {"pontos_por_real": 1.0}  

menu_comum = {
    "1": {"nome": "Hambúrguer Clássico", "preco": 15.00},
    "2": {"nome": "Cheeseburger", "preco": 18.00},
    "3": {"nome": "Batata Frita", "preco": 10.00},
    "4": {"nome": "Refrigerante", "preco": 5.00},
    "5": {"nome": "Milkshake", "preco": 8.00}
}

menu_pontos = {
    "1": {"nome": "Refrigerante", "pontos": 50},
    "2": {"nome": "Batata Frita", "pontos": 100},
    "3": {"nome": "Cheeseburger", "pontos": 150},
    "4": {"nome": "Milkshake", "pontos": 120}
}

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_historico(cpf, tipo, descricao, valor):
    historico.append({
        "cpf": cpf,
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

def encontrar_indice_cliente(cpf):
    for i, cliente in enumerate(clientes):
        if cliente["cpf"] == cpf:
            return i
    return None

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def cadastrar_cliente():
    cpf = input("Digite o CPF (somente números): ").strip()
    if not validar_cpf(cpf):
        print("Erro: CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
        return False
    if encontrar_indice_cliente(cpf) is not None:
        print("Erro: CPF já cadastrado.")
        return False
    
    nome = input("Digite o nome completo: ").strip()
    if not validar_nome(nome):
        print("Erro: Nome inválido. Digite apenas letras e espaços.")
        return False

    telefone = input("Digite o telefone celular (somente números, com DDD): ").strip()
    if not validar_telefone(telefone):
        print("Erro: Telefone inválido. Deve conter exatamente 11 dígitos (DDD + número).")
        return False

    senha = input("Digite a senha: ").strip()
    senha_hash = hash_senha(senha)

    clientes.append({
        "cpf": cpf,
        "nome": nome,
        "telefone": telefone,
        "senha_hash": senha_hash
    })
    pontos.append(0) 
    print("Cadastrado com sucesso!")
    return True

def login_cliente():
    cpf = input("Digite seu CPF (somente números): ").strip()
    if not validar_cpf(cpf):
        print("Erro: CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
        return None, False

    senha = input("Digite sua senha: ").strip()
    idx = encontrar_indice_cliente(cpf)
    if idx is None:
        print("Cliente não encontrado.")
        return None, False

    senha_hash = hash_senha(senha)
    if clientes[idx]["senha_hash"] == senha_hash:
        print(f"Bem-vindo(a), {clientes[idx]['nome']}! Saldo: {pontos[idx]} pontos.")
        return cpf, True

    print("Senha inválida.")
    return None, False

def registrar_e_converter_pontos(cpf, valor_gasto, itens):
    idx = encontrar_indice_cliente(cpf)
    if idx is None:
        print("Erro: Cliente não encontrado para adicionar pontos.")
        return
    pontos_por_real = regras["pontos_por_real"]
    pontos_ganhos = int(valor_gasto * pontos_por_real)
    pontos[idx] += pontos_ganhos
    descricao_itens = ", ".join([f"{qtd}x {nome}" for nome, qtd, _ in itens])
    registrar_historico(cpf, "acúmulo", f"Compra de R${valor_gasto:.2f} ({descricao_itens})", pontos_ganhos)
    print(f"{pontos_ganhos} pontos adicionados! Saldo atual: {pontos[idx]} pontos.")

def realizar_compra(cpf):
    carrinho = []
    total = 0.0
    
    print("\n=== Cardápio Comum ===")
    for chave, item in menu_comum.items():
        print(f"{chave} - {item['nome']}: R$ {item['preco']:.2f}")
    print("0 - Finalizar pedido")
    
    while True:
        opcao = input("\nEscolha um item: ").strip()
        if opcao == "0":
            break
        if opcao not in menu_comum:
            print("Opção inválida.")
            continue
        quantidade = int(input(f"Quantidade de {menu_comum[opcao]['nome']}: "))
        valor_item = menu_comum[opcao]['preco'] * quantidade
        carrinho.append((menu_comum[opcao]['nome'], quantidade, valor_item))
        total += valor_item
    
    if total > 0:
        print("\nResumo do pedido:")
        for nome, qtd, valor in carrinho:
            print(f"{qtd}x {nome} - R$ {valor:.2f}")
        print(f"Total: R$ {total:.2f}")
        confirmar = input("Confirmar compra? (s/n): ").strip().lower()
        if confirmar == "s":
            registrar_e_converter_pontos(cpf, total, carrinho)

def resgatar_pontos(cpf):
    idx = encontrar_indice_cliente(cpf)
    if idx is None:
        print("Erro: cliente não encontrado.")
        return
    saldo = pontos[idx]
    print(f"\n=== Cardápio Fidelidade (Saldo: {saldo} pontos) ===")
    for chave, item in menu_pontos.items():
        print(f"{chave} - {item['nome']}: {item['pontos']} pontos")
    print("0 - Cancelar")
    
    escolha = input("Escolha um item para resgatar: ").strip()
    if escolha == "0":
        return
    if escolha not in menu_pontos:
        print("Opção inválida.")
        return
    item = menu_pontos[escolha]
    if saldo >= item["pontos"]:
        pontos[idx] -= item["pontos"]
        registrar_historico(cpf, "resgate", f"Resgatou {item['nome']}", item["pontos"])
        print(f"{item['nome']} resgatado! Novo saldo: {pontos[idx]} pontos.")
    else:
        print("Saldo insuficiente.")

def exibir_historico(cpf):
    registros = [h for h in historico if h["cpf"] == cpf]
    if not registros:
        print("\nNenhuma atividade registrada ainda.")
        return
    print("\n=== Histórico de Atividades ===")
    for h in registros:
        print(f"[{h['data']}] {h['tipo'].capitalize()} - {h['descricao']} ({h['valor']} pontos)")
    print("===============================")

def fluxo_principal():
    print("\n=== Bem-vindo à Hamburgueria ===")
    possui_cadastro = input("Já possui cadastro? (s/n): ").strip().lower()
    cpf = None
    if possui_cadastro == "s":
        cpf, ok = login_cliente()
        if not ok: return
    elif possui_cadastro == "n":
        if not cadastrar_cliente(): return
        cpf = clientes[-1]["cpf"]
    else:
        print("Opção inválida.")
        return

    while True:
        print("\n--- Menu Principal ---")
        print("1 - Cardápio Comum (R$)")
        print("2 - Cardápio Fidelidade (Pontos)")
        print("3 - Histórico")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            realizar_compra(cpf)
        elif escolha == "2":
            resgatar_pontos(cpf)
        elif escolha == "3":
            exibir_historico(cpf)
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    while True:
        fluxo_principal()
        sair = input("Deseja encerrar o sistema? (s/n): ").strip().lower()
        if sair == "s":
            print("Encerrando...")
            break
