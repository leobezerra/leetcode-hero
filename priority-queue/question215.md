# 215. Kth Largest Element in an Array

## Solução

> Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
> 
> **Example 1:**
> 
> ```
> Input: [3,2,1,5,6,4] and k = 2
> Output: 5
> ```
> 
> **Example 2:**
> 
>  ```Input: [3,2,3,1,2,4,5,5,6] and k = 4
> Output: 4
>  ```
> **Note:**
> You may assume k is always valid, 1 ≤ k ≤ array's length.  

Para resolver essa questão, podemos ordenar a lista em ordem descrecente e retornar o k-ésimo termo, porém para economizar espaço podemos guardar apenas os cinco maiores elementos em uma fila e retornar o menor. 

## Implementação

Como sempre iniciamos declarando a lista, depois, para cada elemento na lista adicionamos ele na fila, e, como queremos guardar apenas os `k` maiores elementos, se o tamanho da fila é maior que `k`, removemos o menor. No final, apenas retornamos o menor elemento da fila. Veja o código: 
```Python 3
pqueue = []
for el in nums:
    heappush(pqueue, el)
    if(len(pqueue) > k):
        heappop(pqueue)
return pqueue[0]
``` 

+ [Código completo](./question215.py)
+ [Pratique no LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Viu algum erro? mande um email para pabloemanuell2017@gmail.com

[<- ANTERIOR](question86.md)&ensp;|&ensp;[PRÓXIMA ->](question767.md)  

[VOLTAR PARA O ÍNICIO](README.md)
