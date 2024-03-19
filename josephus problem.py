def josephus(N, K):
    circle = list(range(1, N + 1))
    index = 0
    
    while len(circle) > 1:
        index = (index + K - 1) % len(circle)
        circle.pop(index)
    
    return circle[0]

# Contoh penggunaan
N = 7
K = 3
print("Posisi yang tersisa:", josephus(N, K))
