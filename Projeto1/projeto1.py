import random
import time
import matplotlib.pyplot as plt
import sys
import os
import pathlib
import json
from pathlib import Path
import pandas as pd

# variavaies
quantidades = [1000,10000,100000]
ordenacao = ["asc","random","desc"]
sort_name=[
        "Bubble Sort",
        "Optimized Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort"
    ]
# variavel de controle de execução
execution = 3


def generate_vector(elements, order):
  """Generates a vector of random numbers and saves it to a file.

  Args:
    elements: The number of elements in the vector.
    order: The order of the vector ('random', 'asc', or 'desc').
  """
  vector = [random.randint(1, 100) for _ in range(elements)]

  if order == 'asc':
    vector.sort()
  elif order == 'desc':
    vector.sort(reverse=True)

  filename = f"{elements}_{order}.txt"
  with open(filename, 'w') as f:
    for element in vector:
      f.write(str(element) + '\n')

  print(f"Vector saved to {filename}")



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        # alteração realizada por sugestão da professora Valéria
        divide = int(len(arr)/2)
        
        pivot = arr[divide]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    


def evaluate_sorting_algorithms(quantidades, ordenacao):
  results = {}
  for quantidade in quantidades:
    results[quantidade] = {}
    for order in ordenacao:

      
        filename = f"{quantidade}_{order}.txt"
        with open(filename, 'r') as f:
            vector = [int(line.strip()) for line in f]
        print(quantidade)
        print(order)
        results[quantidade][order] = {}
        
        for sort_name, sort_func in [
            ("Bubble Sort", bubble_sort),
            ("Optimized Bubble Sort", optimized_bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
        ]:
            print(sort_name)
            nome_arquivo = f"./executions/execution_{str(execution)}_{str(quantidade)}_{order}_{sort_name}.txt"
            arquivo = pathlib.Path(nome_arquivo)
            if arquivo.exists():
                print('algoritimo já processado')
            else:
                print('aqui')
                vector_copy = vector[:]  # Create a copy to avoid modifying the original
                start_time = time.time()
                # sort_func(vector_copy)
                sort_func(vector_copy)
                print(type(sort_func))
                end_time = time.time()
                results[quantidade][order][sort_name] = end_time - start_time
                log = {
                    "execucao":execution,
                    "quantidade":quantidade,
                    "ordem":order,
                    "tipo_algoritimo":sort_name,
                    "inicio": start_time,
                    "fim":end_time,
                    "tempo":results[quantidade][order][sort_name]
                }
                # grava resultado em arquivo
                with open(f"executions/execution_{str(execution)}_{str(quantidade)}_{order}_{sort_name}.txt", "a") as myfile:
                    myfile.write(f'{str(log)}')
                    
                
  return results

# Função para ler o arquivo CSV e plotar o gráfico
def plot_comparison(csv_file):
    # Lê o arquivo CSV
    df = pd.read_csv(csv_file, delimiter=';')
    
    # Verifica se o arquivo contém as colunas esperadas
    if not all(col in df.columns for col in ['ordenacao', 'tempo', 'quantidade']):
        print("O arquivo CSV não possui as colunas esperadas.")
        return
    for qtd in quantidades:
        df_aux = df[df['quantidade'] == qtd]
        df_aux = df_aux.drop(columns=['quantidade', 'Unnamed: 3'])
        print(qtd)
        for ordem in ordenacao:
        #     print(ordem)
        #     df_aux = df_aux[df_aux['ordenacao'].str.contains(ordem)]
            df_aux2 = df_aux[df_aux['ordenacao'].str.contains(ordem)].sort_values(by=['tempo'], ascending=True)
            
            print(df_aux2)
            df_aux2 = df_aux[df_aux['ordenacao'].str.contains(ordem)].sort_values(by=['tempo'], ascending=False)

            # inicio grafico
            # Configurações do gráfico
            plt.figure(figsize=(20, 6))
            plt.xlabel('Algoritmo')
            plt.ylabel('tempo')
            plt.title(f'Comparação {qtd} - {ordem}')
            plt.xticks(rotation=45, ha='right')
            ax = plt.gca()
            df_aux2.plot(kind='barh', alpha=0.75, ax=ax, rot=0, x='ordenacao', y='tempo')

            plt.show()
            # fim grafico
    
    # # Plotando a comparação de tempo vs quantidade
    # for ordenacao in df['ordenacao'].unique():
    #     # Filtra os dados para cada tipo de ordenação
    #     data = df[df['ordenacao'] == ordenacao]
        
    #     # Plotando o gráfico para o tipo de ordenação específico
    #     plt.plot(data['quantidade'], data['tempo'], label=ordenacao, marker='o', linestyle='-', markersize=5)
    
    # # Adiciona título e labels aos eixos
    # plt.title(f'Comparação entre tipos de busca -  Execução {execution}')
    # plt.xlabel('Quantidade de Registros')
    # plt.ylabel('Tempo de Execução (em segundos)')
    
    # # Adiciona legenda
    # plt.legend(title='Tipo de Ordenação')
    
    # # Exibe o gráfico
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()



def load_executions(quantidades, ordenacao, sort_name):
    resultados = []
    ord = []

    # Definindo o caminho do arquivo a ser deletado
    caminho_arquivo = Path(f"result{execution}.csv")

    # Deletando o arquivo
    if caminho_arquivo.exists():
        caminho_arquivo.unlink()
        print('Arquivo deletado com sucesso!')
    else:
        print('Arquivo não encontrado.')


    with open(f"result{execution}.csv", "a") as myfile:
        myfile.write('ordenacao;tempo;quantidade;\n')

    for order in ordenacao:
        for sort in sort_name:
            ord.append(f"{sort} - {order}")
            temp = {}
            temp["sort"] = f"{sort} - {order}"
            for quantidade in quantidades:
                f = open(f"executions/execution_{str(execution)}_{str(quantidade)}_{order}_{sort}.txt", "r")
                a = (json.loads(f.read().replace("'", "\"")))
                print(a)
                temp["quantidade"] = a["quantidade"]
                temp["tempo"] =  a["tempo"]
                resultados.append(temp)
                with open(f"result{execution}.csv", "a") as myfile:
                    myfile.write(f'{sort} - {order};{a["tempo"]};{a["quantidade"]};\n')

    print(resultados)
    print(ord)
    plot_comparison(f"result{execution}.csv")


    # for quantidade in quantidades:
    #     for order in ordenacao:
    #         for sort in sort_name:
    #             # print(f"executions/execution_{str(execution)}_{str(quantidade)}_{order}_{sort}.txt")
    #             f = open(f"executions/execution_{str(execution)}_{str(quantidade)}_{order}_{sort}.txt", "r")
    #             resultados.append(json.loads(f.read().replace("'", "\"")))

    # print(resultados)

    # for item in resultados:
    #     print(item)
    #     print(item.keys())
    #     print(item.values())
    # final = []
    # print(len(resultados))



    # for orde in ord:
    #     print(orde)
    #     # print([o for o in resultados if o['sort'] == orde])
    #     linha = {}
    #     linha["order"] = orde
    #     linha["tempo"] = []
    #     linha["quantidade"] = []
        
        
    #     for o in resultados:
    #         print(orde.strip(" "))
    #         print(o['sort'].strip(" "))
    #         print(o['tempo'])
    #         if (orde.strip(" ")== o['sort'].strip(" ")):
    #             print('SIM')
    #             linha["tempo"].append(o['tempo'])
    #             linha["quantidade"].append(o['quantidade'])
        
    #             final.append( linha )        


    

    # print(final)
    # print(len(final))
    



        # temp_ordem = [o for o in orde if o['sort'] in ord]
        # expectedResult = [d for d in exampleSet if d['type'] in keyValList]
  

        







# cria as massas para avaliação
# for i in quantidades:
#   for j in ordenacao:
#     generate_vector(i,j)


# aumenta o limite de recursão
sys.setrecursionlimit(max(sys.getrecursionlimit(), 101000))

# Executa as avaliações e gera os gráficos
# results = evaluate_sorting_algorithms(quantidades, ordenacao)

load_executions(quantidades, ordenacao, sort_name)



# plot_results(results)
