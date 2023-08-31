//First experimental libtorch file
//Creates a new torch::Tensor and prints it

#include <torch/torch.h>
#include <iostream>

// /space/hall5/sitestore/eccc/crd/ccrn/users/rau001/Pytorch_and_Torchlib_programs/testing/libtorch/include/torch/csrc/api/include/torch

int main() {
  torch::Tensor tensor = torch::rand({2, 3});
  std::cout << tensor << std::endl;
  return 0;
}
