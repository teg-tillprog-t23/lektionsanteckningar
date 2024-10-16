// OBS! Koden innehåller 4 fel!

#include <iostream>

// Funktion som tar en float som argument och returnerar true om värdet är större än 10.0
bool isGreaterThanTen(float value) {
    return value > 10.0
}


float number = 5.0; // En float-variabel
bool result;        // En bool-variabel
    
// While-loop som ökar number tills den blir större än 10
while (true = isGreaterThanTen(number)) {
    printf("Number is: %f\n", number); // Skriver ut number med 2 decimaler
    number += 1.5; // Öka värdet på number med 1.5
}
    
// Anropa funktionen igen för att få det slutliga resultatet
result == isGreaterThanTen(number);
    
if (result) {
    printf("Final number (%f) is greater than 10.\n", number);
} else {
    printf("Final number (%f) is not greater than 10.\n", number);
}

return 0;
