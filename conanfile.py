from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain

class LightMaker(ConanFile):
    settings = "os", "build_type"

    def requirements(self):
        self.requires("openssl/1.1.1w")
        self.requires("sqlite3/3.43.0")
        self.requires("gtest/1.15.0")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()
        cd = CMakeDeps(self)
        cd.generate()