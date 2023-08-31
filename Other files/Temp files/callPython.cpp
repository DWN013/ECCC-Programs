#include <iostream>
#include <cstdlib>

int main() {
    std::string cmnd;

    //Insert Python program to be called here
    // /home/rau001/Desktop/testRemotePython.py
    // /insert/path/to/file/here.py
    std::string prgm_path = "/home/rau001/Desktop/testRemotePython.py";
    std::string param1 = "SUCCESS!";
    //std::string param2;

    //Definition for calling Python program with a parameter
    cmnd = "python3 " + prgm_path + " " + param1;
    
    //Exectutes python program
    //int result = system(cmnd.c_str);
    int result = system(cmnd.c_str());

    //endl same as calling '\n' and flushing
    if(result != 0){
        std::cout << "Exit code was:" << result << std::endl;
    }

}