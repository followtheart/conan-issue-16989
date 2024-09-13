# conan-issue-16989
here is demo of conan-issue-16989

The demo has two part:
- The directory `package`,which contains a dll(`dll/libxxx.dll`) with data(`data/data.dat`)
- The directory `consumer`,which contains a `cmake_exe` package and will using the package `libxxx`
- The directory `cmake-conan-demo`,which is a `cmake_exe` package;and using `cmake-conan` to cooperate with `cmake`
- To reproduce my case:

    First,create the `libxxx` package with data
    ```
    cd package
    conan build . -pr:a .\profile
    conan export-pkg . -pr:a .\profile
    ``` 
    then,failed on(`find_pacakge`,but working on `include`[`CMakeLists.txt`](consumer/CMakeLists.txt)):
    ```
    cd ../consumer
    conan build . -pr:a .\profile  # here,failed!
    ```
    and failed both `find_package` and `include`[`CMakeLists.txt`](cmake-conan-demo/CMakeLists.txt):
    ```
    cd cmake-conan-demo
    cmake -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=".\conan_provider.cmake" -DCONAN_BUILD_PROFILE=default -DCONAN_HOST_PROFILE=default .
    ```
