# conan-issue-16989
here is demo of conan-issue-16989

The demo has two part:
- The directory `package`,which contains a dll(`dll/libxxx.dll`) with data(`data/data.dat`)
- The directory `consumer`,which contains a `cmake_exe` package and will using the package `libxxx`
- To reproduce my case:
    First,create the `libxxx` package with data
    ```
    cd package
    conan build . -pr:a .\profile
    conan export-pkg . -pr:a .\profile
    ``` 
    then,
    ```
    cd ../consumer
    conan build . -pr:a .\profile  # here,failed!
    ```
    error log:
    ```
    -- Detecting CXX compile features - done
    -- Conan: Target declared 'libxxx::libxxx'
    CMake Error at build/generators/cmakedeps_macros.cmake:67 (message):
    Library 'libxxx' not found in package.  If 'libxxx' is a system library,
    declare it with 'cpp_info.system_libs' property
    Call Stack (most recent call first):
    build/generators/libxxx-Target-release.cmake:23 (conan_package_library_targets)
    build/generators/libxxxTargets.cmake:24 (include)
    build/generators/libxxx-config.cmake:16 (include)
    CMakeLists.txt:3 (find_package)


    -- Configuring incomplete, errors occurred!
    ```
