#include <iostream>
using namespace std;


//Author: William Ingersoll


class arrayLoops{

    //this sets up the array we will be using to store user numbers.
    public:
       int nums[9];

    
    //This is an insertion sort algorithim that sorts the num array
    void sort(){
        for(int i = 0; i < 10; i++){
            int piv = nums[i];
            int j = i - 1;
            while(j >= 0 && nums[j] > piv){
                nums[j+1] = nums[j];
                j-=1;
            }
            nums[j+1] = piv;

        }
    }

};

//This is our main function
int main(){
    arrayLoops loop;

    //Takes in ten user responses and saves to nums array           
    for(int i = 0; i < 10; i++){
        cout << "Please enter your number: ";
        cin >> loop.nums[i];
    }

    //prints out the nums the user entered
    cout << "\nUnsorted array: " << endl;
    for(int i = 0; i < 10; i++){
        cout << loop.nums[i];
        cout << " ";
    }

    //sort the nums
    loop.sort();

    //prints out the sorted nums the user entered
    cout << "\nSorted array: " << endl;
    for(int i = 0; i < 10; i++){
        cout << loop.nums[i];
        cout << " ";       
    }

    return 0;

}