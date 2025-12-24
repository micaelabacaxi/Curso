lista_produtos = ["camisa", "calca", "tenis", "blusao", "oversized",] 

lista_preco = [1000, 3000, 2500, 4000, 5000] 

dic_produtos = {"camisa": 1000, "calca": 3000, "tenis": 2500, "blusao": 4000, "oversized": 5000} 


#pegar um item
produto = "oversized"
posicao = lista_produtos.index(produto)
preco = lista_preco[posicao]
print(produto, preco)

#index busca a posicao do item na lista

print(dic_produtos["oversized"])  #pegar o preco do produto diretamente no dicionario

dic_vendas = {"marcos": [1900, 300, 500, 700], "ana": [2000, 400, 600, 800]}
print(dic_vendas["marcos"])  #pegar todas as vendas do marcos


#adicionar item
dic_produtos["boné"] = 1500
print(dic_produtos) 



#editar um item 
dic_produtos["camisa"] = dic_produtos["camisa"] * dic_produtos["tenis"] #aumenta o preco da camisa em 100
print(dic_produtos["camisa"])

dic_produtos["oversized"] = dic_produtos["oversized"] * 2.0  #muda o preco do oversized para 2X
print(dic_produtos["oversized"]) 



#remover um item
item_removido = dic_produtos.pop("calca")
print(dic_produtos)
print(item_removido)

# verificar se um item esta no dicionario
print("tenis" in dic_produtos)  
print("tenis" in dic_produtos.keys())
print(2500 in dic_produtos.values())


produtos = list(dic_produtos.keys()) 
print(produtos )
produtos = list(dic_produtos.values()) 
print(produtos )    

# contagem de itens no dicionario

qtde_itens = len(dic_produtos)
print(qtde_itens)   

dic_produtos = {"camisa": 1000, "calca": 3000, "tenis": 2500, "blusao": 4000, "oversized": 5000} 
produto_buscado = input("qual produto voce esta procurando?  ")
produto_buscado = produto_buscado.lower()
if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print(f"produto {produto_buscado} disponivel para venda por R${preco:.2f}")
else:
    print(f"Produto {produto_buscado} nao disponivel para venda")