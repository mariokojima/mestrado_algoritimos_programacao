# a. achar o resto de dois número inteiros positivos

# Resto
def resto(dividendo, divisor):
  if dividendo < divisor:
    return dividendo
  else:
    return resto(dividendo - divisor, divisor)

# Testes
print("Testes para a função resto:")

# Teste 1
print("resto(10, 3)")  
print(resto(10, 3))  

# Teste 2
print("resto(5, 5)")  
print(resto(5, 5))  

# Teste 3
print("resto(15, 4)")  
print(resto(15, 4))  

# Teste 4
print("resto(0, 5)") 
print(resto(0, 5)) 

# Teste 5
print("resto(7, 2)")  
print(resto(7, 2))  


# b. achar a divisão inteira de dois número inteiros positivos
# divisão inteira 
def divisao_inteira(dividendo, divisor):
  if dividendo < divisor:
    return 0
  else:
    return 1 + divisao_inteira(dividendo - divisor, divisor)

# Testes para a função divisao_inteira
print("\nTestes para a função divisao_inteira:")

# Teste 1
print("divisao_inteira(10, 3)")  
print(divisao_inteira(10, 3))  

# Teste 2
print("divisao_inteira(5, 5)")  
print(divisao_inteira(5, 5))  

# Teste 3
print("divisao_inteira(15, 4)") 
print(divisao_inteira(15, 4))  

# Teste 4
print("divisao_inteira(0,5)") 
print(divisao_inteira(0,5)) 

# Teste 5
print("divisao_inteira(7, 2)")
print(divisao_inteira(7, 2))  

# c. achar o mdc de dois número inteiros positivos
def mdc(a, b) :
  if (b == 0):
    return a
  else:
    return mdc(b, (a % b))

# Testes para a função mdc
print("\nTestes para a função mdc:")


# Teste 1
print("mdc(10, 15)")  
print(mdc(10, 15))  

# Teste 2
print("mdc(25, 15)")  
print(mdc(25, 15))  

# Teste 3
print("mdc(12, 18)")  
print(mdc(12, 18))  

# Teste 4
print("mdc(7, 13)") 
print(mdc(7, 13)) 

# Teste 5
print("mdc(4, 8)")  
print(mdc(4, 8))  

# d. fazer a busca sequencial de um número dentro de um vetor
def busca_sequencial(a, lista):
    for i in range(len(lista)):
        if lista[i] == a:
            return i  
    return -1  

# Testes para a função busca_sequencial
print("\nTestes para a função busca_sequencial:")

# Teste 1
print("busca_sequencial(1, [1, 2, 3, 4, 5, 6]):")  
print(busca_sequencial(1, [1, 2, 3, 4, 5, 6]))  

# Teste 2
print("busca_sequencial(6, [1, 2, 3, 4, 5, 6]):")  
print(busca_sequencial(6, [1, 2, 3, 4, 5, 6]))  

# Teste 3
print("busca_sequencial(7, [1, 2, 3, 4, 5, 6]):")  
print(busca_sequencial(7, [1, 2, 3, 4, 5, 6]))  

# Teste 4
print("busca_sequencial(3, [1,2,3,4,5,6]):") 
print(busca_sequencial(3, [1,2,3,4,5,6])) 

# Teste 5
print("busca_sequencial(5, [1, 2, 3, 4, 5, 6]):") 
print(busca_sequencial(5, [1, 2, 3, 4, 5, 6])) 


# e. fazer a busca binária de um número dentro de um vetor
def busca_binaria(a, lista):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == a:
            return meio  # Retorna o índice se o elemento for encontrado
        elif lista[meio] < a:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  # Retorna -1 se o elemento não for encontrado

# Testes para a função busca_binaria
print("\nTestes para a função busca_binaria:")


# Teste 1
print("busca_binaria(1, [1, 2, 3, 4, 5, 6]):")  
print(busca_binaria(1, [1, 2, 3, 4, 5, 6]))  

# Teste 2
print("busca_binaria(6, [1, 2, 3, 4, 5, 6]):")  
print(busca_binaria(6, [1, 2, 3, 4, 5, 6]))  

# Teste 3
print("busca_binaria(7, [1, 2, 3, 4, 5, 6]):")  
print(busca_binaria(7, [1, 2, 3, 4, 5, 6]))  

# Teste 4
print("busca_binaria(3, [1,2,3,4,5,6]):")  
print(busca_binaria(3, [1,2,3,4,5,6]))  

# Teste 5
print("busca_binaria(5, [1, 2, 3, 4, 5, 6]):")  
print(busca_binaria(5, [1, 2, 3, 4, 5, 6]))  