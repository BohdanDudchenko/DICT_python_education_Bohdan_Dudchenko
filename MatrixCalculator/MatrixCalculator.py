import copy


def determinant():
    matrix = []
    size = input('Input size matrix\n>>> ')
    size = size.replace(' ', '')
    na = int(size[1])
    print('Matrix')
    for i in range(0, na):
        line = []
        for j in range(0, na):
            line.append(int(input(f'Element {j}\n>>> ')))
        matrix.append(line)

    def calc(n, matrix):
        if n == 2:
            d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return d
        else:
            d = int(0)
            temp = copy.deepcopy(matrix)
            rows = copy.deepcopy(temp[0])
            temp.pop(0)
            for l in range(0, n):
                temp2 = copy.deepcopy(temp)
                for k in range(0, n - 1):
                    temp2[k].pop(l)
                d += ((-1) ** (0 + l + 2)) * rows[l] * (calc(n - 1, temp2))
            return d

    for i in matrix:
        print(' '.join(map(str, i)))
    print(f'Your determinate:  {str(calc(na, matrix))}')
    return 0


class MatrixProcessing:
    def __init__(self):
        self.main()

    def main(self):
        print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
            ''')
        choose = input('Enter choose\n>>> ')
        try:
            choose = int(choose)
            if choose == 0:
                print('Goodbye!!!')
            elif choose == 1:
                print('1')
                self.matrix_plus()
            elif choose == 2:
                self.matrix_constant()
            elif choose == 3:
                self.matrix_multiply()
            elif choose == 4:
                self.transpose()
            elif choose == 5:
                determinant()
            elif choose == 6:
                self.inverse_matrix()
        except ValueError:
            print('Try Again')
            self.main()

    def matrix_plus(self):
        matrix_a = []
        matrix_b = []
        matrix_plus = []
        size = input(f'Input matrix size\n>>> ')
        size = size.replace(' ', '')
        if size.isnumeric():
            size = list(size)
            size_m = int(size[0]) * int(size[1])
            print('Matrix A')
            for i in range(0, int(size_m)):
                number = input(f'Element {i}\n>>> ')
                matrix_a.append(number)
                i += 1
            print('Matrix B')
            for i in range(0, int(size_m)):
                number = input(f'Element {i}\n>>> ')
                matrix_b.append(number)
                i += 1
            for i in range(0, len(matrix_a)):
                matrix_plus.append(int(matrix_a[i]) + int(matrix_b[i]))
                i += 1
            for i in range(0, len(matrix_plus), int(size[1]) + 1):
                matrix_plus.insert(i, '\n')
            print(' '.join(map(str, matrix_plus)))
            self.main()

    def matrix_constant(self):
        size = input(f'Input matrix size\n>>> ')
        size = size.replace(' ', '')
        matrix = []
        if size.isnumeric():
            size = list(size)
            size_m = int(size[0]) * int(size[1])
            print('Matrix')
            for i in range(0, int(size_m)):
                number = input(f'Element {i}\n>>> ')
                matrix.append(number)
                i += 1
            constant = float(input(f'Input constant:\n>>> '))
            for i in range(len(matrix)):
                matrix[i] = int(matrix[i]) * constant
            for i in range(0, len(matrix), int(size[1]) + 1):
                matrix.insert(i, '\n')
            print(' '.join(map(str, matrix)))
            self.main()

    def matrix_multiply(self):
        matrix_a = []
        matrix_b = []
        size_a = input('Input size matrix A:\n>>> ')
        size_a = size_a.replace(' ', '')
        ma = int(size_a[0])
        na = int(size_a[1])
        print(size_a)
        size_b = input('Input size matrix B:\n>>> ')
        size_b = size_b.replace(' ', '')
        mb = int(size_b[0])
        nb = int(size_b[1])
        print(size_b)
        if na == mb:
            print('Matrix A')
            for i in range(0, ma):
                new_list = []
                for j in range(na):
                    number = input(f'Element {j}\n>>> ')
                    new_list.append(number)
                matrix_a.append(new_list)
            print('Matrix B')
            for i in range(0, mb):
                new_list = []
                for j in range(nb):
                    number = input(f'Element {j}\n>>> ')
                    new_list.append(number)
                matrix_b.append(new_list)
            r = []
            m = []
            for i in range(len(matrix_a)):
                for j in range(len(matrix_b[0])):
                    sums = 0
                    for k in range(len(matrix_b)):
                        sums = sums + (int(matrix_a[i][k]) * int(matrix_b[k][j]))
                    r.append(sums)
                m.append(r)
                r = []
            print('Your MATRIX')
            for i in m:
                print(' '.join(map(str, i)))
            self.main()
        else:
            self.matrix_multiply()

    def transpose(self):
        matrix = []
        size_a = input('Input size matrix\n>>> ')
        size_a = size_a.replace(' ', '')
        ma = int(size_a[0])
        na = int(size_a[1])
        print('Matrix A')
        for i in range(0, ma):
            new_list = []
            for j in range(na):
                number = input(f'Element {j}\n>>> ')
                new_list.append(number)
            matrix.append(new_list)
        for i in matrix:
            print(' '.join(map(str, i)))
        print('''
    1. Main diagonal
    2. Vertical line
    3. Horizontal line
    0. Back 
        ''')
        choose = input('\n>>> ')
        if choose.isnumeric():
            choose = int(choose)
            if choose == 0:
                self.main()
            elif choose == 1:
                print('transposed'.upper())
                transposed = list(zip(*matrix))
                for i in transposed:
                    print(' '.join(map(str, i)))
                self.main()
            elif choose == 2:
                transposed = []
                for i in range(na):
                    new_list = []
                    for j in reversed(matrix[i]):
                        new_list.append(j)
                    transposed.append(new_list)
                for i in transposed:
                    print(' '.join(map(str, i)))
                self.main()
            elif choose == 3:
                transposed = []
                for i in reversed(matrix):
                    transposed.append(i)
                for i in transposed:
                    print(' '.join(map(str, i)))
                self.main()
        else:
            print('Try Again')
            self.transpose()

    def inverse_matrix(self):
        matrix = []
        size = input('Input size matrix\n>>> ')
        size = size.replace(' ', '')
        m = int(size[0])
        n = int(size[1])
        print('Matrix')
        for i in range(0, n):
            line = []
            for j in range(0, m):
                line.append(int(input(f'Element {j}\n>>> ')))
            matrix.append(line)

        def gen_id_mat(n):
            l = [[0 for i in range(n)] for j in range(n)]
            for k in range(n):
                l[k][k] = 1
            return l

        def gen_id_mat1(n):
            l = [[0.0 for i in range(n)] for j in range(n)]
            for k in range(n):
                l[k][k] = 1.0
            return l

        def row_swap(m, r1, r2):
            m[r1], m[r2] = m[r2], m[r1]
            return m

        def row_op_1(m, r1, r2, c):
            for i in range(len(m)):
                m[r1][i] = (m[r2][i]) * c
            return m

        def row_op_2(m, r1, r2, c):
            for i in range(len(m)):
                m[r1][i] = m[r1][i] - (c * m[r2][i])
            return m

        def disp(m):
            print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in m]))
            # print()
            pass

        idm = gen_id_mat(n)
        id_inv = gen_id_mat(n)

        count = 0
        for col in range(n):
            for row in range(n):
                if idm[row][col] == 1 and matrix[row][col] == 0:
                    for g in range(n):
                        if matrix[g][col] != 0:
                            matrix = row_swap(matrix, row, g)

                if matrix[row][col] != 0 and idm[row][col] == 1:
                    multiply = 1 / matrix[row][col]
                    id_inv = row_op_1(id_inv, row, row, (1 / matrix[row][col]))
                    matrix = row_op_1(matrix, row, row, (1 / matrix[row][col]))
                    count += 1
                    for const in range(n):
                        if const == row:
                            continue
                        multiply = matrix[const][col]
                        id_inv = row_op_2(id_inv, const, row, matrix[const][col])
                        matrix = row_op_2(matrix, const, row, matrix[const][col])

                        count += 1

        if matrix == gen_id_mat1(n):
            print("Ready Matrix:")
            print()
            disp(id_inv)
            self.main()
        else:
            print("Not iterable")
            self.inverse_matrix()


MatrixProcessing()