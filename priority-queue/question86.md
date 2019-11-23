# 86. Partition List

## Solução

> Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
> You should preserve the original relative order of the nodes in each of the two partitions.
> **Example:**
>
> ```None
> Input: head = 1->4->3->2->5->2, x = 3
> Output: 1->2->2->4->3->5
> ```
>
Para resolver a questão, temos que ordenar pelos seguintes críterios, em ordem de prioridade:  

1. Valores menores que `x` primeiro.
2. Valores mais à esquerda na lista original primeiro.  

Isso é, precisamos fazer uma lista de prioridade com que armazene tuplas do tipo:  
t = (critério 1, critério 2, valor)  
Para o critério 1 podemos fazer dois grupos (0 e 1), um para valores menores que `x` e outro para o restante.  
Para o critério 2 podemos usar o índice dos elementos na lista original.  
Ao final da construção da fila, podemos fazer uma lista encadeada com o terceiro item de cada tupla.

## Implementação

Primeiramente declaramos a fila de prioridade:

```Python 3
pqueue = []
```

Depois precisamos percorrer a lista de entrada e colocar os elementos na fila, conforme os critérios estabelecidos:

```Python 3
current = head
i = 0
while(current != None):
    val = current.val
    heappush(pqueue, (0 if val < x else 1, i, val))
    current = current.next
    i += 1
```

Agora construímos a nova lista de adjacência e retornamos:

```Python 3
newhead = ListNode(heappop(pqueue)[2])
        current = newhead
        while(len(pqueue) > 0):
            current.next = ListNode(heappop(pqueue)[2])
            current = current.next
        return newhead
```

Tomando cuidado, no começo, com o caso da lista vazia:
```Python 3
if(head == None):
    return head
```

+ [Código completo](./question86.py)
+ [Pratique no LeetCode](https://leetcode.com/problems/partition-list/)

Viu algum erro? mande um email para pabloemanuell2017@gmail.com
 
&ensp;|&ensp;[-> PRÓXIMA](question215.md)  

&ensp;|&ensp;[<- VOLTAR PARA O ÍNICIO](README.md)
