#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
MFRC522 mfrc522(10, 9);

void setup()
{
    Serial.begin(9600);

    lcd.begin(16, 2);
    lcd.backlight();
    lcd.clear();

    SPI.begin();
    mfrc522.PCD_Init();
}

void loop()
{
    if (Serial.available() > 0)
    {
        char buffer[1];
        Serial.readBytes(buffer, 1);
        display(buffer[0]);
    }
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())
    {
        String id = String(getID()) + '\n';
        Serial.print(id);
        mfrc522.PICC_HaltA();
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

unsigned int getID()
{
    unsigned int id = 0;
    for (int i = 0; i < 4; i++)
    {
        id << 8;
        id += mfrc255.uid.uidByte[i]
    }
    return id;
}
