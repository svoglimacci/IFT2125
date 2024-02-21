//Simon Voglimacci Stephanopoli, 20002825
//Julie Yang, 20239909

#include "PrimeCalculator.h"
#include <stdio.h>
#include <vector>
#include <math.h>

// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class


PrimeCalculator::PrimeCalculator()
{

}

//https://en.wikipedia.org/wiki/Primality_test
bool isPrime(int N)
{
    if (N <= 1)
        return false;

    if (N == 2 || N == 3)
        return true;

    if ( N % 2 == 0 || N % 3 == 0)
        return false;

    for (int i = 5; sqrt(N) >= i; i += 6)
    {
        if (N % i == 0 || N % (i + 2) == 0)
            return false;
    }

    return true;
}

int PrimeCalculator::CalculateNthPrime(int N)
{
  int count = 0;
    int i;
    for (i = 2; ; i++)
    {
        if (isPrime(i))
        {
            count++;
            if (count == N)
                break;
        }
    }
    return i;
}
