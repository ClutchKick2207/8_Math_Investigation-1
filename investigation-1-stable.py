#importing a few modules
import time
import datetime

#initialising 'Global Variables'
currentTime = datetime.datetime.now()
iteration = 0
question = ""

#All of the data that will be used in the program:
data = [1, 'Dusk', 50, '1/4000s', 'f/22', 2, 'Sunset/Shade', 100, '1/2000s', 'f/16', 3, 'Overcast', 200, '1/1000s', 'f/11', 4, 'Cloudy', 400, '1/500s', 'f/8.0', 5, 'Lightly Cloudy', 800, '1/250s', 'f/5.6', 6, 'Sunny', 1600, '1/125s', 'f/4.0', 7, 'Snow/Sand', 3200, '1/60s', 'f/2.8']

#A set with all of the presets:
preset = {'Snow/Sand': {'ISO' : 3200, 'SS' : '1/60s', 'A' : 'f/2.8'}, 'Sunny' : {'ISO' : 1600, 'SS' : '1/125s', 'A' : 'f/4.0'}, 'Lightly Cloudy' : { 'ISO' : 800, 'SS' : '1/250s', 'A' : 'f/5.6'}, 'Cloudy' : {'ISO' : 400, 'SS' : '1/500s', 'A' : 'f/8.0'}, 'Overcast' : {'ISO' : 200, 'SS' : '1/1000s', 'A' : 'f/11'}, 'Sunset' : {'ISO' : 100, 'SS' : '1/2000s', 'A' : 'f/16'}, 'Shade' : {'ISO' : 100, 'SS' : '1/2000s', 'A' : 'f/16'}, 'Dusk' : {'ISO' : 50, 'SS' : '1/4000s', 'A' : 'f/22'}}

#Greets you in the correct way:
if currentTime.hour < 12:
  print('\n')
  print('\n')
  print('Good Morning!')
  time.sleep(5)
  print('Please follow the listed instructions to use this program.')
elif 12 <= currentTime.hour < 18:
  print('\n')
  print('\n')
  print('Good Afternoon!')
  time.sleep(5)
  print('Please follow the listed instructions to use this program.')
else:
  print('\n')
  print('\n')
  print('Good Evening!')
  time.sleep(5)
  print('Please follow the listed instructions to use this program.')

time.sleep(3)

