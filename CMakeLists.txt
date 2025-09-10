cmake_minimum_required(VERSION 3.16 FATAL_ERROR) # Policies <= CMP0097 default to NEW

project(test_sqlitebrowser)

include(cmake_tools/entry/desktop-cpp.cmake)
__install_conan_requirements(MSVC_RUNTIME "dynamic")

add_subdirectory(SQLiteCpp)
add_subdirectory(sqlitebrowser)

