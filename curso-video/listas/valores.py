# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
#itens = ["Antena", "Roteador", "Switch", "Servidor", "Cabine Pack", "Access Popint", "Edge Routers", "Patch cord", "Ups"]

# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":
itens.append('antena')
itens.append('roteador')
itens.append('switch')

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")