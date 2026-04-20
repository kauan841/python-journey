#Criar usuário (dict)
#Permitir atualizar idade
#Mostrar antes e depois

perfil_usuario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

print("Perfil do usuário antes da atualização:")
print(perfil_usuario)   
# Atualizando a idade do usuário
perfil_usuario["idade"] = 31
print("Perfil do usuário após a atualização:")
print(perfil_usuario)