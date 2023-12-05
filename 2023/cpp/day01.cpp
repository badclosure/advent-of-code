#include <fstream>
#include <iostream>

int main() {
  std::ifstream input_file;
  input_file.open("../input/day01.txt");
  if (!input_file) {
    std::cout << "Error reading input file." << std::endl;
  }
}
