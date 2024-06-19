# Smart Safe House for kidsIOT

## 1. Code

[DOWNLOAD](../Code.zip)

Download and unzip these files. Here all codes are in folder **2.Code_kidsIOT**.

For convenience, <span style="color: rgb(2550, 10, 50);">we move the codes into: **D:\Code\2.Code_kidsIOT**.</span> You can also choose to move it into any disks at will. 

---

## 2. Development Environment Configuration

### 2.1 KidsBlock Download

![2101](media/2101.png)

1. [KidsBlock Download](https://wiki.kidsbits.cc/projects/KidsBlock/en/latest/download/)
2. Installation
	- [Windows System](https://wiki.kidsbits.cc/projects/KidsBlock/en/latest/Windows/)
	- [MacOS System](https://wiki.kidsbits.cc/projects/KidsBlock/en/latest/MacOS/)
3. [Driver Installation](https://wiki.kidsbits.cc/projects/KidsBlock/en/latest/driver/)

---

### 2.2 KidsBlock Tutorial

1. Make sure the board is connected to computer. Open KidsBlock and choose a device.

![2201](media/2201.png)

Choose **kidsIOT**.

![2202](media/2202.png)

Click **Connect**.

![2203](media/2203.png)

**Go to Editor**.

![2204](media/2204.png)

![line1](media/line1.png)

2. Build code blocks and upload.

**Method ①**: Directly drag blocks to the editing area.

![2207](media/2207.png)

After building your blocks, save it to your computer: **File --> Save to your computer**

![2209](media/2209.png)

Click ![2210](media/2210.png) to upload the code.

![line4](media/line4.png)

**Method ②**: Load code from your computer.

Download code in **1. Code** to your computer. For convenience, here we save it to D:\Code\2.Code_kidsIOT.

**File --> Load from your computer** and choose code to open.

![2208](media/2208.png)

After loading code, connect to the corresponding port.

![2211](media/2211.png)

![2212](media/2212.png)

After that, click ![2210](media/2210.png) to upload code.

![line1](media/line1.png)

**Main Interface**

![2205](media/2205.png)

![2206](media/2206.png)

---

## 3. Modules

<span style="color: rgb(2550, 10, 50);">Please move the codes to a convenient path as your needs, for instance, path: **D:\Code\2.Code_kidsIOT**.</span>

### KidsIOT Ports View

During experiments, <span style="color: rgb(2550, 10, 50);">modules can only be connected to ports in the same color.</span>

![KD2076](media/KD2076.png)

### 3.1 White LED Module

![1top](media/1top.png)

![KD2078](media/KD2078.png)

**LED (Light-Emitting Diode)**

LED is a commonly used light emitting device that converts electrical energy into light energy. Usually, it is used as an indicator in circuits and instruments, or as part of texts or numeric display.

It generally includes gallium(Ga), arsenic(As), phosphorus(P), nitrogen(N) and so on. 

|     LED components      | Emitting light colors |
| :---------------------: | :-------------------: |
| gallium arsenide diode  |          red          |
| gallium phosphide diode |         green         |
|  silicon carbide diode  |        yellow         |
|  gallium nitride diode  |         blue          |

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5 V

Operating current: 1.5 mA (Peak: 2.3mA)

Maximum power: 0.07 W

Control signal: digital signal

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

Modules with blue housing are digital ones, so we should connect to digital io pins of the mainboard (ports with blue).

![IOT-blue](media/IOT-blue.png)

In this experiment, we connect the white LED module to port 1. According to the board ports view, the digital io pin at port 1 is io13.

When we set the pin to high(1), the LED lights up in white; if we set to low(0), it will be off.![3bottom](media/3bottom.png)

#### Wiring Diagram

![3101](media/3101.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.1Light_on.sb3** file.

![3102](media/3102.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |          Code block           |
| :---------------------------: | :---------------------------: |
|  ![Events](media/Events.png)  |   ![begin](media/begin.png)   |
|       ![P](media/P.png)       | ![setmode](media/setmode.png) |
|       ![P](media/P.png)       |  ![setout](media/setout.png)  |
| ![Control](media/Control.png) | ![forever](media/forever.png) |
| ![Control](media/Control.png) |    ![wait](media/wait.png)    |

![line5](media/line5.png)

**Conceive:**

1. **Initialization**

   Set pins and modes.

   ![3103](media/3103.png)

   <br>

   **Build blocks:**

   ① Add ![begin](media/begin.png) and ![setmode](media/setmode.png).

   ![9top](media/9top.png)

   ![begin](media/begin.png) is a header file which is inevitable.

   ![setmode](media/setmode.png) sets a pin and its mode. pin mode can be one of the followings:

   input

   output
   
   input-pullup

   ![9bottom](media/9bottom.png)
   
   ② Set pin to IO13.

   ![3105](media/3105.png)

   ③ set mode to output.
   
   ![6top](media/6top.png)
   
   Q ：Why "output"?
   
   A ：<span style="color: rgb(10, 10, 200);">The code is written for the mainboard.</span> For the board, the pin IO13 is outputting power levels (high or low) to the connected module.
   
   ![6bottom](media/6bottom.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: LED turns on for 1s and off for 1s.

   ![3104](media/3104.png)

   <br>

   **Build blocks:**

   ① Add ![forever](media/forever.png).

   ![9top](media/9top.png)

   ![forever](media/forever.png): Code blocks in it will run in a loop.

   ![9bottom](media/9bottom.png)

   ② Put ![setout](media/setout.png) into "forever". 

   Set pin to IO13, and set to output high.

   ![9top](media/9top.png)

   ![setout](media/setout.png) sets a digital pin and its output power level:

   high

   low

   ![9bottom](media/9bottom.png)

   ③ Add a delay ![wait](media/wait.png) into "forever". 

   ![9top](media/9top.png)

   ![wait](media/wait.png) sets delay times in seconds.

   ![9bottom](media/9bottom.png)

   ![6top](media/6top.png)

   Q ：Why delay?

   A ：If you output a high level to LED, it will be always on. Yet, we add a delay of 1s, so it lights up for only 1s. Delay time is the ON/OFF time of LED.

   ![6bottom](media/6bottom.png)

   Set pin IO13 to output high for 1s:

   ![3106](media/3106.png)

   ④ Duplicate the blocks.

   ![3107](media/3107.png)

   As follows:

   ![3108](media/3108.png)

   Modify to low. Pin IO13 outputs low for 1s:

   ![3109](media/3109.png)

   The LED will circularly be on for 1s and off for 1s.

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, the LED module will flash with an interval of 1s (on for 1s and off for 1s).

![3102](media/3102.gif)

![4bottom](media/4bottom.png)

---

### 3.2 Tilt Sensor

![1top](media/1top.png)

![KD2090](media/KD2090.png)

Tilt sensor is also known as one-way ball switch because a ball is contained inside. Its one pin is connected and the other is not. The sensor outputs different level signals depending on whether the sensor is tilted. In applications, it is used for tilt detection and alarm.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Voltage: DC 3.3 ~ 5V 

Current: 4.2 mA

Maximum power: 0.03 W

Operating temperature: -10°C ~ +50°C

Dimensions: 32 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

Modules with blue housing are digital ones, so we should connect to digital io pins of the mainboard (ports with blue).

![IOT-blue](media/IOT-blue.png)

In this experiment, we connect the module to port 2. According to the board ports view, the digital io pin at port 2 is io2.

![3201](media/3201.png)

Tilt the sensor and the ball will roll to the pins so that two pins are connected, and the module outputs a low level. If the ball move to the other end, the pins will be disconnected so the module outputs high.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3215](media/3215.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.2Tilt.sb3** file.

![3202](media/3202.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|              Blocks               |              Code block               |
| :-------------------------------: | :-----------------------------------: |
|    ![Events](media/Events.png)    |       ![begin](media/begin.png)       |
|         ![P](media/P.png)         |     ![setmode](media/setmode.png)     |
|         ![P](media/P.png)         | ![readdigital](media/readdigital.png) |
|    ![Serial](media/Serial.png)    | ![serialbegin](media/serialbegin.png) |
|    ![Serial](media/Serial.png)    | ![serialprint](media/serialprint.png) |
| ![Operators](media/Operators.png) |           ![=](media/=.png)           |
|   ![Control](media/Control.png)   |     ![forever](media/forever.png)     |
|   ![Control](media/Control.png)   |      ![ifelse](media/ifelse.png)      |
|   ![Control](media/Control.png)   |        ![wait](media/wait.png)        |

![line5](media/line5.png)

**Conceive:**

1. **Initialization**

   Set pins and modes. Initialize the serial port.

   ![3203](media/3203.png)

   <br>

   **Build blocks:**

      ① Add code blocks to the editing area and build as follows:

   ![3204](media/3204.png)

   ![9top](media/9top.png)

      ![serialbegin](media/serialbegin.png) initializes the serial port and sets baud rate (default is 9600). This block is essential when serial port is adopted; or else printing may fail.

   ![9bottom](media/9bottom.png)

   Set sensor pin to io2 and mode to input. Initialize serial port to facilitate the message printing on the monitor.

   ![6top](media/6top.png)

   Q ：Why "input"?

   A ：<span style="color: rgb(10, 10, 200);">The code is written for the mainboard.</span> For the board, pin io2 is inputting power levels (high or low) from the connected module to the board. According to the power level, the board determines whether the module is tilt.

   ![6bottom](media/6bottom.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: Print the power level read by io2, and determine whether it is low(0).

   If yes, the sensor is tilt and the monitor prints *The switch is turned on* ; If not, the sensor is not tilt and *The switch is turned off* will be shown.

   ![3205](media/3205.png)

   <br>

   **Build blocks:**

   ① Add code blocks to the editing area and build as follows:

   ![3206](media/3206.png)

   ![9top](media/9top.png)

   ![readdigital](media/readdigital.png) reads power level of a digital pin. It returns 1(high) or 0(low).

   ![serialprint](media/serialprint.png) prints the messages on the serial monitor. This message can also be a code block, and the output will be its value. There are three print mode: wrap, no wrap, HEX(hexadecimal).

   ![9bottom](media/9bottom.png)

   Set pin to IO2 and print mode to no-wrap.

   ![3207](media/3207.png)

   ![6top](media/6top.png)

   ​     Q : Why "no-wrap"?

      If we set to wrap, the message will have a line break after the power level value being output.

      Wrap: 

      ![3208](media/3208.png)

     No-wrap:

      ![3209](media/3209.png)

    A ：No-wrap is more convenient for us to check the results.

   ![6bottom](media/6bottom.png)

   ② Add code blocks to the editing area and build as follows:

   ![3210](media/3210.png)

   ![9top](media/9top.png)

   ![=](media/=.png) checks whether the two values equal each other. If yes, output True.

   ![ifelse](media/ifelse.png) determines the condition is true or false. 

   True: execute codes in "if":

   ![3211](media/3211.png)

   False: execute codes in "else":

   ![3212](media/3212.png)

   ![9bottom](media/9bottom.png)

   ![3213](media/3213.png) determines whether the value read by pin io2 equals 0. Put it in "if else" block to set it to the condition.

   value of pin io2 = 0: the condition is true, execute codes in "if", and print two Space + *The switch is turned on* on the serial monitor.

   value of pin io2 ≠ 0: the condition is false, execute codes in "else", and print two Space + *The switch is turned off* on the serial monitor.

   ![6top](media/6top.png)

      Q ：Why Space?

     The value will be too close to the contents, which is not convenient for us to check the outputs.

      Without space:

      ![3214](media/3214.png)

      With space:

      ![3209](media/3209.png)

      A ：We add a space to separate the value and contents.

   ![6bottom](media/6bottom.png)

   ③ Add a delay ![wait](media/wait.png) and set the time to 0.1s.

   ![6top](media/6top.png)

   Q ：Why delay?

   If we do not add a delay, the printing command will always run, so then the serial monitor refreshes the results very fast. A delay of 0.1s will limit the printing speed. Serial monitor refreshes outputs every 0.1s.

   A ：Limit the printing speed.

   ![6bottom](media/6bottom.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

<span style="color: rgb(2550, 10, 50);">Set baud rate before uploading code to avoid garbled words.</span>

Click ![Baud1](media/Baud1.png) and set Buadrate to 9600.

![Baud2](media/Baud2.png)

After uploading code, tilt the sensor to the pins to connect them, and the red LED will light up, and the monitor prints *The switch is turned on*.

If you tilt it to the other end, the pins will disconnected, so the red LED will go off and *The switch is turned off*  shows on the monitor.

![3206](media/3206.gif)

![4bottom](media/4bottom.png)

---

### 3.3 PIR Motion Sensor

![1top](media/1top.png)

![KD2110](media/KD2110.png)

The human body temperature is generally constant at about 37°, and will emit infrared signals with a wavelength of about 10μm. Passive infrared probes just work by detecting the specific infrared waves emitted by human body.

These 10μm infrared waves are enhanced by the Fresnel filter and concentrated on the infrared sensing source to control the interference of the environment. The infrared sensing sources are usually pyroelectric elements, which can generate an alarm signal when the infrared radiation temperature of the human body changes. Otherwise, no signal will be output.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Operating current: 3.6 mA

Maximum power: 0.018 W

View angle: Y = 90°, X = 110° (theoretical value)

Detection distance: ≤5m

Operating temperature: -10°C ~ +50°C

Control signal: digital signal

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

Modules with blue housing are digital ones, so we should connect to digital io pins of the mainboard (ports with blue).

![IOT-blue](media/IOT-blue.png)

In this experiment, we connect the module to port 3. According to the board ports view, the digital io pin at port 3 is io26.

When the sensor detects a **human motion** nearby, it outputs high. If no, it outputs low.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3301](media/3301.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.3PIR.sb3** file.

![3302](media/3302.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|              Blocks               |              Code block               |
| :-------------------------------: | :-----------------------------------: |
|    ![Events](media/Events.png)    |       ![begin](media/begin.png)       |
|         ![P](media/P.png)         |     ![setmode](media/setmode.png)     |
|         ![P](media/P.png)         | ![readdigital](media/readdigital.png) |
|    ![Serial](media/Serial.png)    | ![serialbegin](media/serialbegin.png) |
|    ![Serial](media/Serial.png)    | ![serialprint](media/serialprint.png) |
| ![Operators](media/Operators.png) |           ![=](media/=.png)           |
|   ![Control](media/Control.png)   |     ![forever](media/forever.png)     |
|   ![Control](media/Control.png)   |      ![ifelse](media/ifelse.png)      |
|   ![Control](media/Control.png)   |        ![wait](media/wait.png)        |

![line5](media/line5.png)

**Conceive:**

1. **Initialization**

   Set pins and modes. Initialize the serial port.

   ![3303](media/3303.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: Print the power level read by io26 and determine whether it is high(1). If yes, the monitor will show  *Some body is in this area!* ; If not, print *No one!* 

   ![3304](media/3304.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

<span style="color: rgb(2550, 10, 50);">Set baud rate before uploading code to avoid garbled words.</span>

Click ![Baud1](media/Baud1.png) and set Buadrate to 9600.

![Baud2](media/Baud2.png)

After uploading code, when the PIR motion sensor detects a human motion, it outputs high and the red LED goes off. Monitor prints *Some body is in this area!* ;

![3305](media/3305.png)

If the sensor detects nothing, it outputs low and red LED lights up. Monitor displays *No one!* .

![3306](media/3306.png)

Put you palm above the sensor, and wave it. The sensor will detect the motion and then output high. When you stay still or move your hand away, the sensor detects nothing so then outputs low.

![3307](media/3307.gif)

![4bottom](media/4bottom.png)

---

### 3.4 8002b Power Amplifier

![1top](media/1top.png)

![KD2106](media/KD2106.png)

The 8002b power amplifier is mainly composed of an adjustable potentiometer, a speaker and an audio amplifier chip. This module can amplify the output of small audio signals and play them through its low-power speaker. It can also be used as an external amplifier to play music.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Operating current: ≤350 mA

Maximum power: 1.5 W

Operating temperature: -10°C ~ +50°C

Input signal: digital signal

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

Music is an invisible art. It is a language that narrates emotions and thoughts. 

The foundation of music, as we all know, is note. We can compose a variety of melodies and rhythms with different notes. Of all the notes, the most basic are seven:

![3401](media/3401.png)

We can compose a variety of melodies and rhythms with these notes.

This module must be drive by square waves to emit sound. We can change the duty cycle of PWM to control square waves.

- The greater the duty cycle is, the lauder the sound will be.

And the tones vary from different frequency of PWM.

- The higher the frequency is, the higher the tone will be.

![peg](media/peg.png)

![line3](media/line3.png)

**What is PWM?**

PWM (Pulse width modulation) simulates the change of analog signal through digital signal.

Pulse width is the high level in a complete square wave cycle. So, pulse width modulation is to adjust the high level(of course, in other words, low level is also adjusted).

![3402](media/3402.png)

- **PWM frequency**: the number of times the signal going from high level to low level and back to high level in 1 second (one cycle), that is, how many cycles there are in a second.

  **Unit**: Hz

  **Expression**: 50Hz 100Hz

- **PWM cycle**

  $ T= \frac {1}{f}$      $ Cycle= \frac {1}{frequency}$

  If the frequency is 50Hz, the cycle will be 20ms, i.e., there are 50 PWM cycles in one second.

- **PWM duty cycle**: the ratio of high level time to the whole cycle time.

  - Unit: %(1% ~ 100%)
  - Cycle: The time of a pulse signal. The number of cycles in 1s equals the frequency.
  - Pulse width time: high level time.

  ![3403](media/3403.gif)
  
  <center>The relationship between duty cycle and LED brightness<center>

  The longer the high level time is, the greater the duty cycle will be, and the brighter the LED will be.

  **The PWM frequency corresponding to notes**:
  
  ![3404](media/3404.png)

![line3](media/line3.png)

The module boasts a potentiometer that adjusts the volume of sounds. Rotate clockwise to turn the volume up. 

![3418](media/3418.png)

Modules with blue housing are digital ones, so we should connect to digital io pins of the mainboard (ports with blue).

![IOT-blue](media/IOT-blue.png)

In this experiment, we connect the module to port 4. According to the board ports view, the digital io pin at port 4 is io27.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3405](media/3405.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.4Power amplifier.sb3** file.

![3406](media/3406.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |          Code block           |
| :---------------------------: | :---------------------------: |
|  ![Events](media/Events.png)  |   ![begin](media/begin.png)   |
| ![Speaker](media/Speaker.png) |  ![S_tone](media/S_tone.png)  |
| ![Control](media/Control.png) | ![forever](media/forever.png) |
| ![Control](media/Control.png) |    ![wait](media/wait.png)    |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) and find **Passive buzzer** to load it.

![3407](media/3407.png)

Back.

![3408](media/3408.png)

Successfully add:

![3409](media/3409.png)

1. **Main Code**

   Loop: Play tone C, D, E, F, G, A, B at the beat of 1/2.

   ![3410](media/3410.png)

   <br>

   **Build blocks:**

   ① Drag code blocks as follows:

   ![3411](media/3411.png)

   ![9top](media/9top.png)

   ![S_tone](media/S_tone.png) sets tones and beats of the pin of the amplifier. 

   ![6top](media/6top.png)

      Q ：What is beat? 

      A ：A beat is the basic unit of time in music. You may consider it as the time of a tone being played.

   ![6bottom](media/6bottom.png)

   ![9bottom](media/9bottom.png)

   Set as follows:

   ![3412](media/3412.png)

   ② Duplicate the blocks.

   ![3413](media/3413.png)

   As follows:

   ![3414](media/3414.png)

   Duplicate 6 times in total:

   ![3415](media/3415.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, the amplifier repeatedly plays tone C, D, E, F, G, A, B.

![4bottom](media/4bottom.png)

#### Extension

![7top](media/7top.png)

Congratulations! You have played these basic notes successfully! Now let's try to compose a beautiful music and play with this power amplifier!

![3416](media/3416.png)

<center>Twinkle Twinkle Little Star<center>
*Twinkle Twinkle Little Star* is an outstanding musical work in British children's songs, which has been widely circulated around the world for more than two centuries, and has become the most classic children's song in the enlightenment education of all countries and cultures.

In the score,  “-” indicates the duration of the previous note. When building code blocks, we may set longer beats to last the playing of one tone.

According to the score and the music theory, try to write code blocks to play *Twinkle Twinkle Little Star*!

Or you can directly open file **3.4Twinkle Twinkle Little Star.sb3** and upload it to enjoy the song!

![3417](media/3417.gif)

![7bottom](media/7bottom.png)

---

### 3.5 6812 RGB Module

![1top](media/1top.png)

![KD2083](media/KD2083.png)

RGB LED is imaged in the intersection of three primary colors (RGB): red, green and blue. Both white LED and RGB LED are able to emit white light. The former is presented directly in white, while the latter is mixed with red, green and blue.

**Trichromatic Theory**

![3501](media/3501.png)

Human eyes are sensitive to RGB colors. Most colors can be synthesized by RGB in different proportions. Therefore, the vast majority of monochromatic light can also be decomposed into RGB colors. This is the most basic principle of colorimetry --- trichromatic theory.

Red, green and blue lights are called additive primary colors because by the combination of these three primaries in different proportion, various colored lights will produce. Similarly, there are also subtractive ones. So we may add or/and subtract colors as needed. 

The three primary colors of the paint can not compose white, yet, with optical elements, those of light can do it, which is mixed by **three equal parts of R, G, B**.

6812 RGB module is an intelligent external controlled LED light source that integrates control circuit and light emitting circuit. Each LED is a pixel with a total of four pixels, and they can be controlled by only one pin.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Voltage: DC 3.3 ~ 5V 

Current: 140 mA

Maximum power: 0.7 W

Operating temperature: -10°C ~ +50°C

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

The 6812 RGB module contains four pixels in series. In fact, no matter how many pixels, we can control any one of the lights to show any color through only one pin.

Modules with blue housing are digital ones, so we should connect to digital io pins of the mainboard (ports with blue).

![IOT-blue](media/IOT-blue.png)

In this experiment, we connect the module to port 9. According to the board ports view, the digital io pin at port 9 is digital port 18.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3502](media/3502.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.5pixel.sb3** file.

![3503](media/3503.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |                   Code block                    |
| :---------------------------: | :---------------------------------------------: |
|  ![Events](media/Events.png)  |            ![begin](media/begin.png)            |
|   ![Strip](media/Strip.png)   |     ![Strip-length](media/Strip-length.png)     |
|   ![Strip](media/Strip.png)   | ![Strip-brightness](media/Strip-brightness.png) |
|   ![Strip](media/Strip.png)   |    ![Strip-refresh](media/Strip-refresh.png)    |
|   ![Strip](media/Strip.png)   |      ![Strip-color](media/Strip-color.png)      |
|   ![Strip](media/Strip.png)   |        ![Strip-RGB](media/Strip-RGB.png)        |
| ![Control](media/Control.png) |          ![forever](media/forever.png)          |
| ![Control](media/Control.png) |             ![wait](media/wait.png)             |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) to load **RGB LED Strip**.

![3504](media/3504.png)

1. **Initialization**

   Set pins and modes, and pixel numbers and LED brightness.

   ![3505](media/3505.png)
   
   ![9top](media/9top.png)
   
   ![Strip-length](media/Strip-length.png) sets connected pin and pixel number.
   
   ![Strip-brightness](media/Strip-brightness.png) sets the brightness of LED, range: 0 ~ 255.
   
   ![9bottom](media/9bottom.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: Respectively light up in red, green, blue, white with each for 1s, and then turn off.

   ![3506](media/3506.png)

   <br>

   **Build blocks:**

   ① Drag code blocks as follows:

   ![3507](media/3507.png)

   The pixels will light up in red from 0 to the end, each for 1s and 4 pixels in total.

   ![9top](media/9top.png)

   ![Strip-refresh](media/Strip-refresh.png) refreshes the colors of pixels. This block is inevitable before changing colors. Otherwise the set color may be not displayed.

   

   ![Strip-color](media/Strip-color.png) sets colors for the pixels.

   ![3508](media/3508.png) : the first number is the beginning pixel.

   ![3509](media/3509.png) : the second number is the number of the pixels.

   ![3510](media/3510.png) : the third box is the color of the pixel. You can choose colors and set its saturation and brightness.

   

   ![Strip-RGB](media/Strip-RGB.png) sets the three parameters of RGB. Each value ranges from 0 ~ 255. For example: Red is R=255 and G, B=0; white is R, G, B=0.

   This code block can be combined with the one that sets the colors, which makes it easy to quickly set the color in a stable proportion.
   
   Drag it into the third box of the block:
   
   ![3511](media/3511.png)
   
   As follows:
   
   ![3512](media/3512.png)
   
   Then you can set colors by adjusting the proportion of RGB.
   
   ![9bottom](media/9bottom.png)
   
   ② Duplicate the blocks.
   
   ![3513](media/3513.png)
   
   As follows:
   
   ![3514](media/3514.png)
   
   Duplicate three times and modify the proportion as follows:
   
   ![3515](media/3515.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, the four pixels repeatedly light up in red, green, white and go off.

![3516](media/3516.gif)

![4bottom](media/4bottom.png)

---

###  3.6 Thin Film Pressure Sensor

![1top](media/1top.png)

![KD2100](media/KD2100.png)



This thin film sensor is an analog input module. The previous modules we learned are all digital ones, so what is the difference between these two types? 

The digital modules can only input/output high or low (3.3V or 0V), while the analog ones can output any voltage value read by ADC analog ports within the range.

![3601](media/3601.png)

The thin film sensor can be regarded as a resistance variable with pressure. When the thin film(circled in red) is pressed, the sensor converts the pressure into resistance and outputs it through the pin(squared in blue).



**Using Method:**

1. Place the pressure sensitive area of the sensor on a firm, flat surface when in use. Using or bending the sensor on a curved or shaped surface will lead to a "responsive" state even without pressure; In this state, the sensor will detect a false pressure value, so the output value is not accurate. 

	If you cannot find an appropriate surface, disassemble the sensor housing.

	First, find the **buckle** of the housing:

![3602](media/3602.png)

Place one of your thumb above the **buckle** and pinch the module with another hand. Pull the buckle in the direction shown below:

![3603](media/3603.png)

At the same time, take the module out of the housing in the following direction:

![3604](media/3604.png)

As follows:

![3605](media/3605.gif)

Place the housing upside down and place the thin film on it.

![3606](media/3606.png)

2. After the sensor is stressed and maintained pressure, the output value will drift slightly over time, usually within 5%. Under normal conditions, it is best to lay the film flat without pressure on it.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Current: 0.5 mA

Maximum power: 0.0025 W

Range: 0 ~ 5kg

Trigger conduction pressure: 500g

Operating temperature: -10°C ~ +50°C

Dimensions: 48 x 24 x 18 mm

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

The thin film on the sensor detects the pressure value. It converts the detected pressure value into voltage. As the pressure increases, the resistance and the output voltage gradually decreases (3.3V ~ 0). This voltage value is a continuous analog value ranging from 3.3V ~ 0.

<span style="color: rgb(10, 10, 200);">The main board is not able to process analog signals directly, so we need to convert them into digital ones. Therefore, ADC(Analog to Digital Converter) is required.</span>

![peg](media/peg.png)

![line3](media/line3.png)

**What is ADC?**

ADC(Analog to Digital Converter) converts analog values to digital ones. The ADC acquisition is integrated in our board, so you can call it directly. 

**kidsIOT ADC Parameters**

1. Reference voltage: 3.3V

2. Resolution: 12bit

   A n-bit ADC means this ADC contains 2ⁿ scales. 

   12-bit ADC contains $2^{12}=4096$ scales, and it outputs totally 4096 digital values (including from 0～ 4095), each scale is $\frac{3.3}{4095}≈0.00081(V)$.

3. General ADC input voltage calculation:

   <font face="courier New" color="black" size=6>$ Vin= \frac {AVDD_{ADC}}{2^{Resolution Bit}-1}*ReadData$</font> 

   $AVDD_{ADC}$: Reference voltage

4. ADC channel: 5 channels

   ADC0 - ADC3 are GPIO26 - 29, among which ADC0, ADC1, ADC2 are available to commonly measure the analog voltage, while ADC3 detects on-board VSYS voltage.

   Since ADC4 is built-in, it cannot be used at the pin. It measures on-board temperature sensor.

![line3](media/line3.png)

Modules with red housing are analog ones, so we should connect to analog ports of the mainboard (ports with red).

![IOT-red](media/IOT-red.png)

In this experiment, we connect the module to port 6. According to the board ports view, the analog io pin at port 6 is io36.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3607](media/3607.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.6Pressure.sb3** file.

![3608](media/3608.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|              Blocks               |               Code block                |
| :-------------------------------: | :-------------------------------------: |
|    ![Events](media/Events.png)    |        ![begin](media/begin.png)        |
|         ![P](media/P.png)         |      ![setmode](media/setmode.png)      |
|         ![P](media/P.png)         |   ![readanalog](media/readanalog.png)   |
|    ![Serial](media/Serial.png)    |  ![serialbegin](media/serialbegin.png)  |
|    ![Serial](media/Serial.png)    |  ![serialprint](media/serialprint.png)  |
|      ![Vari](media/Vari.png)      | ![variablename](media/variablename.png) |
|      ![Vari](media/Vari.png)      |  ![setvariable](media/setvariable.png)  |
|      ![Vari](media/Vari.png)      |     ![variable](media/variable.png)     |
| ![Operators](media/Operators.png) |       ![divide](media/divide.png)       |
| ![Operators](media/Operators.png) |     ![multiply](media/multiply.png)     |
|   ![Control](media/Control.png)   |      ![forever](media/forever.png)      |
|   ![Control](media/Control.png)   |         ![wait](media/wait.png)         |

![line5](media/line5.png)

**Conceive:**

1. **Initialization**

   Set pins and modes. Initialize the serial port. Define a variable to store the analog value detected by the thin film sensor.

   ![3609](media/3609.png)
   
   ![9top](media/9top.png)
   
   ![variablename](media/variablename.png) creates a new variable.
   
   - ![3610](media/3610.png)
   
     define global or local variable.
   
   - ![3611](media/3611.png)
   
     Choose a variable type.
   
   - ![3612](media/3612.png)
   
     Name the variable.
   
   - ![3613](media/3613.png)
   
     Assign an initial value to the variable.
   
   ![9bottom](media/9bottom.png)
   
   ![3614](media/3614.png)
   
   Create a float variable named *Pressure_value* to store the analog value read by the sensor with an initial value of 0.

![line3](media/line3.png)

2. **Main Code**

   Loop: print the analog value detected by the sensor and the converted voltage value, and refresh the results every 0.1s.

   ![3615](media/3615.png)

   <br>

   **Build blocks:**

   ① Add code blocks to the editing area and build as follows:

   ![3616](media/3616.png)
   
   ![9top](media/9top.png)
   
   ![setvariable](media/setvariable.png) assigns a value to a specific variable.
   
   ![readanalog](media/readanalog.png) reads analog values of a pin.
   
   ![9bottom](media/9bottom.png)
   
   Connect the sensor to pin IO36. Read the analog value of IO36 and assign it to variable *Pressure_value*, which is used to calculate the actual voltage value. 
   
   ② Add code blocks to the editing area and build as follows:
   
   ![3617](media/3617.png)
   
   ![9top](media/9top.png)
   
   ![variable](media/variable.png) is a variable block.
   
   ![multiply](media/multiply.png) returns the result of multiplying the values of the left and right values.
   
   ![divide](media/divide.png) returns the value of the left value divided by the right one.
   
   ![9bottom](media/9bottom.png)
   
   Code blocks for the calculation of actual voltage: 
   
   ![3618](media/3618.png)
   
   Print analog value and actual voltage value(V) on the serial monitor.
   
   ③ Add a delay ![wait](media/wait.png) in "forever" and set to 0.1s. It is used to maintain the printing time. 

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

<span style="color: rgb(2550, 10, 50);">Set baud rate before uploading code to avoid garbled words.</span>

Click ![Baud1](media/Baud1.png) and set Buadrate to 9600.

![Baud2](media/Baud2.png)

After uploading code, the sensor detects pressure.

![3619](media/3619.png)

Press the thin film by your finger. As the pressure increases, the output voltage gradually decreases.

![3620](media/3620.png)

![3621](media/3621.png)

![4bottom](media/4bottom.png)

---

### 3.7 HT16K33_8X8 Dot Matrix

![1top](media/1top.png)

![KD2085](media/KD2085.png)

Dot matrix is composed of multiple LEDs, whose collection is called the "matrix", where a single unit is called the "dot". The 8X8 dot matrix consists of a total of 64 LEDs, and each one is placed at the intersection of rows and columns.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Current: 190 mA

Maximum power: 0.95 W

Operating temperature: -10°C ~ +50°C

Dimensions: 48 x 24 x 18 mm

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

We control the white LED module by an IO port, so an 8x8 dot matrix requires a total of 16 ports, which is a very waste of ports. To this end, we specially designed this module, LEDs on which can be controlled by one I2C communication interface.

Here is the coordinate diagram of 8x8 dot matrix, and a certain LED is represented by (X,Y).

![3703](media/3703.png)

Modules with green housing are I2C ones, so we should connect to ports with green.

![IOT-green](media/IOT-green.png)

In this experiment, we connect to port 5.

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3701](media/3701.png)

#### Test Code

Choose D:\Code\1.Code_kidsuno to open **3.7Dot matrix.sb3** file.

![3702](media/3702.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |                 Code block                  |
| :---------------------------: | :-----------------------------------------: |
|  ![Events](media/Events.png)  |          ![begin](media/begin.png)          |
|  ![Matrix](media/Matrix.png)  |    ![Matrix-Init](media/Matrix-Init.png)    |
|  ![Matrix](media/Matrix.png)  |   ![Matrix-clear](media/Matrix-clear.png)   |
|  ![Matrix](media/Matrix.png)  |      ![Matrix-XY](media/Matrix-XY.png)      |
|  ![Matrix](media/Matrix.png)  | ![Matrix-refresh](media/Matrix-refresh.png) |
|  ![Matrix](media/Matrix.png)  |    ![Matrix-line](media/Matrix-line.png)    |
|  ![Matrix](media/Matrix.png)  |   ![Matrix-image](media/Matrix-image.png)   |
| ![Control](media/Control.png) |        ![forever](media/forever.png)        |
| ![Control](media/Control.png) |           ![wait](media/wait.png)           |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) to load **Matrix 8*8 IIC**.

![3704](media/3704.png)

1. **Initialization**

   Initialize the dot matrix.

   ![3705](media/3705.png)


![line3](media/line3.png)

2. **Main Code**

   Loop: Light up dot (6,6) for 1s; Draw a line from dot (6,2) to (6,6) to light up for 1s; Light up a smile icon for 1s.

   ![3706](media/3706.png)

   <br>

   **Build blocks:**

   ① Drag code blocks as follows:

   ![3707](media/3707.png)

   Light up dot (6,6) for 1s.

   ![9top](media/9top.png)

   ![Matrix-clear](media/Matrix-clear.png) clears the dot matrix, so all LED on it will go off. Each time before the dot matrix is operated, it should be cleared to avoid the LED that has been lit affecting the currently operated ones.

   ![Matrix-XY](media/Matrix-XY.png)  lights up a single LED. You only need to set the coordinate (x,y). For its state, HIGH is "light on", and LOW is "light out".

   ![Matrix-refresh](media/Matrix-refresh.png) refreshes the dot matrix. After operating on this module, remember to refresh it.

   ![9bottom](media/9bottom.png)

   ② Drag code blocks as follows:

   ![3708](media/3708.png)

   Draw a line from dot (6,2) to (6,6) to light up for 1s.![9top](media/9top.png)

   ![Matrix-line](media/Matrix-line.png) draws a line by inputting the coordinates of the starting and ending point. 

   ![9bottom](media/9bottom.png)

   ③ Drag code blocks as follows:

   ![3709](media/3709.png)

   Light up a smile icon for 1s.

   ![9top](media/9top.png)

   ![Matrix-image](media/Matrix-image.png) draws icons on the dot matrix.

   ![3710](media/3710.png)

   Hold down the mouse, slide on the dot matrix to light the corresponding LED. Same operations can also turn off the LED that has been lit.

   Note that the pattern drawn here will reverse 180° when displayed on the module.

   ![9bottom](media/9bottom.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, the dot matrix will show the set icons.

![3711](media/3711.gif)

![4bottom](media/4bottom.png)

---

### 3.8 RFID Module

![1top](media/1top.png)

![KD2113](media/KD2113.png)

RFID(Radio Frequency Identification) is a kind of communication that identifies specific targets through radio signals to read and write relevant data, without establishing mechanical or optical contact between the identification system and the specific target.

In application, RFID is widely used in clothing tags, library book searching systems, access control systems and food safety traceability systems.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Operating current: 60 mA

Operating power: 0.3 W

Sensing range: 0 ~ 15 mm

Operating temperature: -10°C ~ +50°C

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

RFID adopts radio frequency to carry out non-contact two-way data transmission between the reader and the radio frequency card for target identification and data exchange. 

The working principle of RFID module:

![3801](media/3801.png)

Sending signals: An RFID module (reader) sends a radio signal, usually an RF signal within a specific frequency range.

Reception response: When the IC card (RF card) enters the sensing range of the RFID module, the card receives signals from the reader and is activated by the energy obtained from them. After activation, the card's chip converts the stored information into a response signal that is sent back to the reader via the antenna.

Data processing: After the RFID module receives the signal sent by the IC card, it analyzes and processes these signals through the RF communication protocol. The board then receives these data and store, analyze, process, or pass it on to other systems.

Modules with green housing are I2C ones, so we should connect to ports with green. In this experiment, we connect to port 7.

![IOT-green](media/IOT-green.png)

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3802](media/3802.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.8RFID.sb3** file.

![3803](media/3803.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |              Code block               |
| :---------------------------: | :-----------------------------------: |
|  ![Events](media/Events.png)  |       ![begin](media/begin.png)       |
|    ![RFID](media/RFID.png)    |   ![RFID-init](media/RFID-init.png)   |
|    ![RFID](media/RFID.png)    |   ![RFID-read](media/RFID-read.png)   |
|  ![Serial](media/Serial.png)  | ![serialbegin](media/serialbegin.png) |
|  ![Serial](media/Serial.png)  | ![serialprint](media/serialprint.png) |
| ![Control](media/Control.png) |     ![forever](media/forever.png)     |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) to load **RFID RC522 IIC**.

![3808](media/3808.png)

1. **Initialization**

   Initialize RFID module and the serial port. 

   ![3804](media/3804.png)

   ![9top](media/9top.png)

   ![RFID-init](media/RFID-init.png) initializes the RFID module, which is required when operating on RFID.

   ![9bottom](media/9bottom.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: 

   ① Keep sending signals to search new IC card(s).

   ② Receive IC card response and return the data.

   ③ Print the read details of the IC card.

   ![3805](media/3805.png)

   ![9top](media/9top.png)

   ![RFID-read](media/RFID-read.png) reads the IC card data. When an IC card response is received, this code block reads the  IC card data.

   ![9bottom](media/9bottom.png)


![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

<span style="color: rgb(2550, 10, 50);">Set baud rate before uploading code to avoid garbled words.</span>

Click ![Baud1](media/Baud1.png) and set Buadrate to 9600.

![Baud2](media/Baud2.png)

Before uploading code, please wire up accordingly to ensure that the serial monitor works normally. 

After uploading code, place the white IC card at the sensing range of the RFID module.

![3806](media/3806.png)

The serial monitor will print the read information of the IC card.

![3807](media/3807.png)

**NOTE: IC card data vary from cards. Please record your IC card information, which will be used in later experiment.**

![4bottom](media/4bottom.png)

---

### 3.9 AK8975 Three-axis Magnetic Sensor

![1top](media/1top.png)

![KD2119](media/KD2119.png)

The three-axis magnetic sensor is used to measure and detect the magnetic field force. It detects geomagnetic field on three axes.

**Geomagnetic Field**

Geomagnetic field refers to the natural magnetic field that exists inside the Earth. The Earth can be regarded as a magnetic dipole, with one pole near the geographical North Pole and the other near the geographical South Pole. The force of this magnetic field is about 0.5 to 0.6 Gauss.

![3901](media/3901.png)

**Geomagnetic Sensor**

The geomagnetic field is a vector that, for a fixed location, can be divided into two components parallel to the local horizontal plane and one component perpendicular to the local horizontal plane. If the electronic compass is kept parallel to the horizontal plane, the three axes of the compass correspond to these three components.

For the two parallel components, their vector sum always points to magnetic north. **Course Angle (Azimuth)** in the compass is the Angle between the current direction and magnetic north. Since the compass remains horizontal, it is possible to calculate <span style="color: rgb(10, 10, 200);">**Course Angle**</span> through the values of the two axes(usually X and Y). When the compass rotates horizontally, **the Course Angle varies between 0° and 360° **.

To sum up, three-axis magnetic sensor is widely applied to navigation and positioning systems, attitude control and motion detection, environmental monitoring and safety applications, as well as medical devices. With continuous progress and innovation, its applications will expand, bringing more convenience and possibilities to all walks of life.

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V 

Operating current: 20 mA (at self-check mode)

Maximum power: 0.1 W

Operating voltage: -10°C ~ +50°C

Dimensions: 48 x 24 x 18 mm (without housing)

Positioning holes: diameter of 4.8 mm

Interface: telephone socket

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

The three-axis magnetic sensor adopts IIC communication protocol. When using, we should connect to ports with green. In this experiment, we connect to port 8.

![IOT-green](media/IOT-green.png)

![3bottom](media/3bottom.png)

#### Wiring Diagram

![3903](media/3903.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.9Three-axis magnetic sensor.sb3** file.

![3904](media/3904.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|            Blocks             |              Code block               |
| :---------------------------: | :-----------------------------------: |
|  ![Events](media/Events.png)  |       ![begin](media/begin.png)       |
|      ![AK](media/AK.png)      |     ![AK-init](media/AK-init.png)     |
|      ![AK](media/AK.png)      |  ![AK-compass](media/AK-compass.png)  |
|      ![AK](media/AK.png)      |    ![AK-angle](media/AK-angle.png)    |
|  ![Serial](media/Serial.png)  | ![serialbegin](media/serialbegin.png) |
|  ![Serial](media/Serial.png)  | ![serialprint](media/serialprint.png) |
| ![Control](media/Control.png) |     ![forever](media/forever.png)     |
| ![Control](media/Control.png) |        ![wait](media/wait.png)        |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) to load **ak8975**.

![3909](media/3909.png)

1. **Initialization**

   Initialize AK8975 three-axis magnetic sensor and the serial port.

   ![3905](media/3905.png)

   ![9top](media/9top.png)

   ![AK-init](media/AK-init.png) initialize the AK8975 three-axis magnetic sensor.

   ![9bottom](media/9bottom.png)

![line3](media/line3.png)

2. **Main Code**

   Loop: 

   Print geomagnetic data for three axes, and wrap to print the value of Course Angle. Refresh the results per second.

   ![3906](media/3906.png)

   ![9top](media/9top.png)

   ![AK-compass](media/AK-compass.png) reads the values on axis X, Y, Z; click the triangle to choose an axis.

   ![AK-angle](media/AK-angle.png) reads the value of Course Angle.
   
   ![9bottom](media/9bottom.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

<span style="color: rgb(2550, 10, 50);">Set baud rate before uploading code to avoid garbled words.</span>

Click ![Baud1](media/Baud1-17181918742301.png)and set Buadrate to 9600.

![Baud2](media/Baud2-17181918742322.png)

Before uploading code, please wire up accordingly to ensure that the serial monitor works normally. 

After uploading code, the serial monitor prints the values of axis X, Y, Z and the value of Course Angle.

![3907](media/3907.png)

Rotate the sensor horizontally, the Course Angle degree value will change in the range of 0° ~ 360°.

![3908](media/3908.png)

![4bottom](media/4bottom.png)

---

### 3.10 Servo

![1top](media/1top.png)

![67820072](media/67820072.png)

There are many specifications of servos, yet all contains three wires: brown(GND), red(power positive) and orange(signal). Colors may vary from servo brands.

![31001](media/31001.png)

![1bottom](media/1bottom.png)

#### Parameters

![2top](media/2top.png)

Operating voltage: DC 3.3 ~ 5V

Rated voltage: 4.8V

Rated current: 200 mA

Angular speed: 60°/0.12s

Operating temperature: -10°C ~ +50°C

Length: 5 LEGO holes 8x5 = 40 mm

Width: 2 LEGO holes 8x2 = 16 mm

Height: 3 LEGO height units 3.2x3 = 9.6 mm

Basic hole size: diameter of 4.8

Interface: 3pin interface spacing 2.54 mm

![2bottom](media/2bottom.png)

#### Principle

![3top](media/3top.png)

Servo is usually controlled by PWM(pulse width modulation). This 270° servo is compatible with LEGO, whose angle ranges from -45°  ~ 225°.

![31002](media/31002.png)

NOTE: 270° servo rotates within -45° ~ 225°, which is 270° in total, rather than rotating to 270°.

Before operating on 270° servo, please import library first.

![3bottom](media/3bottom.png)

#### Wiring Diagram

We connect the 270° servo to the pin io33 of the main board via 3pin wire spacing 2.54 mm.

![31003](media/31003.png)

![31004](media/31004.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\1.Code_kidsuno to open **3.10Servo.sb3** file.

![31005](media/31005.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Code Blocks**

|             Blocks              |            Code block             |
| :-----------------------------: | :-------------------------------: |
|   ![Events](media/Events.png)   |     ![begin](media/begin.png)     |
| ![servo270](media/servo270.png) | ![setdegree](media/setdegree.png) |
|  ![Control](media/Control.png)  |   ![forever](media/forever.png)   |
|  ![Control](media/Control.png)  |      ![wait](media/wait.png)      |

![line5](media/line5.png)

**Conceive:**

Add library first. Click ![add](media/add.png) to load **ESP32 Servo 270**.

![31006](media/31006.png)

1. **Main Code**

   Loop: Servo rotates to -45°, 45°, 135°, 225° accordingly with an interval of 1s between every two.

   <span style="color: rgb(10, 10, 200);">NOTE: 270° servo rotates within -45° ~ 225°, which is 270° in total, rather than rotating to 270°.</span>
   
   ![31007](media/31007.png)
   
   <br>
   
   **Build blocks:**
   
   ① Add code blocks to the editing area and build as follows:
   
   ![31008](media/31008.png)
   
   ![9top](media/9top.png)
   
   ![setdegree](media/setdegree.png) sets the pin and the rotating degree of the servo.
   
   ![9bottom](media/9bottom.png)
   
   Connect the servo to IO33 and rotate it to -45°, pause 1s.
   
   ② Duplicate the blocks.
   
   ![31009](media/31009.png)
   
   As follows:
   
   ![31010](media/31010.png)
   
   Duplicate another more twice and modify as follows:
   
   ![31011](media/31011.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, servo rotates to -45°, 45°, 135°, 225° accordingly with a pause of 1s after each rotation. And then it back to -45° to repeat these actions.

![4bottom](media/4bottom.png)

---

## 4. Comprehensive Experiment

### 4.1 Card-scanning Door-lock Control Device

It is an ideal for smart safe house that the Card-scanning Door-lock Control Device features both security and convenience.

In this experiment, we adopt RFID module and a servo to form a door-lock control device, and the RFID module works in real time. When the correct IC card is identified, the door opens; Otherwise, the door won't open.

#### Flow

![4101](media/4101.png)

#### Assembly

![line1](media/line1.png)

**Required Parts**

![41_00](media/41_00.png)

![line1](media/line1.png)

**Step 1**

![41_01](media/41_01.png)

![line1](media/line1.png)

**Step 2**

![41_02](media/41_02.png)

![line1](media/line1.png)

**Step 3**

![41_03](media/41_03.png)

![line1](media/line1.png)

**Step 4**

![41_04](media/41_04.png)

![line1](media/line1.png)

**Step 5**

![41_05](media/41_05.png)

![line1](media/line1.png)

**Step 6**

![41_06](media/41_06.png)

![line1](media/line1.png)

**Step 7**

![41_07](media/41_07.png)

![line1](media/line1.png)

**Step 8**

![41_08](media/41_08.png)

![line1](media/line1.png)

**Step 9**

![41_09](media/41_09.png)

![line1](media/line1.png)

**Step 10**



![41_10](media/41_10.png)

Calibration is required after the servo is mounted. Connect the servo to io33 on the board and connect the board to computer via USB cable.

![44_15](media/44_15.png)

Open KidsBlock, click File --> Load from your computer.

![3111](media/3111.png)

Choose D:\Code\2.Code_kidsIOT to open **Servo_Calibration.sb3** file.

![44_16](media/44_16.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

After calibration, disconnect the board to the computer and continue the assembly.

![line1](media/line1.png)

**Step 11**

![41_11](media/41_11.png)

![line1](media/line1.png)

**Step 12**

<span style="color: rgb(10, 10, 200);">Note that the two gears mesh in order to drive smoothly.</span>

![41_12](media/41_12.png)

![line1](media/line1.png)

**Step 13**

![41_13](media/41_13.png)

![line1](media/line1.png)

**Step 14**

![41_14](media/41_14.png)

![line1](media/line1.png)

**Completed**

![41_15](media/41_15.png)

![line1](media/line1.png)

#### Wiring Diagram

![4102](media/4102.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\2.Code_kidsIOT to open **4.1Card-scanning access control machine.sb3** file.

![4103](media/4103.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Conceive:**	

First, set the rotation angles for opening and closing the door. Herein, we set angle to 120° to open the door, and 0° to close the door.

Then, when the RFID module receives a correct IC card code, it drives the servo to open the door for 3s. Otherwise, servo stays still.

![line2](media/line2.png)

**Build blocks:**

1. Initialization.

   ![4104](media/4104.png)

2. Loop.

   Determine whether the IC card code is correct. If yes, servo opens the door. If not, close the door.
   
   ![4105](media/4105.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, scan the correct IC card, and the door will open for 3s and then close.

![4106](media/4106.gif)

![4bottom](media/4bottom.png)

---

### 4.2 Invasion Alarm

Invasion alarm is a device that alarms when detecting illegal invasion in a prevention area. It plays a pivotal role in security prevention, so it is widely applied to family, stores, warehouses and supermarkets. Thus, our life can be better protected from illegal invasion. Meanwhile, our personal and property safety can also be guaranteed.

In this experiment, we adopt PIR motion sensor, power amplifier and a white LED to form an invasion alarm. When someone is detected, the white LED flashes and the amplifier alarms.

#### Flow

![4201](media/4201.png)

#### Assembly

![line1](media/line1.png)

**Required Parts**

![42_00](media/42_00.png)

![line1](media/line1.png)

**Step 1**

![42_01](media/42_01.png)

![line1](media/line1.png)

**Step 2**

![42_02](media/42_02.png)

![line1](media/line1.png)

**Step 3**

![42_03](media/42_03.png)

![line1](media/line1.png)

**Step 4**

![42_04](media/42_04.png)

![line1](media/line1.png)

**Step 5**

![42_05](media/42_05.png)

![line1](media/line1.png)

**Step 6**

![42_06](media/42_06.png)

![line1](media/line1.png)

**Step 7**

![42_07](media/42_07.png)

![line1](media/line1.png)

**Completed**

![42_08](media/42_08.png)

![line1](media/line1.png)

#### Wiring Diagram

![4202](media/4202.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\2.Code_kidsIOT to open **4.2Invasion alarm.sb3** file.

![4203](media/4203.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Conceive:**

When the sensor detects a human motion (an invasion), the LED flashes and the amplifier alarms. If it detects nothing, LED will go off and the amplifier will not emit sound.

![line2](media/line2.png)

**Build blocks:**

1. Initialization: Set the pins of the PIR motion sensor, white LED module and the power amplifier.

   ![4204](media/4204.png)

2. Loop.

   Read the power level of the board input from the PIR motion sensor.

   Determine whether the power level is 1(indicates an invasion).

   - If yes, the LED flashes and the amplifier alarms.
   - If not, LED will go off and the amplifier will not emit sound.
   
   ![4205](media/4205.png)

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, when the sensor detects a human motion (an invasion), the LED flashes and the amplifier alarms.

![4206](media/4206.gif)

![4bottom](media/4bottom.png)

---

### 4.3 Track Alarm

Track alarm ensures security by detecting pressure. It will remind host when detecting tracks to ensure the safety and property.

In this experiment, we adopt a 8x8 dot matrix and a thin film pressure sensor to form a track alarm. When someone is detected stepping on the sensing area, the dot matrix displays a footprint pattern as a reminder.

#### Flow

![4301](media/4301.png)

#### Assembly

![line1](media/line1.png)

**Required Parts**

<span style="color: rgb(10, 10, 200);">Place the pressure sensitive area of the sensor on a firm, flat surface when in use. For details, please refer to Chapter 3.6.</span>

![43_00](media/43_00.png)

![line1](media/line1.png)

**Step 1**

![43_01](media/43_01.png)

![line1](media/line1.png)

**Step 2**

![43_02](media/43_02.png)

![line1](media/line1.png)

**Step 3**

![43_03](media/43_03.png)

![line1](media/line1.png)

**Step 4**

![43_04](media/43_04.png)

![line1](media/line1.png)

**Step 5**

![43_05](media/43_05.png)

![line1](media/line1.png)

**Step 6**

![43_06](media/43_06.png)

![line1](media/line1.png)

**Step 7**

![43_07](media/43_07.png)

![line1](media/line1.png)

**Step 8**

![43_08](media/43_08.png)

![line1](media/line1.png)

**Step 9**

![43_09](media/43_09.png)

![line1](media/line1.png)

**Completed**

![43_10](media/43_10.png)

![line1](media/line1.png)

#### Wiring Diagram

![4302](media/4302.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\2.Code_kidsIOT to open **4.3Track alarm.sb3** file.

![4303](media/4303.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Conceive:**

When someone steps on the pressure sensing area of the sensor, the output analog value of the sensor will decrease. 

Set a threshold first to determine whether there is pressure. When the output value is smaller than the threshold, someone steps on this area; If the value is greater than the threshold, no track is detected.

If pressure is detected, a footprint icon will be displayed on the dot matrix. 

![4306](media/4306.png)

![line2](media/line2.png)

**Build blocks:**

1. Initialization: initialize the dot matrix and set the pin of the thin film pressure sensor.

   ![4304](media/4304.png)

2. Loop.

   Determine whether the output analog value is smaller than 600 (if yes, tracks are detected).

   - analog value < 600: the dot matrix shows a footprint icon as a reminder.
   - analog value ≥ 600: the dot matrix displays nothing.

   ![4305](media/4305.png)


![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, press the thin film with your finger, and you will see the dot matrix shows a footprint.

![4303](media/4303.gif)

![4bottom](media/4bottom.png)

---

### 4.4 Motion Alarm

Motion alarm has become an important anti-theft device to protect the items in the smart safe house.

In this experiment, we adopts a three-axis magnetic sensor, a power amplifier and a 6812 RGB module to form a motion alarm. When a certain item moves to a specific angle, the alarm will be triggered: the amplifier sounds and the 6812 RGB emits lights.

#### Flow

![4401](media/4401.png)

#### Assembly

![line1](media/line1.png)

**Required Parts**

![44_00](media/44_00.png)

![line1](media/line1.png)

**Step 1**

![44_01](media/44_01.png)

![line1](media/line1.png)

**Step 2**

![44_02](media/44_02.png)

![line1](media/line1.png)

**Step 3**

![44_03](media/44_03.png)

![line1](media/line1.png)

**Step 4**

![44_04](media/44_04.png)

![line1](media/line1.png)

**Step 5**

![44_05](media/44_05.png)

![line1](media/line1.png)

**Step 6**

![44_06](media/44_06.png)

![line1](media/line1.png)

**Step 7**

![44_07](media/44_07.png)

![line1](media/line1.png)

**Completed**

![44_08](media/44_08.png)

![line1](media/line1.png)

#### Wiring Diagram

![4402](media/4402.png)

#### Test Code

Open KidsBlock and connect the board to your computer. Click **File --> Load from your computer**.

![3111](media/3111.png)

Choose D:\Code\2.Code_kidsIOT to open **4.4Motion Alarm.sb3** file.

![4403](media/4403.png)

Click ![Unconnected](media/Unconnected.png)to connect to port and then  ![2210](media/2210.png).

#### Explanations

![5top](media/5top.png)

**Conceive:**

Set a threshold angle range to determine whether objects have been moved.

Place the object and ensure its Course Angle is within the range, which means the object is not moved. Once the Course Angle value is greater than the threshold, it indicates that the item has been moved, so the amplifier alarms and the 6812 RGB lights up.

![line2](media/line2.png)

**Conceive:**

1. **Initialization**

   Initialization: initialize AK8975 three-axis magnetic sensor; set the pin and the pixel number of the 6812 RGB module and set the brightness to 5; initialize serial port; define a float variable *angle* to store the read Course Angle.

   ![4404](media/4404.png)


![line3](media/line3.png)

2. **Main Code**

   Assign the calculated Course Angle to the variable *angle* and print it on the serial monitor.

   Determine whether the angle is within 0° ~ 45°(this range can be modified according to needs).

   - 0° < angle < 45°: the amplifier stay quiet and LED keeps off.
   - angle is not within 0° ~ 45°: the object is moved, so the amplifier alarms and the LED lights up in yellow. 

   ![4405](media/4405.png)

   <br>

   **Build blocks:**

   ① Add code blocks to the editing area and build as follows:

   ![4406](media/4406.png)

   Read the Course Angle of the AK8975 three-axis magnetic sensor and assign it to variable *angle*.

   ② Add code blocks to the editing area and build as follows:

   ![4407](media/4407.png)

   ![9top](media/9top.png)

   ![greater](media/greater.png) determines whether the left value is greater than the right one. If yes, output True.

   ![less](media/less.png) determines whether the left value is smaller than the right one. If yes, output True. 

   ![and](media/and.png) determines whether the two conditions are both satisfied. If yes, output True.

   ![9bottom](media/9bottom.png)

   if else block determines whether the object is moved.

   Conditions: ![4408](media/4408.png) sets the range to 0 ~ 45. When the object is moved, the angle exceeds this range.
   
   So this block determines whether the variable *angle* is within 0 ~ 45.
   
   - If yes, execute codes in if to turn off all pixels.
   - If not, execute codes in else to light up all pixels in yellow, and the amplifier alarms.

![5bottom](media/5bottom.png)

#### Test Result

![4top](media/4top.png)

After uploading code, place the device and maintain the Course Angle within 0° ~ 45°. In the initial state, the amplifier does not emit sound and the pixels are off. Move this device, and the angle will exceed the range of 0° ~ 45°, so the amplifier alarms and the pixels are on in yellow.

![4409](media/4409.gif)

![4bottom](media/4bottom.png)

---
