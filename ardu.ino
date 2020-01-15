#include <Wire.h>
#include <SoftwareSerial.h>
#include <LiquidCrystal_I2C.h>

SoftwareSerial uart(0, 1);
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

void setup()
{
    Serial.begin(9600);
    uart.begin(9600);

    lcd.begin(16, 2);
    lcd.backlight();
    lcd.setCursor(0, 0);
}

void loop()
{
    if (uart.available() > 0)
    {
        display(uart.read());
    }
}

void display(char c)
{
    switch (c)
    {
    case '\r':
        lcd.clear();
        break;
    case '\n':
        lcd.setCursor(0, 1);
        break;
    default:
        String s = "" + c;
        lcd.print(s);
        break;
    }
}
