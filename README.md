# Lista de Exercícios II - Programação Orientada a Objetos

Repositório destinado à resolução da Lista de Exercícios II da disciplina de POO, O projeto foi desenvolvido em Python

## 👤 Autor
- **Nome:** Rhuan
- **Curso:** Engenharia de Software
- **Instituição:** UFAM - ICET

## 👤 Professor
- **Nome:** Alternei de Souza Brito

## 📁 Estrutura do Repositório
O projeto está organizado na pasta `src/`, onde cada sistema possui sua própria arquitetura isolada em `models/` (regras de negócio e contratos) e `repositories/` (gerenciamento de dados):

- [`01-sistema_midias/`](./src/01-sistema_midias): Uso de classes abstratas (ABC) e polimorfismo em mídias educacionais.
- [`02-sistema_funcionarios/`](./src/02-sistema_funcionarios): Gerenciamento e regras de funcionários.
- [`03-sistema_notificacoes/`](./src/03-sistema_notificacoes): Disparos e serviços de notificações.
- [`04-sistema_impressao/`](./src/04-sistema_impressao): Exploração de contratos estruturais via `Protocol` (Duck Typing).
- [`05-sistema_armazenamento/`](./src/05-sistema_armazenamento): Comparativo prático entre Herança Formal (`ABC`) e Tipagem Flexível (`Protocol`).

## 🚀 Como Executar os Exercícios

Primeiro, abra o terminal do seu sistema operacional e clone o repositório:

* Clone o repositório
```bash
git clone https://github.com/Rhodgs/lista-exercicios-ii-poo
```
* Entre na pasta raiz do projeto
```bash
cd lista-exercicios-ii-poo
```

* Agora, escolha qual sistema deseja executar e rode o comando correspondente no seu terminal

---

* 📺 1. Sistema de Mídias (Questão 1)
```bash
python3 src/01-sistema_midias/main.py
```
* 💼 2. Sistema de Funcionários (Questão 2)
```bash
python3 src/02-sistema_funcionarios/main.py
```
* 🔔 3. Sistema de Notificações (Questão 3)
```bash
python3 src/03-sistema_notificacoes/main.py
```
* 📄 4. Sistema de Impressão (Questão 4)
```bash
python3 src/04-sistema_impressao/main.py
```
* 💾 5. Sistema de Armazenamento (Questão 5)
```bash
python3 src/05-sistema_armazenamento/main.py
```