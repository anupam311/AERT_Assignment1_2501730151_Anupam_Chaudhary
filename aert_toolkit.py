# aert_toolkit.py
# Unit–1 Assignment Toolkit
# Author: Anupam (B.Tech AI & ML)
# ---------------------------------

# -------------------------------
# Part A: Stack ADT
# -------------------------------
class StackADT:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# -------------------------------
# Part B: Factorial & Fibonacci
# -------------------------------
def factorial(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

call_counter = {"naive":0, "memo":0}
memo = {}

def fib_naive(n):
    call_counter["naive"] += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

def fib_memo(n):
    call_counter["memo"] += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# -------------------------------
# Part C: Tower of Hanoi
# -------------------------------
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)

# -------------------------------
# Part D: Recursive Binary Search
# -------------------------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)

# -------------------------------
# Part A Task: Using Stack for Trace
# -------------------------------
def binary_search_with_trace(arr, key, low, high, trace_stack):
    if low > high:
        return -1
    mid = (low + high) // 2
    trace_stack.push(mid)   # store mid index in stack
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search_with_trace(arr, key, low, mid-1, trace_stack)
    else:
        return binary_search_with_trace(arr, key, mid+1, high, trace_stack)

# -------------------------------
# Supporting function for binary search(output function)
# -------------------------------
def result(key, result_index):
    if result_index == -1:
        print(f"Key : {key} : no found.")
    else :
        print(f"Key : {key} : found at index : {result_index}")

# -------------------------------
# Test Cases (for output.txt)
# -------------------------------
if __name__ == "__main__":

    print("=== Part A: Stack ADT ===")
    
    s = StackADT()
    s.push(10); s.push(20); s.push(30)
    print("Stack size:", s.size())
    print("Top element:", s.peek())
    print("Pop:", s.pop())
    print("Is empty?", s.is_empty())

    #-----------------------------------------------
    
    print("\n=== Part B: Factorial & Fibonacci ===")
    
    print("Factorial(5):", factorial(5))
    print("Naive Fibonacci(6):", fib_naive(6), "Calls:", call_counter["naive"])
    print("Memoized Fibonacci(6):", fib_memo(6), "Calls:", call_counter["memo"])

    #-----------------------------------------------
    
    print("\n=== Part C: Tower of Hanoi (3 disks) ===")
    
    hanoi(3, "A", "B", "C")

    #-----------------------------------------------
    
    print("\n=== Part D: Binary Search ===")
    
    arr = [1, 3, 5, 7, 9, 11]
    key = 7
    result_index = binary_search(arr, key, 0, len(arr)-1)
    result(key, result_index)
    key = 4
    result_index = binary_search(arr, key, 0, len(arr)-1)
    result(key, result_index)

    #-----------------------------------------------
    
    print("\n=== Part A Task: Binary Search Trace with Stack ===")
    
    trace = StackADT()
    key = 9
    result_index = binary_search_with_trace(arr, key, 0, len(arr)-1, trace)
    result(key, result_index)
    print("Mid indices visited (from stack):")
    while not trace.is_empty():
        print(trace.pop())
