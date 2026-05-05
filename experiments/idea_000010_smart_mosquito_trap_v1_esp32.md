# Smart Mosquito Trap v1 ESP32 Build Note

Canonical idea: `idea_000010` - AI-assisted smart mosquito trap

Status: draft experiment note. This is a low-voltage sensing and fan-control
prototype, not a high-voltage trap and not a capture-efficacy claim.

## Goal

Build the first version that actually moves:

```text
night mode + high humidity + mosquito-friendly temperature
-> ESP32 decides the condition is favorable
-> fan turns on for a bounded window
-> fan turns off automatically
```

The v1 win condition is stable control, not catching many mosquitoes.

## Minimum Parts

| Part | Purpose |
| --- | --- |
| ESP32 development board | Controller |
| DHT22, or DHT11 for rough testing | Temperature and humidity sensing |
| 5V small fan | Negative-pressure capture airflow |
| MOSFET module, or relay module | Safe fan switching |
| Jumper wires | Wiring |
| Breadboard | Bench testing |
| USB cable | Programming and ESP32 power |
| Capture box or fine mesh bag | Collection chamber |

Start with:

```text
ESP32 + DHT22 + 5V fan + MOSFET module
```

Add UV or purple-light attraction only after the sensor and fan loop is stable.

## Safety Boundaries

- Do not use exposed high-voltage circuits.
- Do not drive the fan directly from an ESP32 GPIO pin.
- Use a MOSFET or relay module between the ESP32 and fan.
- If the fan uses a separate 5V supply, share ground with the ESP32 control circuit.
- Keep live-insect testing separate from early bench tests.
- Treat capture results as unverified until there is a logged baseline.

## Wiring

### DHT22 To ESP32

| DHT22 | ESP32 |
| --- | --- |
| VCC | 3.3V |
| GND | GND |
| DATA | GPIO 4 |

Add a 10k pull-up resistor from DATA to 3.3V.

### Fan Control

Use a MOSFET module if available. It is quieter than a relay and better for
frequent switching.

```text
ESP32 GPIO 16
-> MOSFET module signal input
-> MOSFET switches 5V fan power
```

The fan should not be powered from a GPIO pin. Check the fan current before
choosing the driver module.

## v1 Rule

```text
if night mode is enabled
and humidity > 60%
and temperature is 24-32 C
then run fan for a bounded window
else keep fan off
```

For bench testing, use a short run window first. After the switching behavior is
stable, change it to 30 minutes.

## Arduino IDE Setup

1. Install Arduino IDE.
2. Install the ESP32 board package.
3. Install a DHT sensor library.
4. Connect the ESP32 by USB.
5. Select `ESP32 Dev Module`.
6. Select the correct serial port.
7. Upload the sketch.
8. Open Serial Monitor at `115200`.

## Arduino Sketch

```cpp
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22
#define FAN_PIN 16

const bool NIGHT_MODE = true;       // Replace with light sensor or RTC later.
const float HUMIDITY_THRESHOLD = 60;
const float TEMP_MIN_C = 24;
const float TEMP_MAX_C = 32;

const unsigned long SENSOR_INTERVAL_MS = 5000;
const unsigned long FAN_RUN_MS = 30UL * 60UL * 1000UL;

DHT dht(DHTPIN, DHTTYPE);

unsigned long lastSensorRead = 0;
unsigned long fanOffAt = 0;
bool fanRunning = false;

void setFan(bool on) {
  fanRunning = on;
  digitalWrite(FAN_PIN, on ? HIGH : LOW);
  Serial.println(on ? "Fan ON" : "Fan OFF");
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(FAN_PIN, OUTPUT);
  digitalWrite(FAN_PIN, LOW);
}

void loop() {
  unsigned long now = millis();

  if (fanRunning && now >= fanOffAt) {
    setFan(false);
  }

  if (now - lastSensorRead < SENSOR_INTERVAL_MS) {
    return;
  }
  lastSensorRead = now;

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("DHT read failed");
    return;
  }

  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.print(" C, Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  bool mosquitoCondition =
    NIGHT_MODE &&
    humidity > HUMIDITY_THRESHOLD &&
    temperature >= TEMP_MIN_C &&
    temperature <= TEMP_MAX_C;

  if (mosquitoCondition && !fanRunning) {
    fanOffAt = now + FAN_RUN_MS;
    setFan(true);
  }

  if (!mosquitoCondition && fanRunning) {
    setFan(false);
  }
}
```

## Mechanical Layout

```text
attraction area
    |
    v
funnel inlet
    |
    v
5V fan
    |
    v
fine mesh bag or capture box
```

Keep the airflow path simple. The first mechanical test is whether the fan can
pull small paper scraps or lightweight proxy targets into the capture chamber.

## v1 Success Criteria

1. ESP32 reads temperature and humidity reliably.
2. Fan turns on when the rule is satisfied.
3. Fan turns off when the rule is not satisfied or the run window ends.
4. Prototype can run 6-8 hours without crashing.
5. No exposed high voltage is present.

## Next Upgrades

- Add a light sensor or RTC so night mode is measured instead of hardcoded.
- Add runtime logging over serial, WiFi, or local storage.
- Add a microphone only after the v1 control loop is stable.
- Compare always-on fan mode against rule-based fan mode before claiming capture improvement.
