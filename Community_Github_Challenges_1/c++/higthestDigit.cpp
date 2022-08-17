#include<iostream>
#include<string>

using namespace std;
//Highest digit
int highestDigit( int number ){
    string elements = to_string( number );
    int max = elements[0];
    for( int i = 1; i <= elements.size(); i++ ){
        if( elements[i] > max ){
            max = elements[i];
        }
    }
    return max - '0';
}

int main(int argc, char const *argv[]){
    //case input
    cout << highestDigit(1675446);
    return 0;
}
