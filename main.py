# Missão 1: Restaurando as Regras Escolares 📝 
print("Missão 1: Restaurando as Regras Escolares 📝")
nota = float(input("Digite a nota do Aluno: "))

if nota >= 6:
    print("Aprovado!")
elif nota <= 5:
    print("Reprovado!")

print("\n")


# Missão 2: O Sistema Eleitoral Secreto 📝 
print("Missão 2: O Sistema Eleitoral Secreto 📝")
idade = int(input("Digite a sua idade:"))
if(idade >= 16):
    print("Você pode votar.")
else:
    print("Voce não pode votar.")
print("\n")


# Missão 3: Recuperando o Sistema de Notas 📊
print("Missão 3: Recuperando o Sistema de Notas 📊")
nota = int(input("Digite a sua nota:"))

if nota >= 90:
    print("Parabéns, você tirou A!")
elif nota >= 80:
    print("Muito bem, você tirou B.")
elif nota >= 70:
    print("Bom trabalho, você tirou C.")
elif nota >= 60:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

print("\n")


# Missão 4: Restaurando a Identificação de Números ⚖️
print("Missão 4: Restaurando a Identificação de Números ⚖️")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma dos números é", soma)
print("\n")


# Missão 5: Recuperando o Cofre de Segurança 🔒
print("Missão 5: Recuperando o Cofre de Segurança 🔒")
senha = input("Digite a senha: ")
if(senha == "Python123"):
    print("Senha correta")
else:
    print("Senha incorreta")

print("\n")


# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
print("Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾")
i = 1
while i <= 10:
    print(i)
    i += 1
print("\n")


# Missão 7: Organizando a Lista📋
print("Missão 7: Organizando a Lista📋")
numeros = [8, 3, 10, 1, 5]
print("Lista original:", numeros)
numeros.sort()
print("Lista organizada:", numeros)
print("\n")


# Missão 8: Acessando os Registros de Alunos 🏷️
print("Missão 8: Acessando os Registros de Alunos 🏷️")
nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print("Lista de nomes:", nomes)
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]
print("Primeiro nome:", primeiro_nome)
print("Ultimo nome:", ultimo_nome)
print("\n")


# Missão 9: Calculando Dobro de um Número 🛠️
print("Missão 9: Calculando Dobro de um Número 🛠️")
def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"

numero = int(input("Digite um número: "))
print(dobro(numero))
print("\n")


# Missão 10: Contando Letras 🔄
print("Missão 10: Contando Letras 🔄")
def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"

nome = input("Digite um nome: ")
print(contar_letras(nome))
print("\n")