//Calls a Python file from C++
// /fs/site5/eccc/crd/ccrn/users/rau001/Pytorch_and_Torchlib_programs/testing/PytorchConnect

#include <torch/torch.h>
#include <iostream>
#include <cstdlib>

int main() {
  //torch::Tensor tensor = torch::rand({2, 3});
  //std::cout << tensor << std::endl;
  
  std::string cmnd;
  //Insert Python program to be called here
  // /insert/path/to/file/here.py
  std::string prgm_path = "/fs/site5/eccc/crd/ccrn/users/rau001/Pytorch_and_Torchlib_programs/testing/PytorchConnect/pt_file_creator.py";
  //Definition for calling Python program in cmnd line
  cmnd = "python3 " + prgm_path;
    
  //Exectutes python program
  int result = system(cmnd.c_str());

  //endl same as calling '\n' and flushing
  if(result != 0){
      std::cout << "Exit code was:" << result << std::endl;
  }

  return 0;
}