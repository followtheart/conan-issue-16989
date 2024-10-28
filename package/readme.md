
create the `libtorch` package with data

```
cd package
conan build . -pr:a .\profile
conan export-pkg . -pr:a .\profile
``` 