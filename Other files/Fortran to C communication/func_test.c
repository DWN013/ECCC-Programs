#include <stdio.h>

int add(int usr_input[], int size_of_arr)
{   
    int temp_result = 0;
    for (int i = 0; i < size_of_arr; i++)
    {
        temp_result += usr_input[i];
    }
    return temp_result;
}

int main() {
    
    int test_arr[] = {1, 2, 3, 4, 5};
    int size_of_arr = sizeof(test_arr)/sizeof(test_arr[0]);
    int result = 0;
    
    result = add(test_arr, size_of_arr);
    
    printf("%d", result);

    return 0;
}