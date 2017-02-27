#include <iostream>
#include <cmath>

float factorial(int n){
  float result=1;
  if (n==0){
    result=1;
  }
  else if (n>0 && n<20){
    for (int i=1; i<=n; i++){
      result=result*i;
    }
  }
  return result;
}

float Stirling(int l){
  float approx=l*log(l)-l;
  float result=exp(approx);
  return result;
}


int main(){
  int n;
  std::cout << "Input the number you want to calculate(should be bigger than 0): " << std::endl;
  std::cin >> n;
  while(n<0){
    std::cout << "Your input is invalid, please input again." << std::endl;
    std::cin >> n;
  }
  
  if (n>=0 && n<20){
    std::cout << "Factorial of " << n << " is " << factorial(n) << std::endl;
  }
  else if (n>=20){
    std::cout << "Factorial of " << n << " is " << Stirling(n) << std::endl;
  }
  return 0;
}
