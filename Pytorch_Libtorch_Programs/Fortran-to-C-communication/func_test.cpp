//#include <torch/torch.h>
#include <functional>
#include <cstdlib>

//using namespace std;

extern "C" void add(int *usr_input, int *arr_size, int *result){
    
    int temp_result = 0;

    int size_of_arr = *arr_size;
        
    for (int i = 0; i < size_of_arr; i++)
    {
        temp_result += usr_input[i];
    }
    *result = temp_result;
    
}