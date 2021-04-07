#include <iostream>

using namespace std;

//Author: William Ingersoll

int main(){

    int my_ints[4];

    //After defining an array, we fill it with user input
    for(int i = 0; i < 4; i++){
        cout << "Enter number: ";
        cin >> my_ints[i];
    }

    //Here we define an array of pointers, and point each element to the element from the original array
    int* myptrs[4];
    for(int i = 0; i < 4; i++){
        myptrs[i] = &my_ints[i];
    }


    //This is a simple selection sort, just applied to an array of pointers
    int min;
    int* temp;

    for(int i = 0; i < 3; i++){
        min = i;
        for(int j = i+1; j < 4; j++)
            if(*myptrs[j]<*myptrs[min])
                min = j;
            temp = myptrs[min];
            myptrs[min] = myptrs[i];
            myptrs[i] = temp;
    }

    //Finally we print the array of pointers.
    for(int i = 0; i < 4; i++){
        cout << *myptrs[i];
    }    

    cout << endl;

    return 0;

}