#include <iostream>
#include <cstring>
using namespace std;

// Function to insert string S into text T at position K
void insertString(char T[], const char S[], int K) {
    int lenT = strlen(T);
    int lenS = strlen(S);
    for (int i = lenT - 1; i >= K; --i) {
        T[i + lenS] = T[i];
    }
    for (int i = 0; i < lenS; ++i) {
        T[K + i] = S[i];
    }
    T[lenT + lenS] = '\0';
}

// Function to delete first occurrence of pattern P in text T
void deleteFirstOccurrence(char T[], const char P[]) {
    char *pos = strstr(T, P);
    if (pos != nullptr) {
        int lenP = strlen(P);
        int lenT = strlen(T);
        for (int i = pos - T; i < lenT - lenP; ++i) {
            T[i] = T[i + lenP];
        }
        T[lenT - lenP] = '\0';
    }
}

// Function to find the index of the first occurrence of pattern P in string S
int findFirstOccurrence(const char S[], const char P[]) {
    char *pos = strstr(S, P);
    if (pos != nullptr) {
        return pos - S;
    }
    return -1;
}

// Function to calculate the number of occurrences of each letter in input text
void countLetterOccurrences(const char T[]) {
    int count[256] = {0};
    for (int i = 0; T[i] != '\0'; ++i) {
        count[(unsigned char)T[i]]++;
    }
    for (int i = 0; i < 256; ++i) {
        if (count[i] > 0) {
            cout << (char)i << ": " << count[i] << endl;
        }
    }
}

// Function to replace the first occurrence of pattern P in text T with Q
void replaceFirstOccurrence(char T[], const char P[], const char Q[]) {
    char *pos = strstr(T, P);
    if (pos != nullptr) {
        int lenP = strlen(P);
        int lenQ = strlen(Q);
        int lenT = strlen(T);
        if (lenQ > lenP) {
            for (int i = lenT - 1; i >= pos - T + lenP; --i) {
                T[i + lenQ - lenP] = T[i];
            }
        } else if (lenQ < lenP) {
            for (int i = pos - T + lenQ; i < lenT - (lenP - lenQ); ++i) {
                T[i] = T[i + (lenP - lenQ)];
            }
        }
        for (int i = 0; i < lenQ; ++i) {
            pos[i] = Q[i];
        }
        T[lenT + lenQ - lenP] = '\0';
    }
}

// Function to find the length of a string S
int stringLength(const char S[]) {
    int length = 0;
    while (S[length] != '\0') {
        length++;
    }
    return length;
}

// Function to copy string S2 to S1
void stringCopy(char S1[], const char S2[]) {
    int i = 0;
    while (S2[i] != '\0') {
        S1[i] = S2[i];
        i++;
    }
    S1[i] = '\0';
}

// Function to concatenate string S2 to S1
void stringConcatenate(char S1[], const char S2[]) {
    int len1 = stringLength(S1);
    int len2 = stringLength(S2);
    for (int i = 0; i <= len2; ++i) {
        S1[len1 + i] = S2[i];
    }
}

// Function to compare two strings S1 and S2
int stringCompare(const char S1[], const char S2[]) {
    int i = 0;
    while (S1[i] != '\0' && S2[i] != '\0') {
        if (S1[i] != S2[i]) {
            return S1[i] - S2[i];
        }
        i++;
    }
    return S1[i] - S2[i];
}

// Function to reverse a string S
void stringReverse(char S[]) {
    int len = stringLength(S);
    for (int i = 0; i < len / 2; ++i) {
        char temp = S[i];
        S[i] = S[len - 1 - i];
        S[len - 1 - i] = temp;
    }
}

int main() {
    // Example usage of the functions
    char T[100] = "Hello, World!";
    char S[] = "INSERTED";
    insertString(T, S, 7);
    cout << "After insertion: " << T << endl;

    char P[] = "World";
    deleteFirstOccurrence(T, P);
    cout << "After deletion: " << T << endl;

    char text[] = "This is a test string.";
    char pattern[] = "test";
    int index = findFirstOccurrence(text, pattern);
    cout << "First occurrence index: " << index << endl;

    countLetterOccurrences(text);

    char Q[] = "exam";
    replaceFirstOccurrence(text, pattern, Q);
    cout << "After replacement: " << text << endl;

    char str1[50] = "Hello";
    char str2[] = "World";
    cout << "Length of str1: " << stringLength(str1) << endl;

    stringCopy(str1, str2);
    cout << "After copy: " << str1 << endl;

    stringConcatenate(str1, str2);
    cout << "After concatenation: " << str1 << endl;

    int cmpResult = stringCompare("abc", "abcd");
    cout << "Comparison result: " << cmpResult << endl;

    char str3[] = "Reverse me!";
    stringReverse(str3);
    cout << "After reverse: " << str3 << endl;

    return 0;
}