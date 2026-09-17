# 🐍 Trilha de Exercícios Python — Do Zero ao Projeto Final

Uma sequência progressiva de exercícios para aprender **Python na prática**, começando pelos fundamentos e avançando até **Programação Orientada a Objetos (POO)** e projetos integradores.

A ideia é construir conhecimento passo a passo, combinando os conceitos conforme a trilha avança.

---

## 📚 Trilha de aprendizagem

| Nível | Conteúdo | Exercícios |
|---|---|---:|
| 🟢 1 | Variáveis e tipos de dados | 1–3 |
| 🟡 2 | `if / elif / else` | 4–7 |
| 🟠 3 | `for` e `while` | 8–12 |
| 🔵 4 | Funções | 13–16 |
| 🟣 5 | Listas | 17–19 |
| 🟤 6 | Dicionários | 20–22 |
| 🔴 7 | Arquivos | 23–26 |
| 🟧 8 | Classes e objetos | 27–29 |
| 🚀 9 | Projetos integradores | 30–32 |

---

# 🟢 Nível 1 — Variáveis e tipos de dados

## 1. Dados pessoais

Crie um programa que armazene em variáveis:

- Nome
- Idade
- Altura
- Cidade
- Se possui CNH (`True` ou `False`)

Depois, exiba uma frase usando essas informações.

## 2. Calculadora de idade

Peça o ano de nascimento do usuário e calcule sua idade.

Trabalhe com:

- `int`
- `input()`
- Variáveis
- Operações matemáticas

## 3. Conversor de temperatura

Peça uma temperatura em Celsius e converta para Fahrenheit.

**Fórmula:**

```text
F = C * 9/5 + 32
```

---

# 🟡 Nível 2 — `if / elif / else`

## 4. Maior de idade

Peça a idade de uma pessoa e informe:

```text
Menor de idade
```

ou

```text
Maior de idade
```

## 5. Número positivo, negativo ou zero

Leia um número e informe se ele é:

- Positivo
- Negativo
- Zero

## 6. Sistema de notas

Peça três notas e calcule a média.

Classifique:

- Média >= 7 → Aprovado
- Média >= 5 → Recuperação
- Média < 5 → Reprovado

## 7. Caixa eletrônico

Crie um programa que receba o saldo e o valor que o usuário deseja sacar.

Verifique:

- Se o valor é maior que o saldo
- Se o valor é válido
- Quanto sobra depois do saque

---

# 🟠 Nível 3 — `for` e `while`

## 8. Contagem

Use um `for` para mostrar os números de 1 até 100.

Depois faça o mesmo usando `while`.

## 9. Tabuada

Peça um número e mostre sua tabuada de 1 a 10.

**Exemplo:**

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

## 10. Soma de números

Peça 10 números ao usuário e mostre a soma deles.

## 11. Senha

Crie um sistema que peça uma senha.

O usuário terá no máximo **3 tentativas**.

Se acertar:

```text
Acesso permitido
```

Caso contrário:

```text
Acesso bloqueado
```

## 12. Menu interativo

Crie um programa que mostre:

```text
1 - Dizer olá
2 - Mostrar data
3 - Sair
```

O programa deve continuar funcionando até o usuário escolher `3`.

---

# 🔵 Nível 4 — Funções

## 13. Função de saudação

Crie uma função:

```python
saudacao(nome)
```

que receba um nome e mostre:

```text
Olá, João!
```

## 14. Calculadora

Crie funções separadas para:

```python
somar()
subtrair()
multiplicar()
dividir()
```

Depois crie um menu para o usuário escolher a operação.

## 15. Verificar número par

Crie uma função:

```python
eh_par(numero)
```

Ela deve retornar `True` ou `False`.

## 16. Calculadora de média

Crie uma função que receba uma lista de notas e retorne a média.

**Exemplo:**

```python
notas = [8, 7, 9, 10]
```

---

# 🟣 Nível 5 — Listas

## 17. Lista de compras

Crie um programa que permita ao usuário:

```text
1 - Adicionar produto
2 - Remover produto
3 - Listar produtos
4 - Sair
```

Utilize uma lista para armazenar os produtos.

## 18. Maior e menor número

Dada a lista:

```python
numeros = [10, 5, 23, 8, 42, 17, 3]
```

Encontre:

- Maior número
- Menor número
- Soma
- Média

**Desafio:** faça sem utilizar `max()`, `min()` e `sum()`.

## 19. Lista de alunos

Crie uma lista contendo vários alunos.

Depois permita:

- Adicionar aluno
- Remover aluno
- Pesquisar aluno
- Mostrar todos os alunos

---

# 🟤 Nível 6 — Dicionários

## 20. Cadastro de pessoa

Crie um dicionário:

```python
pessoa = {
    "nome": "João",
    "idade": 20,
    "cidade": "Belo Horizonte"
}
```

Depois permita que o usuário altere os valores.

## 21. Cadastro de produtos

Crie uma lista de dicionários:

```python
produtos = [
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 100},
    {"nome": "Monitor", "preco": 800}
]
```

Faça funções para:

- Cadastrar produto
- Listar produtos
- Pesquisar produto
- Calcular o valor total dos produtos

