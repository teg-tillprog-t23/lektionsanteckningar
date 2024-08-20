// Introduktion till C++

// C++ är ett språk som är en vidareutveckling av C
// Vi kommer att använda en enklare version, som är anpassad för att arbeta med mikrokontrollers, men vi börjar med lite vanlig C++

/* Syntaxen i C++ är väldigt lik C, men C++ kan användas som ett objektorienterat språk precis som Python
Med det menas att det går att skriva klasser i C++ (som vi ju testade lite kort i Python förra året)*/

/* C++ är ett kompilerat språk, vilket gör att det kompileras först, och körs sen. Vid Python görs detta istället varteftersom.
Det innebär att C++ tar längre tid innan det startar, men när det väl är kompilerat så går det snabbare.*/

/* C++ är också statiskt typat, vilket innebär att vi vet variabeltyperna när programmet kompileras. 
 Vi behöver därför tydligt tala om vilken typ en variabel har när vi skapar den.
 Python är istället dynamiskt typat. */

// När vi vill programmera i C++ skapar vi en fil på formatet "filnamn.cpp" (cpp = cplusplus)

// Om vi vill kommentera en rad gör vi såhär
/* Vi kan också göra såhär,
för då kan vi skriva på fler rader. */

// Vi behöver alltid ha en main-funktion

int main(){ // vi behöver i början bestämma vilken typ funktionen ska returnera
    return 0;
} // Vi använder ; och {}, indenteringen spelar ingen roll, utan används endast för att det blir mer lättläst


// För att skriva ut text kan vi använda printf()
// Vi behöver då inkludera ett bibliotek #include <iostream>;

// Datatyper: int, double, string, bool

// if/else if/else
/*if (villkor){}*/

// while-loop
/* while(villkor){}*/


// for-loop
/* for (int i = 0; i < 5; i++) {
  printf("Här är talet: %d \n";
}*/

/* %d för helttal, %f för decimaltal, %s för string*/

// listor = arrays
/* string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
*/


// Funktioner
/* Behöver som sagt deklarera vilken typ returvärdet kommer att vara. Om man inte vill returnera blir det void.
Vi kan ha flera parametrar, men vi behöver deklarera deras typ.
Att returnera flera värden är lite komplicerat, så det väntar vi med då det inte är säkert att det kommer att behövas.*/