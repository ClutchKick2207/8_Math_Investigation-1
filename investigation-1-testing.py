import time

# REF, LC, ISO, SS, A
data = [1, 'Dusk', 50, '1/4000s', 'f/22', 2, 'Sunset/Shade', 100, '1/2000s', 'f/16', 3, 'Overcast', 200, '1/1000s', 'f/11', 4, 'Cloudy', 400, '1/500s', 'f/8.0', 5, 'Lightly Cloudy', 800, '1/250s', 'f/5.6', 6, 'Sunny', 1600, '1/125s', 'f/4.0', 7, 'Snow/Sand', 3200, '1/60s', 'f/2.8']

preset = {
    'Snow/Sand' : {
        'ISO' : 3200,
        'SS' : '1/60s',
        'A' : 'f/2.8'
    },
    'Sunny' : {
        'ISO' : 1600,
        'SS' : '1/125s',
        'A' : 'f/4.0'
    },
    'Lightly Cloudy' : {
        'ISO' : 800,
        'SS' : '1/250s',
        'A' : 'f/5.6'
    },
    'Cloudy' : {
        'ISO' : 400,
        'SS' : '1/500s',
        'A' : 'f/8.0'
    },
    'Overcast' : {
        'ISO' : 200,
        'SS' : '1/1000s',
        'A' : 'f/11'
    },
    'Sunset' : {
        'ISO' : 100,
        'SS' : '1/2000s',
        'A' : 'f/16'
    },
    'Shade' : {
        'ISO' : 100,
        'SS' : '1/2000s',
        'A' : 'f/16'
    },
    'Dusk' : {
        'ISO' : 50,
        'SS' : '1/4000s',
        'A' : 'f/22'
    }}

print('Welcome to this Software.')
print()

def restart():
  mode = input('Which mode would like to use? [Suggest a Preset (p) //Recommend a Setting (r): ')

  if 'r' in mode or 'R' in mode:
    print('Lighting Conditions include:')
    print('''
     - Dusk
     - Sunset/Shade
     - Overcast
     - Cloudy
     - Lightly Cloudy
     - Sunny
     - Snow/Sand
    ''')
    l = input('In which lighting condition is your shot?  ')
    lightingindex = data.index(l)
    lr = lightingindex - 1
    lightingref = data[lr]
    s = input('Which setting would like us to recommend [ISO, Shutter Speed (ss), Aperture (a)]? ')
    s = s.lower()

  #SHUTTER SPEED_________________
    if 'ss' in s or 'SS' in s or 'shutter' in s or 'Shutter' in s:
      print('ISO settings include: ')
      print('''
      - 3200
      - 1600
      - 800
      - 400
      - 200
      - 100
      - 50
      ''')
      iso = int(input('Please enter your ISO: '))
      while iso not in data:
        iso = int(input('Please enter your ISO: '))
      print()
      print('Aperture Settings include: ')
      print('''
      - f/22
      - f/16
      - f/11
      - f/8.0
      - f/5.6
      - f/4.0
      - f/2.8
      ''')
      aperture = input('Please enter your Aperture (with "f/"): ')
      while aperture not in data:
        aperture = input('Please enter your Aperture (with "f/"): ')
      print()
      print('Your selected options are: ')
      print('Lighting: ',l)
      print('ISO: ',iso)
      print('Aperture: ',aperture)
      print()
      isoindex = data.index(iso)
      isor = isoindex - 2
      isoref = data[isor]
      apertureindex = data.index(aperture)
      aperturer = apertureindex - 4
      apertureref = data[aperturer]
      refsum = apertureref + isoref + lightingref
      if refsum >= 16:
        decreasen = refsum - 16
        print('Too Bright! Please decrease some of your settings by',decreasen,'stops.')
      else:
        shutterref = 16 - refsum
        shutterrefindex = data.index(shutterref)
        shutterindex = shutterrefindex + 3
        print('The recommended Shutter Speed is: ',data[shutterindex])
        print('Thank-You for using this program.')

  #ISO_________________
    if 'iso' in s:
      print('Aperture Settings include: ')
      print('''
      - f/22
      - f/16
      - f/11
      - f/8.0
      - f/5.6
      - f/4.0
      - f/2.8
      ''')
      aperture = input('Please enter your Aperture (with "f/"): ')
      while aperture not in data:
        aperture = input('Please enter your Aperture (with "f/"): ')
      print()
      print('Shutter Speeds include: ')
      print('''
      - 1/4000s
      - 1/2000s
      - 1/1000s
      - 1/500s
      - 1/250s
      - 1/125s
      - 1/60s
      ''')
      shutterspeed = input('Please enter your Shutter Speed: ')
      while shutterspeed not in data:
        shutterspeed = input('Please enter your Shutter Speed: ')
      print()
      print('Your selected options are: ')
      print('Lighting: ',l)
      print('Shutter Speed: ',shutterspeed)
      print('Aperture: ',aperture)
      print()
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
      else:
        isoref = 16 - refsum
        isorefindex = data.index(isoref)
        isoindex = isorefindex + 2
        print('The recommended ISO is: ',data[isoindex])
        print('Thank-You for using this program.')

    #APERTURE_________________
    if 'a' in s or 'A' in s or 'Aperture' in s or 'aperture' in s:
      print('ISO settings include: ')
      print('''
      - 3200
      - 1600
      - 800
      - 400
      - 200
      - 100
      - 50
      ''')
      iso = int(input('Please enter your ISO: '))
      while iso not in data:
        iso = int(input('Please enter your ISO: '))
      print()
      print('Shutter Speeds include: ')
      print('''
      - 1/4000s
      - 1/2000s
      - 1/1000s
      - 1/500s
      - 1/250s
      - 1/125s
      - 1/60s
      ''')
      shutterspeed = input('Please enter your Shutter Speed: ')
      while shutterspeed not in data:
        shutterspeed = input('Please enter your Shutter Speed: ')
      print()
      print('Your selected options are: ')
      print('Lighting: ',l)
      print('ISO: ',iso)
      print('Shutter Speed: ',shutterspeed)
      print()
      isoindex = data.index(iso)
      isor = isoindex - 2
      isoref = data[isor]
      shutterspeedindex = data.index(shutterspeed)
      shutterspeedr = shutterspeedindex - 3
      shutterspeedref = data[shutterspeedr]
      refsum = isoref + shutterspeedref + lightingref
      if refsum >= 16:
        decreasen = refsum - 16
        print('Too Bright! Please decrease some of your settings by',decreasen,'stops.')
      else:
        apertureref = 16 - refsum
        aperturerefindex = data.index(apertureref)
        apertureindex = aperturerefindex + 4
        print('The recommended Aperture is: ',data[apertureindex])
        print('Thank-You for using this program.')

  if 'p' in mode or 'P' in mode:
    print('Lighting Conditions include:')
    print('''
     - Dusk
     - Sunset/Shade
     - Overcast
     - Cloudy
     - Lightly Cloudy
     - Sunny
     - Snow/Sand''')
    l = input('In which lighting condition is your shot?  ')
    for i in preset:
      if i == l:
        print('The preset for that lighting condition is: ')
        print(preset[l])

restart = input('Would you like to restart the program [y/n]? ')
if 'y' in restart or 'Y' in restart:
  restart()
if 'n' in restart or 'N' in restart:
  print('Thank-You for using this program.')
  exit()
else:
  print('Your input was not recognised.')
  exit()



  
  

  
