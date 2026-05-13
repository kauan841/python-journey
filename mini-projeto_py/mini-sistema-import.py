from calculos import soma, multiplicar
from mensagens import informacao_usuario, mensagem_boas_vindas, mensagem_soma, mensagem_multiplicacao, mensagem_despedida

mensagem_boas_vindas()
print("Informações sobre o sistema:")
informacao_usuario()
mensagem_soma()
print("Resultado da soma: ", soma(0, 0))
mensagem_multiplicacao()
print("Resultado da multiplicação: ", multiplicar(0, 0))
mensagem_despedida()