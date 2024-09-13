#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define DEMO_EXPORT __declspec(dllexport)
#else
  #define DEMO_EXPORT
#endif

DEMO_EXPORT void demo();
DEMO_EXPORT void demo_print_vector(const std::vector<std::string> &strings);
