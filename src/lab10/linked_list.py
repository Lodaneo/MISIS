from collections import deque
from typing import Any, Optional


class Stack:
    """
    Estrutura de dados Stack (Pilha) – LIFO (Last In, First Out).

    O último elemento inserido é o primeiro a ser removido.

    Operações principais:
      - push(item)   → adiciona um elemento ao topo
      - pop()        → remove o elemento do topo
      - peek()       → retorna o elemento do topo sem remover
      - is_empty()   → verifica se a pilha está vazia
      - __len__()    → retorna o tamanho da pilha
    """

    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        # Inicializa a pilha com uma lista (ou vazia, se nada for passado)
        self._data: list[Any] = list(iterable) if iterable is not None else []

    def push(self, item: Any) -> None:
        # Adiciona um elemento ao topo da pilha
        self._data.append(item)

    def pop(self) -> Any:
        # Remove e retorna o elemento do topo da pilha
        if not self._data:
            raise IndexError("Tentativa de remover elemento de uma pilha vazia")
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        # Retorna o elemento do topo sem remover
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        # Verifica se a pilha está vazia
        return not self._data

    def __len__(self) -> int:
        # Retorna a quantidade de elementos na pilha
        return len(self._data)

    def __repr__(self) -> str:
        # Representação da pilha para debug
        return f"Stack({self._data!r})"


class Queue:
    """
    Estrutura de dados Queue (Fila) – FIFO (First In, First Out).

    O primeiro elemento inserido é o primeiro a ser removido.

    Implementada usando collections.deque para eficiência.

    Operações principais:
      - enqueue(item) → adiciona elemento ao final da fila
      - dequeue()     → remove elemento do início da fila
      - peek()        → retorna o primeiro elemento sem remover
      - is_empty()    → verifica se a fila está vazia
      - __len__()     → retorna o tamanho da fila
    """

    __slots__ = ("_data",)

    def __init__(self, iterable=None) -> None:
        # Inicializa a fila com deque (ou vazia)
        self._data: deque[Any] = deque(iterable) if iterable is not None else deque()

    def enqueue(self, item: Any) -> None:
        # Adiciona um elemento ao final da fila
        self._data.append(item)

    def dequeue(self) -> Any:
        # Remove e retorna o primeiro elemento da fila
        if not self._data:
            raise IndexError("Tentativa de remover elemento de uma fila vazia")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        # Retorna o primeiro elemento da fila sem remover
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        # Verifica se a fila está vazia
        return not self._data

    def __len__(self) -> int:
        # Retorna a quantidade de elementos na fila
        return len(self._data)

    def __repr__(self) -> str:
        # Representação da fila para debug
        return f"Queue({list(self._data)!r})"


# ----------------------- Exemplo de uso: Stack ----------------------- #

print('========> Stack <========')

stack = Stack([1, 2, 3, 4])

# Remove o elemento do topo da pilha
print(f'Top element removed: {stack.pop()}')

# Verifica se a pilha está vazia
print(f'Is stack empty? {stack.is_empty()}')

# Mostra o elemento do topo
print(f'Top element: {stack.peek()}')

# Adiciona um novo elemento
stack.push(1)
print(f'Top element after push: {stack.peek()}')

# Mostra o tamanho da pilha
print(f'Stack length: {len(stack)}')

# Mostra o conteúdo interno da pilha
print(f'Stack data: {stack._data}')


# ----------------------- Exemplo de uso: Queue ----------------------- #

print('========> Queue <========')

q = Queue([1, 2, 3, 4])

# Mostra o primeiro elemento da fila
print(f'First element: {q.peek()}')

# Remove o primeiro elemento
q.dequeue()
print(f'First element after dequeue: {q.peek()}')

# Adiciona um elemento ao final da fila
q.enqueue(52)
print(f'First element after enqueue: {q.peek()}')

# Verifica se a fila está vazia
print(f'Is queue empty? {q.is_empty()}')

# Mostra o tamanho da fila
print(f'Queue length: {len(q)}')
