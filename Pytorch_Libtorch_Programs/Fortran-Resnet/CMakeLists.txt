cmake_minimum_required(VERSION 3.11 FATAL_ERROR)
project(pytorch-app)

find_package(Torch REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
add_executable(pytorch-app resnet_model_reader.cpp)
target_link_libraries(pytorch-app "${TORCH_LIBRARIES}")
set_property(TARGET pytorch-app PROPERTY CXX_STANDARD 17)



# Absolute path to libtorch/cmake
# /space/hall5/sitestore/eccc/crd/ccrn/users/rau001/bin/envs/climart_gn/lib/python3.10/site-packages/torch/share/cmake

# To run cmake cmnd to setup build:
# cmake -DCMAKE_PREFIX_PATH=/space/hall5/sitestore/eccc/crd/ccrn/users/rau001/bin/envs/climart_gn/lib/python3.10/site-packages/torch/share/cmake ..

# Assuming successful execution of previous statement
# cmake --build . --config Release
