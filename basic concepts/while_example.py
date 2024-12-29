#Exemplo básico de estrutura de repetição (While)
#Soma realizada enquanto os valores digitados são maiores que 0.

qtd = 0
soma = 0
media = 0
valor = int(input("Digite um valor: "))

while (valor > 0):
    soma = soma + valor
    qtd = qtd + 1
    valor = int(input("Digite um valor: "))

media = soma/qtd
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ", media)