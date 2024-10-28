#include "consumer.h"
#include <vector>
#include <string>
//#include "torch/script.h"
//#include "torch/torch.h"
#include "torch-test.h"
int main() {
    consumer();
    test_torch();
    std::vector<std::string> vec;
    vec.push_back("test_package");

    consumer_print_vector(vec);
}
