import math

def main():
    test_case = [12, 15324]

    for i in test_case:
        solution(i)

def solution(area):
    solution_list = []
    # Perfect square problem...
    # Step 1 is to find the largest perfect square
    # Pass values to is_square until you've found the perfect square
    i = area
    # While we have values left
    while (i > 0):
        # Start at the highest number, and check for squares while decrementing
        if (is_square(i)):
            # If the number is square, it is a solution
            solution_list.append(i)
            # Update our variables (subtract the perfect square from i and keep track of where we left)
            area = area - i
            i = area
        # Otherwise, check next lowest number for square
        else:
            i -= 1

    return solution_list

def is_square(number):
    # Calc square root of number
    calc = math.sqrt(number)
    # If the number mod 1 is 0, it is square
    if (calc % 1 == 0):
        return True
    # Else it is not
    else:
        return False

if __name__ == "__main__":
    main()