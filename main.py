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

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você e maior de idade, otimo! Ja pode beber ou dirigir
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else: 
  print("Você é jovem ainda, jovem ainda...")

  #E se eu quisesse perguntar o genero (M = Masculino e F = Feminino)
  #Mostre (...e voce tambem precisa/precisou prestar o serviço militar obrigatorio)

print("vai ser executada de qualquer jeito")