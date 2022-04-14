from numpy import base_repr

def main():
    # k = input("Enter a number k where length of k is 2 <= k <= 9: ")
    # b = input("Enter a number b where length of b is 2 <= b <= 10: ")
    n = '1211'
    b = 10
    print(solution(n, b))

def solution(n, b):
    # Error checking
    k = len(n)
    # Check to make sure lenth is within bounds
    if k < 2 or k > 9:
        print("Invalid input, k must be 2 <= k <= 9")
        return
    # Check to make sure b is within bounds
    if b < 2 or b > 10:
        print("Invalid input, b must be 2 <= b <= 10")
        return

    # Check to make sure that x is a positive integer
    x = int(n, base=b)
    if (x < 0):
        print("Invalid input, n must be positive")
        return

    # Start algorithm
    # Stores results in a list
    results = []
    # Iterate until return is called
    while(True):
        # Sort x in descending, then convert back to a string, then convert back to an int
        x = int("".join(sorted(n, reverse=True)), base=b)
        # Sort y in ascending, then convert back to a string, then convert back to an int
        y = int("".join(sorted(n)), base=b)

        # Subtract the two
        z = x - y
        # Convert to a string representation in base b
        z = base_repr(z, base=b)
        # Add prepending 0's to the string representation
        if (len(z) < k):
            z = "0" * (k - len(z)) + z
        # Assign n = z
        n = z
        # Check against the results list to see if we've converged
        if n in results:
            return (len(results) - results.index(n))
        # If not, append and repeat
        results.append(n)

if __name__ == "__main__":
    main()