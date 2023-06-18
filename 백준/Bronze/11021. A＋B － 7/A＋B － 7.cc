#include <iostream>
using namespace std;


int main() {

	int num;
	cin >> num;

	for (int i = 1; i <= num; i++) {
		int num1, num2;
		cin >> num1 >> num2;

		cout << "Case #" << i << ": " << num1 + num2 << "\n";
	}

	return 0;
}