if __name__ == '__main__':
    class Matrix:

        count = 0

        def __init__(self, mtrx_list):
            self.mtrx_list = mtrx_list

        def __add__(self, other):
            num_in_str = []
            result_list = []
            for i in range(len(self.mtrx_list)):
                for j in range(len(self.mtrx_list[i])):
                    num_summ = self.mtrx_list[i][j] + other.mtrx_list[i][j]
                    num_in_str.append(num_summ)
                    if len(num_in_str) == len(self.mtrx_list):
                        result_list.append(num_in_str)
                        num_in_str = []

            return Matrix(result_list)

        def __str__(self):
            Matrix.count += 1
            out_str = ''
            for i in self.mtrx_list:
                out_str += ' '.join(list(map(str, i))) + '\n'

            return f'Матрица №{self.count}\n{out_str}'


    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[10, 20, 30], [35, 42, 85], [21, 43, 36]])
    print(m1)
    print(m2)
    print(m1 + m2)
