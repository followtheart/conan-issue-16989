#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define CONSUMER_EXPORT __declspec(dllexport)
#else
  #define CONSUMER_EXPORT
#endif

CONSUMER_EXPORT void consumer();
CONSUMER_EXPORT void consumer_print_vector(const std::vector<std::string> &strings);
