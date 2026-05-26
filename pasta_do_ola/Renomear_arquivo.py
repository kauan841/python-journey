
import os
novo_caminho = "C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\"
novo_caminho += "novo_exemplo2.txt"

os.rename("C:\\Users\\kaike\\Desktop\\pasta_de_exercicio\\pasta_do_ola\\exemplo.txt", novo_caminho)
print("Arquivo renomeado com sucesso!")
