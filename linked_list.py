class LinkedList():

    def __init__(self, node=None):
        self.head = node
    
    def append_to_tail(self, data):
        self.head.append_to_tail(data)

class Node():

    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        next = Node(data)
        node = self
        while (node.next):
            node = node.next
        node.next = next

def main():
    first_node = Node(1)
    ll = LinkedList(first_node)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    node = ll.head
    while (node):
        print(node.data)
        node = node.next

if __name__ == '__main__':
    main()