#ifndef StudentRecord_h
#define StudentRecord_h

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

class StudentRecord {
 public:
  StudentRecord( std::string lastname = "", std::string firstname = "", float score = 0 );
  ~StudentRecord();

  void print() const;

  std::string lastname() const;
  std::string firstname() const;
  float score() const;

  bool input( std::istream & in );

  StudentRecord & operator>( StudentRecord const & right );

  StudentRecord & operator<( StudentRecord const & right );

  StudentRecord & operator>=( StudentRecord const & right );

  StudentRecord & operator<=( StudentRecord const & right );
  
  
 private:
  std::string lastname_;
  std::string firstname_;
  float score_;

};


#endif
