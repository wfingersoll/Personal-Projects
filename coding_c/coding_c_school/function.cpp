#include <iostream>

using namespace std;

//Author: William Ingersoll


//This function swaps the two values using pointers and an intermediary variable
void swaplnts(int *num1, int *num2){
    int num3;
    num3 = *num1;
    *num1 = *num2;
    *num2 = num3;

}

//Our main function takes in two inputs, then swaps and outputs them using a function
int main(){


    int num1;
    int num2;

    cout << "Enter First Number: ";
    cin >> num1;
    cout << "Enter Second Number: ";
    cin >> num2;

    cout << "Prior to swapping, the first number is: " << num1 << ", and the second number is: " << num2 << "." << endl; 

    swaplnts(&num1, &num2);

    cout << "After swapping, the first number is: " << num1 << ", and the second number is: " << num2 << "." << endl; 

    return 0;

}