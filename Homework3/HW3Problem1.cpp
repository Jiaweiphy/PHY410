#include <iostream>
#include <iomanip>
#include <array>
#include <cmath>

int main()
{
	int n;
	std::cout << " How many vectors do you have?";
	std::cin >> n;
	while (n < 2) {
		std::cout << "We need at least 2 vectors. Please input again." << std::endl;
		std::cin >> n;
	}

        float *arrx = new float[n];
	float *arry = new float[n];
     
	for (int i = 0; i < n; i++) {
		std::cout << "x" << i+1 << "=";
		std::cin >> arrx[i];
		std::cout << "y" << i+1 << "=";
		std::cin >> arry[i];
	}

	float s;
	float min = arrx[0] * arrx[0] + arry[0] * arry[0];
	int l=1;

	for (int j = 0; j < n; j++) {
			s = arrx[j]* arrx[j] +arry[j]*arry[j];
			if (min > s) {
				min = s;
				l = j + 1;
			}
	}

	std::cout << "The minimum pair is (x"<< l << ", y" << l << ") , whose magnitude is " << sqrt(min) << "." << std::endl;
    return 0;
}

