# Knapp introduktion

## Digital output

Vi har ju tidigare programmerat LED-lampor. Vi har då använt oss av pins på mikrokontrollen för att ge output. Vi har definierat detta i kod, och sedan använt digitalWrite(). Vi har använt digital output, det vill säga den har två lägen. Antingen är den 1 (HIGH) eller 0 (LOW).

## Digital input

Digital input betyder att vi har 1 eller 0, HIGH eller LOW. Pinnen kommer då att känna av spänningen. Om spänningen är hög, nära max (i vårt fall 3,3V) kommer den läsas som 1/HIGH, om den däremot är nära 0 kommer den att läsas som 0/LOW. Vi sätter en pin till input genom att använda pinMode(PIN, INPUT). Vi läser av pinnen genom att använda digitalRead(PIN) som då kan ge HIGH eller LOW.

## Knapp

En knapp är en strömbrytare, antingen släpper den igenom strömmen eller så gör den inte det. Knappen har fyra pins. De är ihopkopplade med varandra i par. Om knappen är nedtryck kommer de två sidorna vara ihopkopplade, och strömmen kan gå igenom. Om den inte är nedtryckt kan strömmen inte passera och kretsen är bruten. För en bild på hur knappen är uppdelad i två sidor, se [här](https://drive.google.com/file/d/1nwq42M8LVgZetJSkh4qSrZjrc4byYYDu/view?usp=drive_link).

Om vi kopplar en väldigt enkel krets (se exempel) där knappen är kopplad till en pin som tar input och GND så kan vi resonera på följande sätt. Om knappen är intryckt så går strömmen genom knappen till GND, vilket resulterar i att spänningen blir mycket låg. Om knappen är intryckt kommer vi alltså att läsa av värdet LOW från pinnen. Om knappen däremot inte är intryckt vill vi istället att värdet ska bli HIGH, att spänningen ska bli nära 3,3V. Detta är dock lite komplicerat.

## Flytande pins (floating pins)
När knappen inte är intryckt så kan spänningen som pinnen läser av fluktuera lite beroende på utomstående faktorer. Detta kallas för flytande pin (floating pin). Det kan leda till att värdet som läses av växlar lite mellan HIGH och LOW, vilket till exempel kan få en lampa som styrs av knappen att flickra. Detta löses genom en pull-up resistor.

## Pull-up resistor
Idén med en pull-up resistor är att se till att när knappen inte är intryckt så ska spänningen hållas hög. Vi löser detta genom att koppla knappens ena sida (som inte är kopplad till GND) till den positiva sidan av kopplingsbrädan (se exempelkrets). För att det inte ska gå så mycket ström kopplar vi också in en resistor (så kallad pull-up resistor). Vanligtvis har den en styrka på 10 k$\Omega$. Resultatet blir att när knappen inte är intryckt så kommer input-värdet att konstant vara HIGH, vilket ger en mer förutsägbar situation att använda i programmeringen av exempelvis LED.

Om vi bryter ner hur ovanstående exempelkrets fungerar så händer följande:
* Om knappen är intryckt kommer strömmen att gå via knappen till GND, och därmed blir spänningen mycket låg. Väldigt lite ström (nästan ingen) väljer vägen via den ganska starka resistorn.
* Om knappen inte är intryckt kommer strömmen att gå via resistorn, som ju är kopplad till 3,3V. Spänningen blir hög, men det krävs inte så mycket ström tack vare resistorn.

## Inbyggd pull-up
Nu när ni har sett hur en vanlig resistor kan användas så kan ni få veta att det finns ett enklare sätt. På vår mikrokontroller finns nämligen en inbyggd funktion så att man kan tala om att pinnen ska vara pull-up, det vill säga att dess default ska vara HIGH. Detta görs såhär: pinMode(PIN, INPUT_PULLUP).