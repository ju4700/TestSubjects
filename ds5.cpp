#include <iostream>

void insertElement(int arr[], int &n, int element, int position) {
    if (position < 0 || position > n) {
        std::cout << "Invalid position!" << std::endl;
        return;
    }

    for (int i = n; i > position; --i) {
        arr[i] = arr[i - 1];
    }

    arr[position] = element;
    ++n;
}

int main() {
    const int MAX_SIZE = 100;
    int arr[MAX_SIZE] = {1, 2, 3, 4, 5};
    int n = 5; // Current number of elements in the array

    int element = 10;
    int position = 2;

    insertElement(arr, n, element, position);

    for (int i = 0; i < n; ++i) {
        std::cout << arr[i] << " ";
    }

    return 0;
}