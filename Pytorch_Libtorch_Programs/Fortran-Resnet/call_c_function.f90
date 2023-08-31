!! Fortran program to call a C function directly
!! Ukhin, A
!! June 21, 2023

program  callFunction
    use iso_c_binding
    implicit none
    
    !integer :: inp_arr(5) = (/1, 2, 3, 4, 5 /)
    !integer :: arr_size = size(inp_arr)
    integer :: result

!    interface
!        subroutine add(inp_arr, arr_size, result) bind(c)
!        import c_int
!        integer(kind=c_int) :: arr_size
!        integer(kind=c_int), intent(in) :: inp_arr(arr_size)
!        integer(kind=c_int) :: result
!        end subroutine add
!    end interface


    interface
        subroutine call_model(result) bind(c)
        import c_int
        integer(kind=c_int) :: result
        end subroutine call_model
    end interface

    call call_model(result)
    !call add(inp_arr, arr_size, result)
    !print *, "Final result:", result

end program callFunction