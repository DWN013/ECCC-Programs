# Version being used by HPC is 3.11.4
cmake_minimum_required(VERSION 3.11 FATAL_ERROR)
# Project(${PROJECT_NAME})
project(pytorch-app)

# Find Torch package
find_package(Torch REQUIRED)
# cxx is also C++
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

# Add libtorch_example.cpp file to project
add_executable(pytorch-app libtorch_example.cpp)
# Ensure libtorch_example.cpp can use torch
target_link_libraries(pytorch-app "${TORCH_LIBRARIES}")
set_property(TARGET pytorch-app PROPERTY CXX_STANDARD 17)

# To run cmake cmnd to setup build:
# cmake -DCMAKE_PREFIX_PATH=/space/hall5/sitestore/eccc/crd/ccrn/users/rau001/bin/envs/climart_gn/lib/python3.10/site-packages/torch/share/cmake ..

# Absolute path to libtorch/cmake
# /space/hall5/sitestore/eccc/crd/ccrn/users/rau001/bin/envs/climart_gn/lib/python3.10/site-packages/torch/share/cmake

# To run cmake cmnd to setup build:
# cmake -DCMAKE_PREFIX_PATH=/space/hall5/sitestore/eccc/crd/ccrn/users/rau001/bin/envs/climart_gn/lib/python3.10/site-packages/torch/share/cmake ..

# Assuming successful execution of previous statement
# cmake --build . --config Release
