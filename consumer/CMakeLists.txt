project(consumer CXX)


# find_package(libxxx)  # not working `conan build` 
include(libxxxConfig)   # working in `conan build`

add_executable(consumer src/consumer.cpp src/main.cpp)

message("####******************############:" ${TEST_DIR})

