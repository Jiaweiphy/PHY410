#include <vector>
#include <iostream>
#include <math.h>
#include "trapezoid.hpp"
#include "simpson.hpp"

using namespace std;


int main()
{
  unsigned n1=1,n2=0;
  cout << "Trapezoid quadrature of exp(x) [0, 1]" << endl;
  while ( n1 % 2 != 0 ) {
    cout << "Enter number of intervals desired for trapezoidal rule (must be even)" << endl;  
    cin >> n1;
  }
  double a = 0;
  double b = 1;
  double ans1 = trapezoid(exp, a, b, n1);
  cout << "Trapezoidal rule : " << ans1 << endl;


  double ans2 = adaptive_trapezoid( exp, a, b, 0.0001);
  cout << "Adaptive trapezoidal rule : " << ans2 << endl;

  double ans3 = simpson(exp, a, b, n1);
  cout << "Simpson rule : " << ans1 << endl;
}
