import random
import time
import matplotlib.pyplot as plt
import sys
import os
import pathlib

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
            nome_arquivo = f"./execution_{str(execution)}_{str(quantidade)}_{order}_{sort_name}.txt"
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
                with open(f"execution_{str(execution)}_{str(quantidade)}_{order}_{sort_name}.txt", "a") as myfile:
                    myfile.write(f'{str(log)}')
                    
                
  return results


def plot_results(results):
  for quantidade in results:
    plt.figure(figsize=(12, 6))
    plt.title(f"Comparação de algoritmos de ordenação - {quantidade} elementos")
    for order in results[quantidade]:
        y_pos = range(len(results[quantidade][order]))
        performance = list(results[quantidade][order].values())
        algoritmos = list(results[quantidade][order].keys())

        plt.barh(y_pos, performance, label=order)
        plt.yticks(y_pos, algoritmos)
        plt.xlabel("Tempo de execução (segundos)")
        plt.ylabel("Algoritmos de ordenação")

    plt.legend()
    plt.tight_layout()
    plt.show()







# variavaies
quantidades = [1000,10000,100000]
ordenacao = ["asc","random","desc"]

# cria as massas para avaliação
# for i in quantidades:
#   for j in ordenacao:
#     generate_vector(i,j)


# aumenta o limite de recursão
sys.setrecursionlimit(max(sys.getrecursionlimit(), 101000))

# Executa as avaliações e gera os gráficos
results = evaluate_sorting_algorithms(quantidades, ordenacao)
# plot_results(results)
