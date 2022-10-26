# comando input(): quero permitir que o usuario digite algo...
nome = input("Digite seu nome: ")
# comando de saida..exibir na tela 
idade = int(input("Digite sua idade: "))


print(nome)
print(idade)

print(f"Boa noite, seu nome é {nome}")

#e se eu quisesse mostrar o dobro da idade informada?
dobro = idade * 2 
print("O dobro da idade informada é {}".format(dobro))

