#!/usr/bin/env python3
"""
data_structures.py  —  Python Data Structures Examples
Run:  python data_structures.py
"""

from collections import deque, namedtuple, defaultdict, Counter
import heapq


# ─────────────────────────────────────────────
# 1. LIST  — ordered, mutable, allows duplicates
# ─────────────────────────────────────────────
def demo_list():
    print("=" * 50)
    print("1. LIST")
    print("=" * 50)

    fruits = ["apple", "banana", "cherry", "apple"]
    fruits.append("mango")          # add to end
    fruits.insert(1, "blueberry")   # insert at index
    fruits.remove("apple")          # remove first occurrence
    popped = fruits.pop()           # remove & return last item
    fruits.sort()                   # sort in-place

    print("Fruits:", fruits)
    print("Popped:", popped)
    print("Slice [1:3]:", fruits[1:3])
    print("Length:", len(fruits))


# ─────────────────────────────────────────────
# 2. TUPLE  — ordered, immutable, allows duplicates
# ─────────────────────────────────────────────
def demo_tuple():
    print("\n" + "=" * 50)
    print("2. TUPLE")
    print("=" * 50)

    coordinates = (10.5, 20.3, 30.1)
    x, y, z = coordinates           # unpacking

    print("Coordinates:", coordinates)
    print("X:", x, "| Y:", y, "| Z:", z)
    print("Index of 20.3:", coordinates.index(20.3))
    print("Count of 10.5:", coordinates.count(10.5))

    person = ("Alice", 30, True)
    print("Mixed-type tuple:", person)


# ─────────────────────────────────────────────
# 3. DICTIONARY  — key-value pairs, ordered (3.7+), mutable
# ─────────────────────────────────────────────
def demo_dict():
    print("\n" + "=" * 50)
    print("3. DICTIONARY")
    print("=" * 50)

    student = {"name": "Bob", "age": 22, "grades": [88, 92, 75], "active": True}
    student["email"] = "bob@example.com"    # add key
    student["age"] = 23                     # update value
    student.pop("active")                   # remove key

    print("Student:", student)
    print("Name:", student["name"])
    print("Age (get):", student.get("age", "N/A"))
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))

    squares = {n: n**2 for n in range(1, 6)}
    print("Comprehension squares:", squares)


# ─────────────────────────────────────────────
# 4. SET  — unordered, unique elements, mutable
# ─────────────────────────────────────────────
def demo_set():
    print("\n" + "=" * 50)
    print("4. SET")
    print("=" * 50)

    mixed = {1, 2, 2, 3, 3, 3}     # duplicates dropped
    print("Mixed (duplicates removed):", mixed)

    evens = {2, 4, 6, 8, 10}
    evens.add(12)
    evens.discard(2)                # no error if missing

    primes = {2, 3, 5, 7}
    nums   = {1, 2, 3, 4, 5}
    print("Union:", primes | nums)
    print("Intersection:", primes & nums)
    print("Difference (primes - nums):", primes - nums)
    print("Symmetric difference:", primes ^ nums)


# ─────────────────────────────────────────────
# 5. FROZENSET  — immutable set
# ─────────────────────────────────────────────
def demo_frozenset():
    print("\n" + "=" * 50)
    print("5. FROZENSET")
    print("=" * 50)

    immutable_set = frozenset([1, 2, 3, 4, 5])
    print("Frozenset:", immutable_set)
    print("Is 3 in frozenset?", 3 in immutable_set)
    # immutable_set.add(6)  → AttributeError (immutable)


# ─────────────────────────────────────────────
# 6. STRING  — ordered, immutable character sequence
# ─────────────────────────────────────────────
def demo_string():
    print("\n" + "=" * 50)
    print("6. STRING (as a sequence)")
    print("=" * 50)

    sentence = "  Hello, Python World!  "
    print("Upper:", sentence.upper())
    print("Strip:", sentence.strip())
    print("Replace:", sentence.replace("Python", "Data Structures"))
    print("Split:", sentence.strip().split(" "))
    print("Starts with 'Hello':", sentence.strip().startswith("Hello"))
    print("Slice [7:13]:", sentence.strip()[7:13])


# ─────────────────────────────────────────────
# 7. STACK  — LIFO using a list
# ─────────────────────────────────────────────
def demo_stack():
    print("\n" + "=" * 50)
    print("7. STACK (LIFO — using list)")
    print("=" * 50)

    stack = []
    for task in ["task_1", "task_2", "task_3"]:
        stack.append(task)
    print("Stack after pushes:", stack)
    print("Pop (LIFO):", stack.pop())
    print("Stack now:", stack)


