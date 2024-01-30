class Matrix:
    def __init__(self, rows, cols, values):
        self.rows = rows
        self.cols = cols
        self.values = values

    def __str__(self):
        return '\n'.join([' '.join([str(self.values[i * self.cols + j]) for j in range(self.cols)]) for i in range(self.rows)])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("ابعاد ماتریس مطابقت ندارد.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.values[i * self.cols + j] + other.values[i * self.cols + j])
            result.append(row)
        return Matrix(self.rows, self.cols, [val for row in result for val in row])



    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("نمی توان ماتریس ها را با این ابعاد ضرب کرد.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                val = sum(self.values[i * self.cols + k] * other.values[k * other.cols + j] for k in range(self.cols))
                row.append(val)
            result.append(row)
        return Matrix(self.rows, other.cols, [val for row in result for val in row])
    


def transpose_matrix(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix



def inverse_matrix(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return "ماتریس معکوس پذیر نیست."
    inv_det = 1 / det
    inverted_matrix = [
        [matrix[1][1] * inv_det, -matrix[0][1] * inv_det],
        [-matrix[1][0] * inv_det, matrix[0][0] * inv_det]
    ]
    return inverted_matrix



def mean(values):
    return sum(values) / len(values)

def covariance_matrix(X, Y):
    n = len(X)

    mean_X = mean(X)
    mean_Y = mean(Y)

    # محاسبه ماتریس کوواریانس
    cov_XY = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / (n - 1)

    cov_XX = sum((X[i] - mean_X) * (X[j] - mean_X) for i in range(n) for j in range(n)) / (n - 1)
    cov_YY = sum((Y[i] - mean_Y) * (Y[j] - mean_Y) for i in range(n) for j in range(n)) / (n - 1)

    cov_matrix = [
        [cov_XX, cov_XY],
        [cov_XY, cov_YY]
    ]

    return cov_matrix



