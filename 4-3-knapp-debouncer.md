# Mer om knappar

## Bounce
När en knapp trycks ned, kommer den inte omedelbart att byta från ett tillstånd till ett annat. På grund av små mekaniska vibrationer kommer det att uppstå en kort period av brus innan den helt når sitt nya tillstånd. Detta sker för snabbt för att vi människor ska kunna upptäcka det, men det upptäcks enkelt av ESP32. Fenomenet kallas på engelska för bounce (vi kan kalla det för studs på svenska om ni vill). En illustration av fenomenet finns [här](https://drive.google.com/file/d/124oR_-2_3roh63s1_rpgc7Ng7KkmPZ5h/view?usp=sharing).

Om vi som förut bara vill att LED:en ska lysa när knappen hålls intryckt så stör inte bounce, utan det märks inte. Om vi däremot endast trycker på knappen en gång, för att exempelvis sätta igång en LED, så kan det ställa till problem. Eftersom att knappens tillstånd är lite oklart precis i början så kan det tolkas lite slumpmässigt som att du har tryckt in knappen eller inte. Hur vi löser detta ser du nedan.

## Debounce
För att lyckas läsa av rätt tillstånd på knappen måste vi implementera ett system för debounce (motverka studs). Vi gör det genom att kolla om knappen är nedtryckt, vänta en kort stund och sedan kolla igen. Om knappen fortfarande är nedtryckt så kan vi slå på/stänga av LED:en. Tiden man väntar är tillräcklig för att bounce (studsen) ska ha gått över och knappens tillstånd ska vara stabilt. Stunden man väntar är dock så kort att en människa inte kommer att trycka på knappen kortare, vilket gör att det inte märks på något sätt för användaren.