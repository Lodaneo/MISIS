from typing import Any, Iterator, Optional


class Node:
    # Classe que representa um nó da lista ligada
    # Cada nó armazena um valor e a referência para o próximo nó
    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        # Inicializa o nó com um valor e o próximo nó
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        # Representação do nó para debug
        return f"Node({self.value!r})"


class SinglyLinkedList:
    """
    Lista simplesmente ligada (Singly Linked List).

    Atributos principais:
      - head: primeiro nó da lista
      - tail: último nó da lista
      - _size: quantidade de elementos

    Métodos principais:
      - append(value)       → adiciona no final
      - prepend(value)      → adiciona no início
      - insert(idx, value)  → insere em um índice específico
      - remove(value)       → remove pelo valor
      - remove_at(idx)      → remove pelo índice
    """

    __slots__ = ("head", "tail", "_size")

    def __init__(self, iterable=None) -> None:
        # Inicializa a lista vazia
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

        # Se for passado um iterável, adiciona os elementos
        if iterable:
            for v in iterable:
                self.append(v)

    def append(self, value: Any) -> None:
        """Adiciona um elemento no final da lista (O(1))."""
        node = Node(value)

        if not self.head:
            # Caso a lista esteja vazia
            self.head = node
            self.tail = node
        else:
            # Caso a lista já possua elementos
            assert self.tail is not None
            self.tail.next = node
            self.tail = node

        self._size += 1

    def prepend(self, value: Any) -> None:
        """Adiciona um elemento no início da lista (O(1))."""
        node = Node(value, next=self.head)
        self.head = node

        # Se a lista estava vazia, o novo nó também é o tail
        if self._size == 0:
            self.tail = node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Insere um elemento em um índice específico."""
        if idx < 0 or idx > self._size:
            raise IndexError("insert index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        # Percorre a lista até o nó anterior ao índice desejado
        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next

        assert prev is not None
        node = Node(value, next=prev.next)
        prev.next = node
        self._size += 1

    def remove(self, value: Any) -> None:
        """Remove a primeira ocorrência de um valor na lista."""
        prev: Optional[Node] = None
        cur = self.head

        while cur:
            if cur.value == value:
                # Caso o elemento esteja no início
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next

                # Caso o elemento seja o último
                if cur is self.tail:
                    self.tail = prev

                self._size -= 1
                return

            prev, cur = cur, cur.next

        # Caso o valor não seja encontrado
        raise ValueError("remove: value not found in SinglyLinkedList")

    def remove_at(self, idx: int) -> None:
        """Remove um elemento pelo índice."""
        if idx < 0 or idx >= self._size:
            raise IndexError("remove_at index out of range")

        prev: Optional[Node] = None
        cur = self.head

        # Percorre até o índice desejado
        for _ in range(idx):
            prev, cur = cur, cur.next  # type: ignore

        assert cur is not None

        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next

        if cur is self.tail:
            self.tail = prev

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        # Permite percorrer a lista usando for
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        # Retorna o tamanho da lista
        return self._size

    def __repr__(self) -> str:
        # Representação técnica da lista
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def __str__(self) -> str:
        # Representação visual da lista encadeada
        parts = []
        cur = self.head
        while cur:
            parts.append(f"[{cur.value!s}]")
            cur = cur.next
        parts.append("None")
        return " -> ".join(parts)


# ----------------------- Exemplo de uso ----------------------- #

sll = SinglyLinkedList()

# Mostra o tamanho inicial da lista
print(f'List length: {len(sll)}')

sll.append(1)
sll.append(2)
sll.prepend(0)

# Mostra o tamanho após adicionar elementos
print(f'List length after adding elements: {len(sll)}')
print(f'List contents: {list(sll)}')

sll.insert(1, 0.5)
print(f'List length after inserting 0.5 at index 1: {len(sll)}')
print(f'List contents: {list(sll)}')

sll.append(52)
print(f'List after appending 52: {list(sll)}')

# Representação encadeada final
print(sll)
            for v in iterable:
                self.append(v)

    def append(self, value: Any) -> None:
        """Добавить в конец — O(1)."""
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить в начало — O(1)."""
        node = Node(value, next=self.head)
        self.head = node
        if self._size == 0:
            self.tail = node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить по индексу. Допускаются idx==0 и idx==len."""
        if idx < 0 or idx > self._size:
            raise IndexError("insert index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self.head
        for _ in range(idx - 1):
            assert prev is not None
            prev = prev.next
        assert prev is not None
        node = Node(value, next=prev.next)
        prev.next = node
        self._size += 1

    def remove(self, value: Any) -> None:
        """Удалить первое вхождение value. Если не найдено — ValueError."""
        prev: Optional[Node] = None
        cur = self.head
        idx = 0
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev, cur = cur, cur.next
            idx += 1
        raise ValueError("remove: value not found in SinglyLinkedList")

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу. Возбуждает IndexError при неверном индексе."""
        if idx < 0 or idx >= self._size:
            raise IndexError("remove_at index out of range")
        prev: Optional[Node] = None
        cur = self.head
        for _ in range(idx):
            prev, cur = cur, cur.next  # type: ignore
        assert cur is not None
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        if cur is self.tail:
            self.tail = prev
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(repr(x) for x in self)}])"

    def __str__(self) -> str:
        parts = []
        cur = self.head
        while cur:
            parts.append(f"[{cur.value!s}]")
            cur = cur.next
        parts.append("None")
        return " -> ".join(parts)

sll = SinglyLinkedList()
print(f'Длина нашего односвязанного списка : {len(sll)}')

sll.append(1)
sll.append(2)
sll.prepend(0)
print(f'Наша ныняшняя длина списка после добавления эллементов : {len(sll)}') 
print(f'Односвязаный список : {list(sll)}')

sll.insert(1, 0.5)
print(f'Длина списка после добавления на 1 индекс числа 0.5 : {len(sll)}')
print(f'Односвязаный список : {list(sll)}')
sll.append(52)
print(f'Односвязанный список после добавления числа в конец : {list(sll)}')


print(sll) 
