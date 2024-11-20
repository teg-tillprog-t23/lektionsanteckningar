# Analog output
Vi har tidigare pratat om digital output (lampa som är tänd eller släckt), digital input (knapp som är nedtryckt eller uppsläppt) och analog input (potentiometer). Nu ska vi prata om analog output. Analog innebär ju att vi har en mer kontinuerlig skala, som en våg, istället för bara 1 eller 0. Det som händer vid analog output är att vi vill mata ut en lägre effekt för ett lägre värde. Det kan vi göra på två sätt:

1. DAC - digital to analog converter. Den konverterar digitala signaler från processorn till analoga. Detta går endast att göra på två pinnar (de som är märkta med DAC_1 och DAC_2 på pin-kartan). Vi kommer därför inte att använda detta sätt.
2. PWM - pulse width modulation

## PWM

PWM är en teknik för att få till analog output utifrån digitala signaler. De analoga signalerna är antingen på eller av, 1 eller 0. Vi kan dock simulera analoga signaler genom att justera hur stor del av tiden som en digital signal är 0 och hur stor del av tiden den är 1. Det som sker är att ju längre del av tiden som signalen är på (1) desto högre effekt matas ut, desto närmare hamnar vi maximala spänningen (3,3 V i vårt fall). 

Outputen sker med en viss frekvens (ofta hög). Varje period av den frekvensen kan vi välja att ha på en viss andel av tiden och av en viss andel av tiden. Den andel av tiden som signalen är på (1) kallas för "duty cycle" (pulskvot på svenska). Om vi har 100% pulskvot så kommer signalen alltid att vara på (1) och om vi har 0% pulskvot kommer signalen alltid att vara av (0).

Om vi tänker oss att vi skulle använda PWM för att styra hur starkt en LED lyser så kommer det i själva verket vara så att den "blinkar" eftersom att signalen växlar mellan på och av. Dock sker detta så snabbt, så istället så uppfattar vi blinkningarnas olika hastighet som att LED:en lyser olika starkt.

För att se PWM illustrerat i bild, se [bild på olika pulskvoter](https://drive.google.com/file/d/1s0fCoraiLtegM5yp4N9vaVZZpFCW-Bjj/view?usp=sharing) och [annan bild på olika pulskvoter](https://drive.google.com/file/d/1Y5TFwv2wkzQvkzVnEBBtC8FankZraWZT/view?usp=sharing).

## PWM för ESP32

I arduino finns en analogWrite(), men den kommer vi inte att använda för den är kopplad till DAC.

Vi kommer att använda oss av ledcAttach() och ledcWrite(), två funktioner som är utvecklade för att kunna justera styrkan på en LED med PWM. För att detta ska fungera även i VS Code behöver man ändra i sin platformio.ini-fil i sitt projekt så att processorn är annorlunda, då Platform IO inte är helt uppdaterat. Detta är dock redan gjort i repot från Github som ni kommer att få arbeta med under dagens lektion. Raden som ska ändras är att på platform ska det stå: "platform = https://github.com/pioarduino/platform-espressif32/releases/download/51.03.07/platform-espressif32.zip"

Information om ledcAttach() och ledcWrite() finns inte i Arduino dokumentationen, utan den finns i [dokumentation från Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/ledc.html).