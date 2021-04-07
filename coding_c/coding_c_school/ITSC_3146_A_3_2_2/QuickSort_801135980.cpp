//
//  QuickSort_Skeleton.cpp
//
//  Created by Bahamon, Julio on 6/25/19.
//  UNC Charlotte
//  Copyright © 2019 Bahamon, Julio. All rights reserved.
//


//Finalized by William Ingersoll

#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

//  Declaring a new struct to store patient data
struct patient {
    int age;
    char name[20];
    float balance;
};


//The comparison function takes two specific elements of the patient_list array, and compares specific elements of them, returning the relevant result.
int compareAge(const void* a, const void* b){

    struct patient* patient1 = (struct patient*)a;
    struct patient* patient2 = (struct patient*)b;
  

    if(patient1->age < patient2->age){
        return -1;
    }
    else if(patient1->age > patient2->age){
        return 1;
    }
    else{
        return 0;
    }
    

}



//Compare balance works identically to the compare age function, just substituting age for balance
int compareBalance(const void* a, const void* b){

    struct patient* patient1 = (struct patient*)a;
    struct patient* patient2 = (struct patient*)b;
  

    if(patient1->balance < patient2->balance){
        return -1;
    }
    else if(patient1->balance > patient2->balance){
        return 1;
    }
    else{
        return 0;
    }
    

}

//The compare name function is the simplest, since the strcmp function does the comparison for us, so we just return the result of that.
int compareName(const void* a, const void* b){

    struct patient* patient1 = (struct patient*)a;
    struct patient* patient2 = (struct patient*)b;
  
    return strcmp(patient1->name, patient2->name);
    

}


//  The main program
int main()
{
    int total_patients = 5;
    
    //  Storing some test data
    struct patient patient_list[5] = {
        {25, "Juan Valdez   ", 1250},
        {15, "James Morris  ", 2100},
        {32, "Tyra Banks    ", 750},
        {62, "Maria O'Donell", 375},
        {53, "Pablo Picasso ", 615}
    };
    
    
    cout << "Patient List: " << endl;

    for(int i = 0; i < 5; i++){
        cout << "       Age: " << patient_list[i].age << "         Name: " << patient_list[i].name << "        Balance Due: " << patient_list[i].balance << endl;
    }
    
    cout << endl;
    
    
    cout << "Sorting..." << endl;
    

    //For each sorting method it is a simple call to qsort like the one below, only changing which comparator is called
    qsort(patient_list,5,sizeof(struct patient),compareAge);
    
    cout << "Patient List - Sorted by Age: " << endl;

    //A simple for loop to print out the patient list
    for(int i = 0; i < 5; i++){
        cout << "       Age: " << patient_list[i].age << "         Name: " << patient_list[i].name << "        Balance Due: " << patient_list[i].balance << endl;
    }

    cout << endl;
    
    
    cout << "Sorting..." << endl;


     qsort(patient_list,5,sizeof(struct patient),compareBalance);
    
    cout << "Patient List - Sorted by Balance Due: " << endl;
    
    

    
    for(int i = 0; i < 5; i++){
        cout << "       Age: " << patient_list[i].age << "         Name: " << patient_list[i].name << "        Balance Due: " << patient_list[i].balance << endl;
    }

    cout << endl;
    
    
    cout << "Sorting..." << endl;


    qsort(patient_list,5,sizeof(struct patient),compareName);
    
    cout << "Patient List - Sorted by Name: " << endl;
    

    for(int i = 0; i < 5; i++){
        cout << "       Age: " << patient_list[i].age << "         Name: " << patient_list[i].name << "        Balance Due: " << patient_list[i].balance << endl;
    }
    
    cout << endl;
    
    return 0;
}
