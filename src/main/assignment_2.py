# Alanna Hill
# al538601
# COT4500 Spring 2023

import numpy as np;

# This function uses nevilles method to find the second degree
# interpolating value for f(x) given x and y points
def neville(x_points, y_points, x):
    num_points = len(x_points) 
    matrix = np.zeros((num_points,num_points))
    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]

    for i in range(1, num_points):
        for j in range(1, i + 1): 
            first = (x - x_points[i - j]) * matrix[i][j - 1]
            second = (x - x_points[i]) * matrix[i - 1][j - 1]
            denom = x_points[i] - x_points[i - j]
            matrix[i][j] = (first - second) / denom
    return matrix[num_points - 1][num_points - 1]

# This function uses newton's forward method and returns a matrix
# based off of the x and y points provided
def newton(x_points, y_points):
    size = len(x_points)
    matrix  = np.zeros((size, size))

    for index, row in enumerate(matrix):
        row[0] = y_points[index]

    for i in range(1, size):
        for j in range(1, i + 1):
            numer = matrix[i][j - 1] - matrix[i - 1][j - 1]
            denom = x_points[i] - x_points[i - j]
            op = numer / denom
            matrix[i][j] = op
    return matrix
# This function takes in a matrix and a set of points and a value
# to aproximate and aproximates it
def aprox(matrix, x_points, y_points, x):
    rec_x = 1
    rec_px = y_points[0]

    for index in range(1, len(x_points)):
        coef = matrix[index][index]
        rec_x *= (x - x_points[index - 1])
        mult = coef * rec_x
        rec_px += mult
    return rec_px
# This function applies divided diferences to a Hermite aproximation
# matrix
def apply_div_dif(matrix):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i + 2):
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue

            left = matrix[i][j - 1]
            diag_left = matrix[i - 1][j - 1]
            num = left - diag_left
            den = matrix[i][0] - matrix[i - (j - 1)][0]
            matrix[i][j] = num / den
    return matrix
# This function calculates a Hermite aproximation matrix
def hermite(x_points, y_points, f1x):
    num_points = len(x_points)
    matrix = np.zeros((num_points * 2, num_points * 2))
    for x in range(0, 2 * num_points):
        matrix[x][0] = x_points[x // 2]
    for x in range(0, 2 * num_points):
        matrix[x][1] = y_points[x // 2]
    for x in range(1, 2 * num_points, 2):
        matrix[x][2] = f1x[x // 2]

    matrix = apply_div_dif(matrix)
    return matrix


def findMatrix(x_points, y_points):
    num_points = len(x_points)
    return

def findVector(x, vals):
    return

# This is the main function which runs everything
def main():
    np.set_printoptions(precision=7,suppress=True,linewidth=100)
    x_points1 = [3.6, 3.8, 3.9]
    y_points1 = [1.675, 1.436, 1.318]
    ans1 = neville(x_points1, y_points1, 3.7)
    print(ans1, end="\n\n")
    x_points2 = [7.2, 7.4, 7.5, 7.6]
    y_points2 = [23.5492, 25.3913, 26.8224, 27.4589]
    table = newton(x_points2, y_points2)
    ans2 = [table[1][1], table[2][2], table[3][3]]
    print(ans2, end ="\n\n")
    ans3 = aprox(table, x_points2, y_points2,  7.3)
    print(ans3, end="\n\n")
    f1x = [-1.195, -1.188,-1.182]
    table2 = hermite(x_points1, y_points1, f1x)
    print(table2, end="\n\n")
    x_points3 = [2, 5, 8, 10]
    y_points3 = [3, 5, 7, 9]

if __name__ == "__main__":
    main()