# ─────────────────────────────────────────────
# 8. QUEUE  — FIFO using collections.deque
# ─────────────────────────────────────────────
def demo_queue():
    print("\n" + "=" * 50)
    print("8. QUEUE (FIFO — collections.deque)")
    print("=" * 50)

    queue = deque(["customer_1", "customer_2", "customer_3"])
    print("Queue:", queue)
    print("Dequeue (FIFO):", queue.popleft())
    print("Queue now:", queue)


# ─────────────────────────────────────────────
# 9. LINKED LIST  — manual node-based implementation
# ─────────────────────────────────────────────
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements, current = [], self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(str(e) for e in elements)

def demo_linked_list():
    print("\n" + "=" * 50)
    print("9. LINKED LIST")
    print("=" * 50)

    ll = LinkedList()
    for value in [10, 20, 30, 40]:
        ll.append(value)
    print("Linked list:", ll.display())


# ─────────────────────────────────────────────
# 10. HEAP (PRIORITY QUEUE)  — using heapq
# ─────────────────────────────────────────────
def demo_heap():
    print("\n" + "=" * 50)
    print("10. HEAP / PRIORITY QUEUE (heapq)")
    print("=" * 50)

    min_heap = [5, 3, 8, 1, 9, 2]
    heapq.heapify(min_heap)         # convert list to min-heap in-place
    print("Min-heap:", min_heap)
    heapq.heappush(min_heap, 0)
    print("After push 0:", min_heap)
    print("Pop smallest:", heapq.heappop(min_heap))
    print("Heap now:", min_heap)


# ─────────────────────────────────────────────
# 11. NAMED TUPLE  — lightweight, readable records
# ─────────────────────────────────────────────
def demo_namedtuple():
    print("\n" + "=" * 50)
    print("11. NAMED TUPLE")
    print("=" * 50)

    Point = namedtuple("Point", ["x", "y", "z"])
    p = Point(1, 2, 3)
    print("Point:", p)
    print("X:", p.x, "| Y:", p.y, "| Z:", p.z)


# ─────────────────────────────────────────────
# 12. DEFAULTDICT  — dict with automatic default values
# ─────────────────────────────────────────────
def demo_defaultdict():
    print("\n" + "=" * 50)
    print("12. DEFAULTDICT")
    print("=" * 50)

    word_count = defaultdict(int)
    for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
        word_count[word] += 1
    print("Word counts:", dict(word_count))

    grouped = defaultdict(list)
    for category, item in [("fruit", "apple"), ("veggie", "carrot"),
                            ("fruit", "mango"), ("veggie", "spinach")]:
        grouped[category].append(item)
    print("Grouped:", dict(grouped))


# ─────────────────────────────────────────────
# 13. COUNTER  — specialized dict for counting
# ─────────────────────────────────────────────
def demo_counter():
    print("\n" + "=" * 50)
    print("13. COUNTER")
    print("=" * 50)

    votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
    tally = Counter(votes)
    print("Vote tally:", tally)
    print("Most common (top 2):", tally.most_common(2))


# ─────────────────────────────────────────────
# 14. 2D LIST (Matrix)
# ─────────────────────────────────────────────
def demo_matrix():
    print("\n" + "=" * 50)
    print("14. 2D LIST (Matrix)")
    print("=" * 50)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix:")
    for row in matrix:
        print("  ", row)

    print("Element [1][2]:", matrix[1][2])

    transposed = [[matrix[r][c] for r in range(3)] for c in range(3)]
    print("Transposed:")
    for row in transposed:
        print("  ", row)


# ─────────────────────────────────────────────
# MAIN  — entry point
# ─────────────────────────────────────────────
def main():
    print("\n  Python Data Structures — Live Examples")
    print("  ========================================\n")

    demo_list()
    demo_tuple()
    demo_dict()
    demo_set()
    demo_frozenset()
    demo_string()
    demo_stack()
    demo_queue()
    demo_linked_list()
    demo_heap()
    demo_namedtuple()
    demo_defaultdict()
    demo_counter()
    demo_matrix()

    print("\n" + "=" * 50)
    print("All examples executed successfully.")
    print("=" * 50)


if __name__ == "__main__":
    main()
