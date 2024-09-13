from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy
import os

class libxxxRecipe(ConanFile):
    name = "libxxx"
    version = "5.9.1"

    # package_type = "shared-library" 

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    def package(self):
        copy(self, "*.dat", os.path.join(self.build_folder, "data"), os.path.join(self.package_folder, "include"), keep_path=False)
        copy(self, "*.dll", os.path.join(self.build_folder, "dll"), os.path.join(self.package_folder, "bin"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs =["libxxx"]
        # self.cpp_info.bindirs = ["dll"]


