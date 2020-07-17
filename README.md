# Year 8 Coding Investigation

## Requirements:

__Requirement/Feature__ | __Status__
------------ | -------------
Input for lighting condition | *__Finished__*
Input for setting to be recommended | *__Finished__*
Input for other 2 prefered settings | *__Finished__*
Check if output is too dark/bright | *__Pending__*
Logic uses 'Modified Sunny 16 Rule' | *__Pending__*
Output: Lighting Condition, Selected Settings, Recommended Settings | *__Pending__*
Automatic Mode: Asking for lighting and mode (portrait/sport) | *__Possible__*
Semi-Automatic: Ask for one preferred setting, output other 2 | *__Possible__*
Error-Checking | *__Pending__*
Summarise lighting condition, mode and settings | *__Possible__*
Be uploaded and viewable/interactable on https://groklearning.com/ | *__Pending__*


## Definitions/Knowledge:

### ISO:

The ISO is the sensor at the camera body. The sensitivity is directly proportional to the amount of light in an image (i.e. **Doubling the ISO doubles the image brightness**)

* The higher the ISO **The brighter the image** (is also directly proportional)
* The higher the ISO **The noisier the image** (as the sensor is more sensitive to light, not more light entering)

<br>
  
### Shutter Speed:

The Shutter speed is the amount of time that the ISO can have light for. Shutter Speed is directly proportional to the amount of light in an image (i.e. **Doubling the Shutter Speed doubles the image brightness**)

* The higher the Shutter Speed **The brighter the image** (is also directly proportional)
* The higher the Shutter Speed **More motion blur is visible** (as the shutter is open for longer, it can take photos while the subject has moved, making it blurred)

<br>

### Aperature:

Controls the amount of light that the sensor recieves. (**Note that the larger the f-stop number, the smaller the aperature**). Aperature is inversely proportional to the amount of light in an image (i.e. **Decreasing the f-stop by a factor of &radic;2&asymp;1.4 will double the brightness in the image.**)

* The higher the Aperature the dimmer the image (is inversely proportional)
* The lower the Aperature 

<br>

### Sunny 16 Rule:

This is a rule that states on a __sunny day__, if you set the aperature to f/16, then you should set the shutter speed to the __reciprocal__ of the ISO, for example (ISO: 200, Shutter-Speed 1/250s (as there is no 1/200s), Aperature: f/16)

### Modified Sunny 16 Rule:

This is a rule that can be used in other different lighting conditions, with the use of specific lighting conditions. These are:

__Lighting Condition__ | __Aperature__
-----------------------|--------------
Snow/Sand| f/22
Sun | f/16
Lightly Cloudy | f/11
Cloudy | f/8
Overcast | f/5.6
Sunset/Shade | f/4
Dusk | f/2.8

From these aperatures, you can then set the shutter speed as a reciprocal of the ISO (e.g. Cloudy Day = ISO: 800, Shutter Speed: 1/1000s (as there is no 1/800s, nearest setting), Aperature: f/8.0)

<br>

### Balancing the settings:

This is done by using an equation, and example will be displayed in the table below: (For a cloudy day)

__ISO__ | __Shutter Speed__ | __Aperature__ | __Result__
--------| ------------------|---------------|-----------
800 | 1/1000s | f/8.0 | 1 (Notional Baseline)
100 (&divide;8) | 1/2000s (&divide;2) | f/2.0 (x 4<sup>2</sup>) | 1 &divide; 8 &divide; 2 x 16 = 1
400 (&divide;2) | 1/500s (x2) | f/8.0 (x1) | 1 &divide; 2 x 2 x 1 = 1
1600 (x2) | 1/500s (x2) | f/16 (&divide;2<sup>2</sup>) | 1 x 2 x 2 &divide 4 = 1

<br>

### Stops:

As you may have noticed, each seemingly increment doubles or halves the brightness (approximately), and this can be known as a 'stop'. I will have a graph below with all of the possible stops: __(Note: This graph goes from least bright to most bright, from bottom to top)__


__ISO__ | __Shutter Speed__ | __Aperature__
--------|-------------------|--------------
6400 | 1/30s   | f/2.0
3200 | 1/60s   | f/2.8
1600 | 1/125s  | f/4.0
800  | 1/250s  | f/5.6
400  | 1/500s  | f/8.0
200  | 1/1000s | f/11
100  | 1/2000s | f/16
50   | 1/4000s | f/22

For you to have the same amount of brightness, all movements from the baseline have to equal out (e.g. ISO decreasing by 3 stops, Shutter Speed decreasing by 1 stop and Aperature increasing by 4 stops)

<br>

### Shot Types:

* Sports Shot __(Faster Shutter Speed required)__
  * __Example__: Decrease Shutter Speed by 2 stops (from 1/1000s to 1/4000s), increase ISO by 1 stop (from ISO 800 to ISO 1600) and increase aperature by 1 stop (f/8.0 to f/5.6)
* Portrait __(Larger Aperature is required)__
  * __Example__: Increase the Aperture by 4 stops (from f/8.0 to f/2.0), Decrease the ISO by 4 stops (from ISO 800 to ISO 50) and keep the Shutter Speed (1/1000s)

<br>

### Lighting Conditions/Camera Settings Table:
__Reference No.__ | __Lighting Condition__ | __ISO__ | __Shutter Speed__ | __Aperture__
------------------|------------------------|---------|-------------------|-------------
__8__ | Default | 6400 | 1/30s | f/2.0
__7__ | Snow/Sand | 3200 | 1/60s | f/2.8 |
__6__ | Sunny | 1600 | 1/125s | f/4.0 |
__5__ | Lightly Cloudy | 800 | 1/250s | f/5.6
__4__ | Cloudy | 400 | 1/500s | f/8.0
__3__ | Overcast | 200 | 1/1000s | f/11
__2__ | Sunset/Shade | 100 | 1/2000s | f/16
__1__ | Dusk | 50 | 1/4000s | f/22
