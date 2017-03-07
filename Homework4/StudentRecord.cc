#include "StudentRecord.h"
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>

StudentRecord::StudentRecord( std::string lastname, std::string firstname, float score ){
  lastname_=lastname;
  firstname_=firstname;
  score_=score;
}
StudentRecord::~StudentRecord(){};

void StudentRecord::print() const {
  std::cout << lastname_ << "," << firstname_  << "," << score_ << std::endl;
}

bool StudentRecord::input ( std::istream & in ) {   
    std::string line;   
    std::getline( in, line, ',');   
    lastname_ = line;   
    std::getline( in, line, ',');   
    firstname_ = line;   
    std::getline( in, line );
    score_ = std::atof( line.c_str() );   
    if ( line == "")      
       return false;   
    else     
       return true;
  }

std::string StudentRecord::lastname() const {return lastname_;}
std::string StudentRecord::firstname() const {return firstname_;}
float StudentRecord::score() const {return score_;}

StudentRecord & StudentRecord::operator>( StudentRecord const & right ){
  score_ > right.score_;
  return *this;
}

StudentRecord & StudentRecord::operator<( StudentRecord const & right ){
  score_ < right.score_;
  return *this;
}

StudentRecord & StudentRecord::operator>=( StudentRecord const & right ){
  score_ >= right.score_;
  return *this;
}

StudentRecord & StudentRecord::operator<=( StudentRecord const & right ){
  score_ <= right.score_;
  return *this;
}

