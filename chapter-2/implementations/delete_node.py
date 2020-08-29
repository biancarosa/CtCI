class LinkedList():

    def __init__(self, node=None):
        self.head = node

    def append_to_tail(self, node):
        self.head.append_to_tail(node)


class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, node):
        next = node
        node = self
        while (node.next):
            node = node.next
        node.next = next


def delete_middle_node(ll, delete_node):
    node = ll.head
    while (node):
        if node.next == delete_node:
            node.next = node.next.next
            break
        node = node.next


def main():
    first_node = Node(1)
    ll = LinkedList(first_node)
    ll.append_to_tail(Node(2))
    ll.append_to_tail(Node(3))
    ll.append_to_tail(Node(4))
    middle_node = Node(5)
    ll.append_to_tail(middle_node)
    ll.append_to_tail(Node(6))
    ll.append_to_tail(Node(7))
    ll.append_to_tail(Node(8))
    delete_middle_node(ll, middle_node)
    node = ll.head
    while (node):
        print(node.data)
        node = node.next


if __name__ == '__main__':
    main()
