/*
 @file: pthreads_skeleton.cpp
 
 @author: student name1, student2@uncc.edu
 @author: student name2, student2@uncc.edu
 @author: student name3, student3@uncc.edu
 
 @description: A program that demonstrates processes.
 
 @course: ITSC 3146
 @assignment: in-class activity [n]
 */

#include <pthread.h>
#include <iostream>
#include <algorithm>

using namespace std;

int numarray[10];

// This function shows the skeleton that pthread 
// functions must adhere to. 
// Copy this skeleton for any pthread function 
// you need to define. 
// In the copy, modify the name of the function 
// and the function body as needed. 
void *routineName(void *arg)
{
   // TODO: Add code that implements
   //       the thread's functionality
   cout << "Thread is running..." << endl;
   return 0;
}

void *countNegatives(void *arg){
   int total = 0;

   for(int i = 0; i < 10; i++){
      if(numarray[i]<0){
         total+=1;
      }
   }

   cout << "There are " << total << " negative numbers." << endl;
   return 0;
}

void *average(void *arg){
   double average;

   for(int i = 0; i < 10; i++){
      average += (double)numarray[i];
   }

   cout << "The average is: " << average/10.0 << "." << endl;
   return 0;
}

void *reverse(void *arg){
   reverse(numarray + 0, numarray + 10);

   cout << "The reversed array is: ";
   for(int i = 0; i < 10; i++){
      cout << numarray[i] << ", ";
   }
   return 0;
}

int main()
{
   // id is used to store a unique thread identifier,
   // returned by the call to create a new POSIX thread
   pthread_t id;
   
   // rc is used to store the code returned by the
   // call to create a new POSIX thread. The value is
   // zero (0) if the call succeeds.
   int rc;
   

   // TODO: Add code to perform any needed initialization
   //       or to process user input

   for(int i = 0; i < 10; i++){
      cout << "\nEnter Number: ";
      cin >> numarray[i];
   }
   
   

   // Create thread(s)
   // TODO: Modify according to assignment requirements
   rc = pthread_create(&id, NULL, countNegatives, NULL);
   rc = pthread_create(&id, NULL, average, NULL);
   for (int count = 0; count < 100000; count++);
   rc = pthread_create(&id, NULL, reverse, NULL);
   

   if (rc){
      cout << "ERROR; return code from pthread_create() is " << rc << endl;
      return -1;
   }
   

   // NOTE: Using exit here will immediately end execution of all threads
   pthread_exit(0);
}
