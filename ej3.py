#función de fibonacci.
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#         yield a
# for i in fibonacci(10):
#     print(i)
def fib(n):
    a = 0
    b = 1
    
    for k in range(n):
        c = b+a
        a = b
        b = c
    return a


if __name__ == "__main__":
    print(fib(15))
    print(fib(20))