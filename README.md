# 🍔 Sistema de Fidelidade - Hamburgueria Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Security-SHA--256-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

Sistema de gerenciamento de pedidos e fidelidade via terminal, permitindo que clientes acumulem pontos em compras reais e os troquem por produtos do cardápio especial.

---

## 📋 Sobre o Projeto

O projeto é um script robusto em Python que simula a operação de uma hamburgueria. Ele foca na **experiência do cliente**, oferecendo desde o cadastro seguro até a conversão automática de valores gastos em pontos de fidelidade.

---

## 🎯 Funcionalidades

- 🔐 **Segurança**: As senhas dos usuários não são salvas em texto puro; o sistema utiliza **SHA-256** para gerar hashes seguros.
- ✅ **Validações**: Verificação rigorosa de CPF, Nome e Telefone para evitar dados inconsistentes.
- 🛒 **Cardápio Duplo**:
    - **Comum**: Compras em Reais (R$) que geram pontos.
    - **Fidelidade**: Produtos exclusivos resgatados apenas com pontos acumulados.
- 📜 **Histórico Detalhado**: Registro completo de cada acúmulo e resgate, incluindo data e hora.
- 💰 **Conversão Dinâmica**: Sistema de regras que define quantos pontos o cliente ganha por real gasto.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Bibliotecas Nativas:** - `hashlib`: Para criptografia de senhas.
    - `datetime`: Para registro temporal das atividades.

---

## 📂 Estrutura do Código

```text
.
├── sistema_fidelidade.py   # Script principal com toda a lógica
└── README.md               # Documentação do projeto
```

---

⚙️ Como Executar
Certifique-se de ter o Python instalado.

Clone o repositório:

```text
git clone [https://github.com/jmpfbr/nome-do-repositorio.git](https://github.com/jmpfbr/nome-do-repositorio.git)
```

Inicie o sistema:

```text
python sistema_fidelidade.py
```

---

📌 Objetivo Acadêmico

Desenvolvido para consolidar conhecimentos em Lógica de Programação, este projeto aplica conceitos de:

Estruturas de dados complexas (Listas de Dicionários).

Funções com múltiplos retornos e parâmetros.

Algoritmos de busca e validação.

Persistência em memória e segurança da informação.

---

👨‍💻 Autor

João Marcos Fierro e Grupo

---

📄 Licença

Fierro Softwares

Este projeto é de uso acadêmico e livre para estudos.
