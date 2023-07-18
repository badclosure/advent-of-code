#include <fstream>
#include <iostream>
#include <string>

int main() {
  std::ifstream infile("../input/day1.txt");

  int top[3];
  int cur = 0;

  std::string line;

  while (std::getline(infile, line)) {
    if (line.empty()) {
      if (top[0] < cur) {
        top[2] = top[1];
        top[1] = top[0];
        top[0] = cur;
      } else if (top[1] < cur) {
        top[2] = top[1];
        top[1] = cur;
      } else if (top[2] < cur) {
        top[2] = cur;
      }
      cur = 0;
      continue;
    }
    cur += std::stoi(line);
  }
  std::cout << "day1-part1: " << top[0] << std::endl;
  std::cout << "day1-part2: " << top[0] + top[1] + top[2] << std::endl;
  return 0;
}
