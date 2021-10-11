# Eigen Values Calculator
import math

A = []
print('Enter the values of 3x3 matrix')

# Input the matrix values.
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    A.append(row)

# Print the matrix for better visualization.
print('\n      Matrix')
for i in range(len(A)):
    for j in range(len(A[i])):
        print('%4d' % (A[i][j]), end=' ')
    print()

# Sum of diagonal elements.
s1 = A[0][0] + A[1][1] + A[2][2]

# Sum of diagonal minors.
s2 = (A[1][1]*A[2][2] - A[1][2]*A[2][1]) + \
     (A[0][0]*A[2][2] - A[0][2]*A[2][0]) + \
     (A[0][0]*A[1][1] - A[0][1]*A[1][0])

# Determinant of matrix.
determinant = (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])) - \
              (A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])) + \
              (A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))

# Characteristic Equation.
equation = '(lambda^3) - (' + str(s1) + ')*(lambda^2) + (' + \
           str(s2) + ')*(lambda) - (' + str(determinant) + ') = 0'
print('\nCharacteristic Equation : ', equation)

# Find the roots of cubic equation, which are ultimately the eigen values.
if determinant == 0:
    # If determinant is 0 then one root is 0 and we find other two roots.
    roots = [0]
    try:
        a = 1
        b = -s1
        c = s2
        root2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        root3 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        roots.extend([root2, root3])
    except Exception as e:
        print('Eigen Values do not exist or are not real numbers.')
        exit(0)
else:
    try:
        # Find the factors of determinant.
        x = [i for i in range(1, abs(determinant)+1) if determinant % i == 0]
        # Also include negative values of the factors.
        # For example, if the factors are [1, 2, 3]
        # then also include [-1, -2, -3] to form [1, 2, 3, -1, -2, -3].
        x.extend([-i for i in x])

        roots = []
        for lambda_ in x:
            eqn = math.pow(lambda_, 3) - s1*math.pow(lambda_, 2) + s2*lambda_ \
                  - determinant
            if eqn == 0.00:
                roots.append(lambda_)

        # If there is at least one root, then calculate other two roots.
        if len(roots) < 3:
            root1 = roots[0]
            c = determinant/root1
            a = 1
            b = (s2 - c)/-root1
            root2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2*a)
            root3 = (-b - math.sqrt(b * b - 4 * a * c)) / (2*a)
            roots = [root1, root2, root3]
    except Exception as e:
        print('Eigen Values do not exist or are not real numbers.')
        exit(0)

eigen_values = roots
print('\nEigen Values of the given matrix are : ', eigen_values)
