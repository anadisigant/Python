#Introdução ao conceito de variável.

codigo = int(input("Código do funcionário: "))
nome = input("Nome do funcionário: ")
salario = float(input("Salário: "))
ativo = True

print("O fúncionário sob o código %d"% codigo, ", chama-se %s"% nome)
print(f"Recebe R${salario:.2f} por mês.")
print("Ativo: %r"% ativo)