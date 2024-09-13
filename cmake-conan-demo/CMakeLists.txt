project(demo CXX)

find_package(zlib)  # for trigger cmake-conan  install


#find_package(libxxx)   # fails here
include(libxxxConfig)   # fails here too


add_executable(demo src/demo.cpp src/main.cpp)

