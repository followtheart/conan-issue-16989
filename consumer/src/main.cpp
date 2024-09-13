#include "consumer.h"
#include <vector>
#include <string>

int main() {
    consumer();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    consumer_print_vector(vec);
}
