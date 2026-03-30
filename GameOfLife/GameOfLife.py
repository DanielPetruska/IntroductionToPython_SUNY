import random

ROWS = 10
COLS = 10

def create_grid():
    return [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]

def display(grid):
    for row in grid:
        print(" ".join("█" if cell else "." for cell in row))
    print()

def count_neighbors(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                count += grid[nr][nc]
    return count

def next_generation(grid):
    new = [[0]*COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new[r][c] = 1 if n == 2 or n == 3 else 0
            else:
                new[r][c] = 1 if n == 3 else 0
    return new

grid = create_grid()

while True:
    display(grid)
    if input("Continue? (y/n): ").lower() != "y":
        break
    grid = next_generation(grid)