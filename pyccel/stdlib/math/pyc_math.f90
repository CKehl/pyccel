module pyc_math

    implicit none

        real(kind=8), parameter, private :: pi = 4.D0 * DATAN(1.D0)

    contains

        ! Implementation of math factorial function
        function pyc_factorial(x) result(fx)

            implicit none
            integer(kind=8), value  :: x
            integer(kind=8)         :: fx

            fx = 1
            do while (x > 0)
                fx = fx * x
                x = x - 1
            enddo
            return

        end function pyc_factorial

        ! Implementation of math gcd function
        function pyc_gcd(a, b) result(gcd)

            implicit none
            integer(kind=8), value  :: a
            integer(kind=8), value  :: b
            integer(kind=8)         :: gcd

            do while (b > 0)
                a = MOD(a, b)
                a = XOR(a, b)
                b = XOR(b, a)
                a = XOR(a, b)
            enddo
            gcd = a
            return

        end function pyc_gcd

        ! Implementation of math lcm function
        function pyc_lcm(a, b) result(lcm)

            implicit none
            integer(kind=8), value :: a
            integer(kind=8), value :: b
            integer(kind=8)        :: lcm

            lcm = a / pyc_gcd(a, b) * b
            return

        end function pyc_lcm

        ! Implementation of math radians function
        function pyc_radians(deg) result(rad)

            implicit none
            real(kind=8), value     :: deg
            real(kind=8)            :: rad

            rad = deg * (pi / 180.0)
            return

        end function pyc_radians

        ! Implementation of math degrees function
        function pyc_degrees(rad) result(deg)

            implicit none
            real(kind=8), value     :: rad
            real(kind=8)            :: deg

            deg = rad * (180.0 / pi)
            return

        end function pyc_degrees

end module pyc_math