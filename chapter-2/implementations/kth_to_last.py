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


def kth_to_last(linked_list, kth=0):
    p1 = p2 = linked_list.head
    for i in range(kth):
        p2 = p2.next
    while p2 != None:
        p1 = p1.next
        p2 = p2.next
    return p1


def main():
    first_node = Node(1)
    ll = LinkedList(first_node)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    ll.append_to_tail(4)
    ll.append_to_tail(5)
    ll.append_to_tail(6)
    ll.append_to_tail(7)
    ll.append_to_tail(8)
    print(kth_to_last(ll, 1).data)


if __name__ == '__main__':
    main()
