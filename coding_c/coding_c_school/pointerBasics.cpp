#include <iostream>

using namespace std;

int main(){

    int myInt = 15;
    int* mypointer;
    mypointer = &myInt;

    cout << "The address of myInt is: " << &myInt << endl;
    cout << "The value of myPointer is: " << mypointer << endl;
    cout << "The value of myInt is: " << myInt << endl;
    cout << "The value pointed to by myPointer is: " << *mypointer << endl;

    myInt = 10;

    cout << "\nThe address of myInt is: " << &myInt << endl;
    cout << "The value of myPointer is: " << mypointer << endl;
    cout << "The value of myInt is: " << myInt << endl;
    cout << "The value pointed to by myPointer is: " << *mypointer << endl;

    return 0;
}