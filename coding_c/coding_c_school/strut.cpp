#include <iostream>
#include <cmath>

using namespace std;

//Author: William Ingersoll

//The structure for a point, contains an x and y int.
struct Point{
    int x;
    int y;
};

//The function for calculating distance. Takes in two point pointers and uses the euclidian distance formula to calculate the distance as a double.
double calculateDistance(Point *p1, Point *p2){
    int resultx = pow(((*p2).x - (*p1).x), 2);
    int resulty = pow(((*p2).y - (*p1).y), 2);
    double result = sqrt(resultx + resulty);

    return result;
};

//The main function creates two point objects and takes in four inputs, outputting the result of the caluclate distance function.
int main(){
    struct Point p1, p2;
    cout << "Enter x value of first point: ";
    cin >> p1.x;
    cout << "Enter y value of first point: ";
    cin >> p1.y;

    cout << "Enter x value of second point: ";
    cin >> p2.x;
    cout << "Enter y value of second point: ";
    cin >> p2.y;

    cout << "The distance is : " << calculateDistance(&p1, &p2) << endl;

    return 0;
}