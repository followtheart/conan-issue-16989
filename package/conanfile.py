from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy
import os

class libtorchRecipe(ConanFile):
    name = "libtorch"
    version = "5.9.1"
    package_type = "shared-library"

    settings = "os", "compiler", "build_type", "arch"

    def package(self):
        # copy(self, "*.dat", os.path.join(self.build_folder, "data"), os.path.join(self.package_folder, "include"), keep_path=False)
        copy(self, "*.dll", os.path.join(self.build_folder, "dll"), os.path.join(self.package_folder, "bin"), keep_path=False)
        copy(self, "*.lib", os.path.join(self.build_folder, "lib"), os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*", os.path.join(self.build_folder, "include"), os.path.join(self.package_folder, "include"), keep_path=True)
        # copy(self,"*.cmake",os.path.join(self.build_folder, "cmake"),  os.path.join(self.package_folder, "cmake"), keep_path=False)  # Assuming CMake scripts are here

    
    def package_info(self):
        #pass
        # self.cpp_info.components["clog"].libs = ["clog"]
        self.cpp_info.components["c10"].libs = ["c10"]
        # self.cpp_info.components["c10"].requires = ["clog"]

        self.cpp_info.components["torch_cpu"].libs = ["torch_cpu"]
        self.cpp_info.components["torch_cpu"].requires = ["c10"]

        # self.cpp_info.components["torch"].libs = ["torch"]
        self.cpp_info.components["torch_cpu"].includedirs = ["include","include/torch/csrc/api/include"]
        # self.cpp_info.components["torch"].requires = ["torch_cpu"]        
        
        # self.cpp_info.builddirs = ["cmake"]


