//#include <torch/torch.h>
//#include <Python.h>

#include <iostream>
#include <Python.h>

#include <functional>
#include <cstdlib>

//using namespace std;

extern "C++" void libtorch_func(int *result){
    
    std::string cmnd;
    std::string prgm_path = "/space/hall5/sitestore/eccc/crd/ccrn/users/rau001/Pytorch_and_Torchlib_programs/testing/Fortran-Resnet/pt_file_creator.py";
    cmnd = "python3 " + prgm_path;

    int sysResult = system(cmnd.c_str());

    if(sysResult != 0){
      std::cout << "Exit code was:" << sysResult << std::endl;
    }

    *result = sysResult;
}

// extern "C" void add(int *usr_input, int *arr_size, int *result){
    
//     int temp_result = py_call();

//     int size_of_arr = *arr_size;
        
//     for (int i = 0; i < size_of_arr; i++)
//     {
//         temp_result += usr_input[i];
//     }
//     *result = temp_result;
    
// }