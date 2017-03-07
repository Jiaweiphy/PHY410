#include <fstream>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include "StudentRecord.h"

float calculate_average(std::vector<StudentRecord> *pr){
    
    int size =0;
    int n = 0;
    size = pr -> size();
    double sum,average = 0;
    
    for ( n = 0; n < size ; ++n) {
        sum += pr -> at(n).score();
    }
    
    average = sum / size;
    return average;
    
}

int main ( int argc, char *argv[] ){

   StudentRecord testres;
   
   std::vector<StudentRecord> recordvec;
    
   std::ifstream in( argv[1] );

    
   while(testres.input(in)){
        
        recordvec.push_back(testres);
        
    }

   int vecsize = recordvec.size();

    if( argc == 2 ){
    
      for( int j = 0; j < vecsize; j++ ){
        recordvec.at(j).print();
      }
    
      double result =0;
    
      result = calculate_average( &recordvec );
    
      std::cout << "Average of this test is " << result << std::endl;
    }
    else if ( argc == 3 ){
    
      int index = atoi(argv[2]);
      if ( index > vecsize ) {
        std::cout << "There is no such index." << std::endl;
      }
      else
        recordvec.at(index-1).print();
    }
    else
      std::cout << "Invalid input." << std::endl;

    return 0;
    
}