## 22. Sistema de notas

Crie um dicionário contendo alunos e suas notas:

```python
alunos = {
    "João": [8, 7, 9],
    "Maria": [10, 9, 8],
    "Pedro": [5, 6, 4]
}
```

Calcule a média de cada aluno e informe sua situação.

---

# 🔴 Nível 7 — Arquivos

## 23. Escrever em arquivo

Peça uma mensagem ao usuário e salve-a em:

```text
mensagem.txt
```

Utilize `open()` e `write()`.

## 24. Ler arquivo

Abra o arquivo criado anteriormente e mostre seu conteúdo na tela utilizando `read()`.

## 25. Cadastro em arquivo

Crie um programa que permita cadastrar nomes.

Cada nome deve ser salvo no arquivo:

```text
nomes.txt
```

Quando o programa iniciar, ele deve ler o arquivo e mostrar os nomes já cadastrados.

## 26. Diário

Crie um pequeno diário.

O usuário poderá escrever uma nova entrada, que será adicionada ao arquivo:

```text
diario.txt
```

O programa também deve possuir uma opção para visualizar todas as entradas.

---

# 🟧 Nível 8 — Classes e objetos

## 27. Classe Pessoa

Crie uma classe:

```python
class Pessoa:
```

Ela deve possuir:

```text
nome
idade
```

E um método:

```text
apresentar()
```

**Exemplo de utilização:**

```python
pessoa1 = Pessoa("João", 25)
pessoa1.apresentar()
```

## 28. Classe ContaBancaria

Crie uma classe `ContaBancaria` com:

- Titular
- Saldo

Métodos:

```text
depositar()
sacar()
consultar_saldo()
```

Não permita sacar mais dinheiro do que existe na conta.

## 29. Classe Produto

Crie uma classe `Produto` com:

- Nome
- Preço
- Quantidade

Crie métodos para:

```text
calcular_total()
adicionar_estoque()
remover_estoque()
```

---

# 🚀 Nível 9 — Projetos integradores

Aqui começam exercícios que realmente juntam os conceitos.

## 30. Sistema de cadastro de alunos

Crie um sistema que permita:

```text
1 - Cadastrar aluno
2 - Listar alunos
3 - Pesquisar aluno
4 - Remover aluno
5 - Salvar alunos
6 - Carregar alunos
7 - Sair
```

Cada aluno deve possuir:

```text
nome
idade
notas
```

Utilize:

- Lista
- Dicionário
- Funções
- `if / elif / else`
- `while`
- Arquivo

---

## 31. Sistema bancário

Crie um sistema bancário com:

```text
1 - Criar conta
2 - Depositar
3 - Sacar
4 - Consultar saldo
5 - Listar contas
6 - Sair
```

Aqui você deve obrigatoriamente utilizar uma classe:

```python
class Conta:
```

Cada objeto `Conta` deve representar uma conta bancária.

Use também um arquivo para salvar os dados.

---

# 🔥 32. Projeto final — Sistema de biblioteca

Esse é o exercício que eu recomendo fazer **sem olhar solução**.

Crie um sistema de biblioteca capaz de:

```text
===== BIBLIOTECA =====

1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Cadastrar usuário
5 - Listar usuários
6 - Emprestar livro
7 - Devolver livro
8 - Salvar dados
9 - Carregar dados
10 - Sair
```

Cada livro deve possuir:

```text
título
autor
ano
disponível
```

Cada usuário deve possuir:

```text
nome
idade
```

Você deverá criar pelo menos:

```python
class Livro:
    ...


class Usuario:
    ...


class Biblioteca:
    ...
```

## O projeto deve utilizar obrigatoriamente

- Variáveis e tipos de dados
- `if / elif / else`
- `for`
- `while`
- Funções
- Listas
- Dicionários
- `open()`
- `read()`
- `write()`
- Classes
- Objetos
- Métodos
- `__init__`

---

# 🧠 Regra importante

Tente fazer os exercícios **na ordem**.

Do **1 ao 29**, o objetivo é construir cada conceito separadamente.

Do **30 em diante**, você começa a combinar tudo em sistemas maiores.

Não tenha pressa para avançar. Se um exercício parecer difícil, tente quebrá-lo em partes menores antes de procurar uma solução.

---

# 🗺️ Trilha resumida

```text
1–3   → Fundamentos
  ↓
4–7   → Condicionais
  ↓
8–12  → Loops
  ↓
13–16 → Funções
  ↓
17–19 → Listas
  ↓
20–22 → Dicionários
  ↓
23–26 → Arquivos
  ↓
27–29 → POO
  ↓
30–32 → Projetos completos
```

---

## ⭐ Objetivo da trilha

Ao finalizar os 32 exercícios, você terá praticado uma base sólida de Python:

**fundamentos → lógica → estruturas de dados → funções → arquivos → POO → projetos.**

A proposta não é apenas terminar uma lista de exercícios, mas aprender a **pensar e construir programas por conta própria**.

> 💡 Dica: tente resolver cada exercício sozinho antes de pesquisar uma solução. Errar faz parte do processo de aprendizagem.
