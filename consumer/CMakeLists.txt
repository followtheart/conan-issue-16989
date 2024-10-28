cmake_minimum_required(VERSION 3.15)
project(consumer CXX)


find_package(libtorch REQUIRED COMPONENTS c10 torch_cpu)  # not working `conan build` 
# include(libtorchConfig)   # working in `conan build`

add_executable(consumer src/consumer.cpp src/main.cpp)
target_link_libraries(consumer libtorch::torch_cpu libtorch::c10 )
message("####******************############:" ${TEST_DIR})

