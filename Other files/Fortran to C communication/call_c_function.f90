!Program to commnicate with C

program  callFunction
    use iso_c_binding
    implicit none
    


    interface
    subroutine func_test(seed, n, x) bind(c)
    import c_int, c_double
    integer(kind=c_int), intent(in), value :: seed, n
    real(kind=c_double)                    :: x(n)
    end subroutine normal_vec
    end interface


end program  callFunction

