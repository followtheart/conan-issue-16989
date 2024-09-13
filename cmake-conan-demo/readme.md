#conan-cmake demo
- version `develop2`

***build fails with conan-cmake***

- `find_package(libxxx)`  # not working with [`cmake-conan`](https://github.com/conan-io/cmake-conan/tree/develop2)
- `include(libxxxConfig)`   #not working with [`cmake-conan`](https://github.com/conan-io/cmake-conan/tree/develop2)

To reproduce:
```
cd cmake-conan-demo
cmake -DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=".\conan_provider.cmake" -DCONAN_BUILD_PROFILE=default -DCONAN_HOST_PROFILE=default .
```