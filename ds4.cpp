#include <iostream>

void sieveOfEratosthenes(int n) {
    bool prime[n + 1];
    for (int i = 0; i <= n; ++i) {
        prime[i] = true;
    }
    prime[0] = prime[1] = false;

    for (int p = 2; p * p <= n; ++p) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }

    for (int p = 2; p <= n; ++p) {
        if (prime[p]) {
            std::cout << p << " ";
        }
    }
    std::cout << std::endl;
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    sieveOfEratosthenes(n);
    return 0;
}