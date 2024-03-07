#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Iterate from the second row to the nth row
    for i in range(1, n):
        # Create a new row
        row = [1]

        # Iterate through the previous row to calculate values for the current row
        for j in range(1, len(triangle[i - 1])):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the last element of the row
        row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
