#include <torch/script.h>
#include <iostream>
#include <memory>

extern "C" void call_model(int *result) {
//int main() {

  // Deserialize scriptmodule from a .pt file
  torch::jit::script::Module module;
  const char *path_arg;
  path_arg = "/space/hall5/sitestore/eccc/crd/ccrn/users/rau001/Pytorch_and_Torchlib_programs/testing/Fortran-Resnet/traced_resnet_model.pt";
  module = torch::jit::load(path_arg);

  std::cout << "Model load OK\n";

  // After model is loaded
  // Create a vector of inputs.
  std::vector<torch::jit::IValue> inputs;
  inputs.push_back(torch::ones({1, 3, 224, 224}));

  // Execute the model and turn its output into a tensor.
  at::Tensor output = module.forward(inputs).toTensor();
  std::cout << output.slice(/*dim=*/1, /*start=*/0, /*end=*/5) << '\n';
}