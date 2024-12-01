#include <iostream>

void deleteElement(int arr[], int& n, int x) {
    // Find the position of the element to be deleted
    int pos = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            pos = i;
            break;
        }
    }

    // If element not found
    if (pos == -1) {
        std::cout << "Element not found in the array." << std::endl;
        return;
    }

    // Delete element by shifting elements to the left
    for (int i = pos; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }

    // Decrease the size of the array
    n--;
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Original array: ";
    printArray(arr, n);

    int x = 3;
    deleteElement(arr, n, x);

    std::cout << "Array after deleting " << x << ": ";
    printArray(arr, n);

    return 0;
}