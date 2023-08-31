!> \file
!> \Program to call C++ libtorch
!!
!! A. Ukhin 
!! June 6, 2023

program call_cpp

implicit none
character(len = 256) :: file_path
character(len = 256) :: file_name
character(len = 512) :: cmnd

print *, "Input the file path to the C++ program:"
read(*, '(A256)') file_path

print *, "Input the compiled filename:"
read(*, '(A256)') file_name

!All at once
cmnd = "cd " // trim(file_path) // " && ./"
cmnd = trim(cmnd) // trim(file_name)


call execute_command_line(cmnd)

end program call_cpp