import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2  # Start position

    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        i_new, j_new = (i - 1) % n, (j + 1) % n  # Move diagonally up-right

        if magic_square[i_new, j_new]:  # Conflict, move down instead
            i += 1
        else:
            i, j = i_new, j_new
    
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    indices = np.array([(i, j) for i in range(n) for j in range(n) if (i % 4 == j % 4 or (i % 4 + j % 4) == 3)])
    for i, j in indices:
        magic_square[i, j] = n * n + 1 - magic_square[i, j]
    
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)
    offsets = [0, 2, 3, 1]  # Offset for the four quadrants
    
    for r in range(2):
        for c in range(2):
            magic_square[r * half_n:(r + 1) * half_n, c * half_n:(c + 1) * half_n] = \
                sub_square + offsets[r * 2 + c] * (half_n * half_n)
    
    # Column swapping for balancing
    k = (n - 2) // 4
    left_cols = list(range(k)) + [k]
    right_cols = list(range(n - k, n))
    
    # Swap left columns in the first and third quadrants
    for r in range(half_n):
        for c in left_cols:
            magic_square[r, c], magic_square[r + half_n, c] = magic_square[r + half_n, c], magic_square[r, c]
    
    # Swap right columns in the second and fourth quadrants
    for r in range(half_n):
        for c in right_cols:
            magic_square[r, c], magic_square[r + half_n, c] = magic_square[r + half_n, c], magic_square[r, c]
    
    return magic_square

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

# Generate magic squares for N = 4, 5, 6, 7, 8
for n in [4, 5, 6, 7, 8]:
    print(f"Magic Square for N={n}:")
    print(generate_magic_square(n))