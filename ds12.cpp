#include <iostream>
using namespace std;

// Function to interchange rows and columns of a matrix
void transposeMatrix(int matrix[3][3], int transposed[3][3], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            transposed[j][i] = matrix[i][j];
        }
    }
}

// Function to add two matrices
void addMatrices(int matrix1[3][3], int matrix2[3][3], int result[3][3], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
}

// Function to multiply two matrices
void multiplyMatrices(int matrix1[3][3], int matrix2[3][3], int result[3][3], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < cols; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

// Function to calculate row sum and column sum of a matrix
void rowColumnSum(int matrix[3][3], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        int rowSum = 0;
        for (int j = 0; j < cols; ++j) {
            rowSum += matrix[i][j];
        }
        cout << "Sum of row " << i + 1 << ": " << rowSum << endl;
    }

    for (int j = 0; j < cols; ++j) {
        int colSum = 0;
        for (int i = 0; i < rows; ++i) {
            colSum += matrix[i][j];
        }
        cout << "Sum of column " << j + 1 << ": " << colSum << endl;
    }
}

// Function to check if a matrix is a sparse matrix
bool isSparseMatrix(int matrix[3][3], int rows, int cols) {
    int zeroCount = 0;
    int totalElements = rows * cols;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (matrix[i][j] == 0) {
                zeroCount++;
            }
        }
    }
    return zeroCount > (totalElements / 2);
}

int main() {
    int matrix1[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int matrix2[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int result[3][3];
    int transposed[3][3];

    // Interchange rows and columns
    transposeMatrix(matrix1, transposed, 3, 3);
    cout << "Transposed Matrix:" << endl;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << transposed[i][j] << " ";
        }
        cout << endl;
    }

    // Add two matrices
    addMatrices(matrix1, matrix2, result, 3, 3);
    cout << "Sum of Matrices:" << endl;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    // Multiply two matrices
    multiplyMatrices(matrix1, matrix2, result, 3, 3);
    cout << "Product of Matrices:" << endl;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    // Calculate row sum and column sum
    cout << "Row and Column Sums:" << endl;
    rowColumnSum(matrix1, 3, 3);

    // Check if matrix is sparse
    if (isSparseMatrix(matrix1, 3, 3)) {
        cout << "Matrix is Sparse" << endl;
    } else {
        cout << "Matrix is not Sparse" << endl;
    }

    return 0;
}