# 767. Reorganize String

## Solução

> Given a string `S`, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
> 
> If possible, output any possible result.  If not possible, return the empty string.
> 
> **Example 1:**  
> <pre>
>  <strong>Input:</strong> S = "aab"
>  <strong>Output:</strong> = "aba"
> </pre>
> **Example 2:**  
> <pre>
>  <strong>Input:</strong> S = "aaab"
>  <strong>Output:</strong> = ""
> </pre>
> **Note:**  
> - `S` will consist of lowercase letters and have length in range` [1, 500]`.  

Para resolver essa questão, é necessário seguir uma estrátegia para tentar reorganizar a string. Devemos perceber que as letras que mais ocorrem são as que causam mais problema. Podemos alternar entre duas letras com maior número de ocorrências na string das letras que ainda precisam ser organizadas. Como na questão [86](question86.md), precisamos de uma tupla, que nesse caso terá primeiro o número de ocorrências e depois o valor.  

Além disso temos um valor máximo do maior número de ocôrrencias, imagine que a letra que mais ocorre é um separador, se tivermos `k` separadores, precisamos de, no mínimo `k` letras restantes, se `k` for ímpar e `k-1` letras restantes se `k` for par. Em geral `k` pode ser no máximo `piso(n + 1 / 2)` . 


## Implementação

Para fazer a contagem, usamos um dicionário, primeiro precisamos colocar os elementos nele:

```Python 
C = {}
max_count = (len(S) + 1) // 2 
for ch in S:
    count = C.get(ch, 0)  + 1
    if(count > max_count):
        return ""
    C[ch] = count
```

Depois é só ordenar pelos critérios discutidos. Mas como temos uma min-heap e queremos que os elementos com maior número de ocorrências venham primeiro, utilizamos o valor negativo para as ocorrências.

```Python 
pq = []
for key, value in C.items():
    pq.append((-value, key))
heapify(pq)
```

Por fim organizamos a nova string, altenando entre os dois elementos com mais ocorrências (atualmente), sempre diminuindo o número de ocorrências em 1 (ou seja, somando 1 no número negativo de ocorrências), e retornamos o resultado.

```Python 
result = ""
        while(len(pq) > 1):
            p1, v1 = heappop(pq)
            p2, v2 = heappop(pq)
            result += v1 + v2
            if(p1 != -1):
                heappush(pq, (p1 + 1, v1))
            if(p2 != -1):
                heappush(pq, (p2 + 1, v2))
        if(len(pq) == 1):
            result += heappop(pq)[1]
        return result 
```
Como pode ser observado ao pegar os elementos dois a dois, pode ser que sobre um, se sobrar é só concatenar no resultado.

+ [Código completo](./question767.py)
+ [Pratique no LeetCode](https://leetcode.com/problems/reorganize-string/)

Viu algum erro? mande um email para pabloemanuell2017@gmail.com
 
&ensp;|&ensp;[<- ANTERIOR](question215.md)  

&ensp;|&ensp;[<- VOLTAR PARA O ÍNICIO](README.md)
