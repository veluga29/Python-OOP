from typing import Generic, TypeVar, Optional


T = TypeVar("T")


class Node(Generic[T]):
    __slots__ = ["item", "pointer"]

    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item: T = item
        self.pointer: "Node" | None = pointer


class LinkedList(Generic[T]):
    __slots__ = ["head"]

    def __init__(self, head: Node[T] | None = None):
        self.head: Node[T] | None = head

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            tail: Node[T] = self.head
            length = 1
            while tail.pointer:
                tail = tail.pointer
                length += 1
            return length

    def __str__(self) -> str:
        result: str = ""
        tail = self.head
        if tail is None:
            return ""
        result += f"{tail.item}"
        while tail.pointer:
            tail = tail.pointer
            result += f", {tail.item}"

        return result


class Stack(Generic[T], LinkedList[T]):
    def push(self, item: T):
        if self.head is None:
            self.head = Node[T](item)
        else:
            tail: Node = self.head
            while tail.pointer:
                tail = tail.pointer
            tail.pointer = Node(item)

    def pop(self) -> T | None:
        if self.head is None:
            raise ValueError("Stack is empty")
        cur_node: Node[T] = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        else:
            while cur_node.pointer.pointer:  # type: ignore
                cur_node = cur_node.pointer  # type: ignore
            tail = cur_node.pointer
            cur_node.pointer = None

            return tail.item  # type: ignore


if __name__ == "__main__":
    stack: Stack = Stack()

    stack.push("Welsh Corgi")
    stack.push("Poodle")

    print(stack.pop())
    print(stack.pop())

    stack.push("Welsh Corgi")
    stack.push("Poodle")

    print(stack.length)
    print(stack)
