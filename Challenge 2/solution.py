def main():
    test_array = [12, 2, 3, 4]
    test_value = 12

    soln = solution(test_array, test_value)
    print(soln)

def solution(l, t):
    # Game of 21 essentially,
    # Except you have to hit 21 *exactly*
    # If ur over, move over 1 value in the array and start counting again
    # If ur under, keep counting until you're over

    possible_soln = []
    sum_soln = 0

    # Starting index
    for i in range(len(l)):
        # Store start index
        possible_soln.append(i)
        # Add start index value to current sum
        sum_soln += l[i]

        # Checking end indexes
        for j in range(len(l)):
            # If the sum matches, we have our solution
            if (sum_soln == t):
                # Store end index and return
                possible_soln.append(j + i)
                return possible_soln
            # If we're over, scootch over one index and start counting again
            elif (sum_soln > t):
                break

            # If the next case pushes us out of the index bounds, we've run out of numbers to check.
            if (j + i + 1 < len(l)):
                sum_soln += l[j + i + 1]
            # No match found, return could not find
            else:
                possible_soln = [-1, -1]
                return possible_soln

        # Reset solution when scootching over index
        possible_soln = []
        sum_soln = 0
    

if __name__ == "__main__":
    main()
