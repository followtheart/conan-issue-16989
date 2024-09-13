#include "demo.h"
#include <vector>
#include <string>

int main() {
    demo();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    demo_print_vector(vec);
}
