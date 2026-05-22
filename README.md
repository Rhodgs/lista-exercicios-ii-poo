# Lista de Exercícios II - Programação Orientada a Objetos

Repositório destinado à resolução da Lista de Exercícios II da disciplina de POO, O projeto foi desenvolvido em Python.

## 👤 Autor
- **Nome:** Rhuan
- **Curso:** Engenharia de Software
- **Instituição:** UFAM - ICET

## 📁 Estrutura do Repositório
O projeto está organizado na pasta `src/`, onde cada sistema possui sua própria arquitetura isolada em `models/` (regras de negócio e contratos) e `repositories/` (gerenciamento de dados):

- [`01_sistema_midias/`](./src/01-sistema_midias): Uso de classes abstratas (ABC) e polimorfismo em mídias educacionais.
- [`02_sistema_funcionarios/`](./src/02-sistema_funcionarios): Gerenciamento e regras de funcionários.
- [`03_sistema_notificacoes/`](./src/03-sistema_notificacoes): Disparos e serviços de notificações.
- [`04_sistema_impressao/`](./src/04-sistema_impressão): Exploração de contratos estruturais via `Protocol` (Duck Typing).
- [`05_sistema_armazenamento/`](./src/05-sistema_armazenamento): Comparativo prático entre Herança Formal (`ABC`) e Tipagem Flexível (`Protocol`).

## 🚀 Como Executar os Testes
Para rodar qualquer um dos sistemas, navegue até a pasta raiz do projeto no terminal e execute o arquivo `main.py` do sistema desejado. 

Exemplo para rodar o Sistema de Mídias (Questão 1):
```bash
python src/01_sistema_midias/main.py