def restart():
  #Initialising variables for the process 'restart'
    l = ""
    s = ""
    iso = ""
    aperature = ""
    mode = ""
    shutterspeed = ""
    shutterindex = 0
    while mode != 'p' and mode != 'r':
      mode = input('Which mode would like to use? [Suggest a Preset (p) || Recommend a Setting (r)]: ')
      if mode != 'p' and mode != 'r':
        print('Please try again')
    time.sleep(2)

    if 'r' in mode or 'R' in mode:
      while l != "Dusk" and l != "Sunset/Shade" and l != "Overcast" and l != "Cloudy" and l != "Lightly Cloudy" and l != "Sunny" and l != "Snow/Sand" and l != "Default":
        print('Please enter the lighting condition [Dusk, Sunset/Shade, Overcast, Cloudy, Lightly Cloudy, Sunny, Snow/Sand]:')
        l = input('Please enter the lighting condition: ')
        time.sleep(2)
        if l != "Dusk" and l != "Sunset/Shade" and l != "Overcast" and l != "Cloudy" and l != "Lightly Cloudy" and l != "Sunny" and l != "Snow/Sand" and l != "Default":
          print('Your input seems to be invalid (Please type exactly as it is written)')
        lightingindex = data.index(l)
        lr = lightingindex - 1
        lightingref = data[lr]
        while s != 'ISO' and s != 'ss' and s != 'a':
          s = input('Which setting  recommend [ISO [ISO] || Shutter Speed (ss) || Aperture (a)]? ')
          if s != 'ISO' and s != 'ss' and s != 'a':
              print('Your input seems to be invalid (Please type exactly as it is written)')
        s = s.lower()
        print('\n')

  #SHUTTER SPEED
    if 'ss' in s or 'SS' in s or 'shutter' in s or 'Shutter' in s:
      while iso != 3200 and iso != 1600 and iso != 800 and iso != 400 and iso != 200 and iso != 100 and iso != 50:
        print('Please enter the ISO [3200 || 1600 || 800 || 400 || 200 || 100 || 50]: ')
        iso = int(input('Please enter your ISO: '))
        while iso not in data:
          iso = int(input('Please enter your ISO: '))
          print('\n')
      print('\n')
      time.sleep(2)
      while aperature != 'f/22' and aperature != 'f/16' and aperature != 'f/8.0' and aperature != 'f/5.6' and aperature != 'f/4.0' and aperature != 'f/2.8':
        print('Please enter the Aperature [f/22 || f/16 || f/11 || f/8.0 || f/5.6 || f/4.0 || f/2.8]: ')
        aperature = str(input('Please enter your Aperture (with "f/"): '))
        while aperature not in data:
            aperature = str(input('Please enter your Aperture (with "f/"): '))
      time.sleep(2)
      print('\n')
      time.sleep(0.5)
      print('Your selected options are: ')
      time.sleep(0.5)
      print('Lighting: ',l)
      time.sleep(0.5)
      print('ISO: ',iso)
      time.sleep(0.5)
      print('Aperture: ',aperature)
      time.sleep(0.5)
      print('\n')
      time.sleep(0.5)
      isoindex = data.index(iso)
      isor = isoindex - 2
      isoref = data[isor]
      apertureindex = data.index(aperature)
      aperturer = apertureindex - 4
      apertureref = data[aperturer]
      refsum = apertureref + isoref + lightingref
      if refsum >= 16:
        decreasen = refsum - 16
        print(f'Too Bright! Please decrease some of your settings by {decreasen} stops.')
      elif refsum <= 16:
        decreasen = refsum - 16
        print(f'Too Dark! Please increase some of your settings by {decreasen} stops.')
      else:
          shutterref = 16 - refsum
          shutterrefindex = data.index(shutterref)
          shutterindex = shutterrefindex + 3
      time.sleep(2)
      print('The recommended Shutter Speed is: ',data[shutterindex])
      time.sleep(0.5)
      print('Thank-You for using this program.')

  #ISO
    if 'iso' in s:
      while aperature != 'f/22' and aperature != 'f/16' and aperature != 'f/8.0' and aperature != 'f/5.6' and aperature != 'f/4.0' and aperature != 'f/2.8':
        print('Please enter the Aperature [f/22 || f/16 || f/11 || f/8.0 || f/5.6 || f/4.0 || f/2.8]: ')
        aperature = str(input('Please enter your Aperture (with "f/"): '))
        while aperature not in data:
            aperature = str(input('Please enter your Aperture (with "f/"): '))
        time.sleep(2)
        print('\n')

        while shutterspeed != '1/4000s' and shutterspeed != '1/2000s' and shutterspeed != '1/1000s' and shutterspeed != '1/500s' and shutterspeed != '1/250s' and shutterspeed != '1/125s' and shutterspeed != '1/60s':
          print('Please enter your shutter-speed [1/4000s, 1/2000s, 1/1000s, 1/500s, 1/250s, 1/125s, 1/60s]: ')
          shutterspeed = input('Please enter your Shutter Speed: ')
          while shutterspeed not in data:
            shutterspeed = input('Please enter your Shutter Speed: ')
            print('\n')
        time.sleep(2)

        print('\n')
        time.sleep(0.5)
        print('Your selected options are: ')
        time.sleep(0.5)
        print('Lighting: ',l)
        time.sleep(0.5)
        print('Shutter Speed: ',shutterspeed)
        time.sleep(0.5)
        print('Aperture: ',aperture)
        time.sleep(0.5)
        print('\n')
        time.sleep(0.5)
        apertureindex = data.index(aperture)
        aperturer = apertureindex - 4
        apertureref = data[aperturer]
        shutterspeedindex = data.index(shutterspeed)
        shutterspeedr = shutterspeedindex - 3
        shutterspeedref = data[shutterspeedr]
        refsum = apertureref + shutterspeedref + lightingref
        if refsum >= 16:
          decreasen = refsum - 16
          print('Too Bright! Please decrease some of your settings by',decreasen,'stops.')
        elif refsum <= 16:
          decreasen = refsum - 16
          print(f'Too Dark! Please increase some of your settings by {decreasen} stops.')
        else:
            isoref = 16 - refsum
            isorefindex = data.index(isoref)
            isoindex = isorefindex + 2
            time.sleep(2)
            print('The recommended ISO is: ',data[isoindex])
            time.sleep(0.5)
            print('Thank-You for using this program.')

    #APERTURE
    if 'a' in s or 'A' in s or 'Aperture' in s or 'aperture' in s:
        while iso != 3200 and iso != 1600 and iso != 800 and iso != 400 and iso != 200 and iso != 100 and iso != 50:
          print('Please enter the ISO [3200 || 1600 || 800 || 400 || 200 || 100 || 50]: ')
          iso = int(input('Please enter your ISO: '))
          while iso not in data:
            iso = int(input('Please enter your ISO: '))
            print('\n')
        time.sleep(2)
        print('\n')

        while shutterspeed != '1/4000s' and shutterspeed != '1/2000s' and shutterspeed != '1/1000s' and shutterspeed != '1/500s' and shutterspeed != '1/250s' and shutterspeed != '1/125s' and shutterspeed != '1/60s':
          print('Please enter your shutter-speed [1/4000s, 1/2000s, 1/1000s, 1/500s, 1/250s, 1/125s, 1/60s]: ')
          shutterspeed = input('Please enter your Shutter Speed: ')
          while shutterspeed not in data:
            shutterspeed = input('Please enter your Shutter Speed: ')
            print('\n')

        time.sleep(2)
        print('\n')
        time.sleep(0.5)
        print('Your selected options are: ')
        time.sleep(0.5)
        print(f'Lighting: {l}')
        time.sleep(0.5)
        print(f'ISO: {iso}')
        time.sleep(0.5)
        print(f'Shutter Speed: {shutterspeed}')
        time.sleep(0.5)
        print('\n')
        time.sleep(0.5)
        isoindex = data.index(iso)
        isor = isoindex - 2
        isoref = data[isor]
        shutterspeedindex = data.index(shutterspeed)
        shutterspeedr = shutterspeedindex - 3
        shutterspeedref = data[shutterspeedr]
        refsum = isoref + shutterspeedref + lightingref
        if refsum >= 16:
          decreasen = refsum - 16
          print(f'Too Bright! Please decrease some of your settings by {decreasen} stops.')
        elif refsum <= 16:
          decreasen = refsum - 16
          print(f'Too Dark! Please increase some of your settings by {decreasen} stops.')
        else:
          apertureref = 16 - refsum
          aperturerefindex = data.index(apertureref)
          apertureindex = aperturerefindex + 4
          time.sleep(2)
          print('The recommended Aperture is: ',data[apertureindex])
          time.sleep(0.5)
          print('Thank-You for using this program.')

    if 'p' in mode or 'P' in mode:
      print('Please enter your lighting condition [Dusk, Sunset/Shade, Overcast, Cloudy, Lightly Cloudy, Sunny, Snow/Sand]:')
      while l != 'Dusk' and l != 'Sunset/Shade' and l != 'Overcast' and l != 'Cloudy' and l != 'Lightly Cloudy' and l != 'Sunny' and l != 'Snow/Sand':
        l = input('In which lighting condition is your shot? ')
        if l != 'Dusk' and l != 'Sunset/Shade' and l != 'Overcast' and l != 'Cloudy' and l != 'Lightly Cloudy' and l != 'Sunny' and l != 'Snow/Sand':
          print('Please try again: ')
      time.sleep(2)

      for i in preset:
        if i == l:
          print('The preset for that lighting condition is: ')
          time.sleep(0.5)
          print(preset[l])

restart()

while question != 'y' and question != 'n':
  question = input('Do you want to repeat the program? [y/n] ')
  if question != 'y' and question != 'n':
    print('Please try again!')
if question == 'y':
  print('restarting...')
  time.sleep(2)
  restart()
if question == 'n':
  print('exiting...')
  time.sleep(2)
  exit()
