import math

combinations = [];

def main():
    steps = 200;
    print(solution(steps));

def solution(n):
    if n <= 3 or n > 200:
        return;

    table = [1] + [0] * (n)

    for brick in range(1, n + 1):
        for height in range(n, brick - 1, -1):
            table[height] += table[height - brick];

    return table[-1] - 1

if __name__ == '__main__':
    main()