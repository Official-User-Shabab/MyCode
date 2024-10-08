#include <iostream>
using namespace std;

int main() {
  
    string word1 = "Fizz";
    string word2 = "Buzz";
    string word3 = "Fizz Buzz";
    int values;
    cout << "How many values do you want to see? ";
    cin >> values;

    for (int x = 1; x <= values; x++) {
        if (x % 3 == 0 && x % 5 == 0) {
            cout << word3 << endl; //Fizz Buzz
        } else if (x % 3 == 0) {
            cout << word1 << endl; //Fizz
        } else if (x % 5 == 0) {
            cout << word2 << endl; //Buzz
        } else {
            cout << x << endl;
        }
    }
    return 0;
}
