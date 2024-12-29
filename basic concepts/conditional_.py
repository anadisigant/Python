#Exemplo básico de estrutura de decisão composta.

notaA = float(input("Nota da I Unidade: "))
notaB = float(input("Nota da II Unidade: "))
notaC = float(input("Nota da III Unidade: "))

mediafinal = (notaA + notaB + notaC)/3

if mediafinal > 7.0:
    print("Média: %.1f - Aprovado!"% mediafinal)
elif mediafinal >=4.0:
    print("A média %.1f te permite realizar a prova de recuperação final.\nDedique-se e boa prova!"% mediafinal)
else:
    print("Média: %.1f - Reprovado!"% mediafinal)