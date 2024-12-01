#include <iostream>
#include <string>

void insertString(std::string &T, const std::string &S, size_t K) {
    if (K > T.length()) {
        std::cerr << "Position K is out of bounds." << std::endl;
        return;
    }
    T.insert(K, S);
}

int main() {
    std::string T, S;
    size_t K;

    std::cout << "Enter the main text (T): ";
    std::getline(std::cin, T);

    std::cout << "Enter the string to insert (S): ";
    std::getline(std::cin, S);

    std::cout << "Enter the position (K): ";
    std::cin >> K;

    insertString(T, S, K);

    std::cout << "Resulting text: " << T << std::endl;

    return 0;
}