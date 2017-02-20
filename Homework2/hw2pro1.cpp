#include <iostream>
#include <cmath>
#include <limits>

int main(){
  float x1, y1, x2, y2;
  float tolerance = 0.01f;
  float slope, midx, midy, yintercept, pslope, pyintercept;
  std::cin >> x1 >> y1 >> x2 >> y2;
  if (std::abs(x1-x2)>tolerance){
    if (std::abs(y1-y2)>tolerance){
       slope = (y2-y1)/(x2-x1);
       midx = 0.5*(x1+x2);
       midy = 0.5*(y1+y2);
       yintercept = slope*x1+y1;
       pslope = -1/slope;
       pyintercept = pslope*x1+y1;
       std::cout << "the midpoint is " << "(" << midx << ", " << midy << ")" << std::endl;
       std::cout << "its slope is " << slope << std::endl;
       std::cout << "y-intercept is " << yintercept << std::endl;
       if (yintercept < 0){
         std::cout << "the equation of this line is y=" << slope << "x" << yintercept << std::endl;
       }
       else
         std::cout << "the equation of this line is y=" << slope << "x+" << yintercept << std::endl;
       if (pyintercept <0){
         std::cout << "and the equation of the line perpendicular to this one passing through the first point is y=" << pslope << "x" << pyintercept << std::endl;
       }
       else
         std::cout << "and the equation of the line perpendicular to this one passing through the first point is y=" << pslope << "x+" << pyintercept << std::endl;
    }
    else
      std::cout << "Nuke!" << std::endl;
    }
  else
    std::cout << "Nuke!" << std::endl;
  return 0;
}
