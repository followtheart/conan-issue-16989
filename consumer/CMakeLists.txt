cmake_minimum_required(VERSION 3.15)
project(consumer CXX)
find_package(libxxx)


add_executable(consumer src/consumer.cpp src/main.cpp)



install(TARGETS consumer DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
