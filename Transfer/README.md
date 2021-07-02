# 107transfer

In mathematics and computer science, Horner's method (or Horner's scheme) is an algorithm for polynomial evaluation.
After the introduction of computers, this algorithm became fundamental for computing efficiently with polynomials.
This allows the evaluation of a polynomial of degree n with only n multiplications and n additions. This is optimal, since there are polynomials of degree n that cannot be evaluated with fewer arithmetic operations.

# mathematical formula example
```
P(x) =anx^n + ... + a2x^2 +a1x +a0
     =(anx^(n−1) + ... + a3x + a2 +a1) x+ a0
     = (...(((anx + an−1)x + an−2)x + an−3)...)x + a0
```

```
                   \\\||||||////
                   \\  ~ ~  //
                    (  @ @  )
 ________________ oOOo-(_)-oOOo_____________________
|          _                                       |                             
|         | |                                      |
|         | |__   ___  _ __ _ __   ___ _ __        |
|         | '_ \ / _ \| '__| '_ \ / _ \ '__|       |
|         | | | | (_) | |  | | | |  __/ |          |
|         |_| |_|\___/|_|  |_| |_|\___|_|          |
|_______________________Oooo.______________________|
              .oooO     (   )
               (   )     ) /
                \ (     (_/
                 \_)
```