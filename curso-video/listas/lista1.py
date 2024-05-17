num = [2, 5, 9, 1]
num[2] = 3 #trocando um valor da lista que foi o 9 pelo 3
num.append(7) #adicionando valor a lista, pois lista é mutavel
num.sort() #coloca a lista em ordem crescente, para lista em decrescente usa (resverse=True)
num.insert(2, 0) #inserir valor em uma determinada posição 
if 4 in num:
   num.remove(5)
else:
   print("nao achei o numero para eliminar")   
#num.pop(2)#para eliminar elmento da lista 
print(num)
#print(f'esta lista tem {len(num)} elementos')