import time 
import sys

b = ""
x = ""
what = ""
sett = ""
n = ""

print('Hello! Welcome to the PMS Photography Program.')
time.sleep(1.5)
print('I am your digital assistant, PHOTOGRAPH, here to quickly calculate the camera settings you will require')
while x != 'Y':
  x = input('Are you ready to get started?(Y or N): ')
  if x != 'Y'and x != 'N':
    print('Oops! You seem to have given an invalid answer. Please try again.')
  if x == "Y":
    print('Great!')
  if x == 'N':
    print('See you next time, then!')
    sys.exit()
  
print('')
time.sleep(1.5)

c_set = settings = [['1', 'Dusk', '50', '1/4000s', 'f/22'], 
                    ['2', 'Sunset/Shade', '100', '1/2000s', 'f/16'], 
                    ['3', 'Overcast', '200', '1/1000s', 'f/11'], 
                    ['4', 'Cloudy', '400', '1/500s', 'f/8'], 
                    ['5', 'Lightly Cloudy', '800', '1/250s', 'f/5.6'], 
                    ['6', 'Sunny', '100', '1/2000s', 'f/4'], 
                    ['7', 'Snow/Sand', '3200', '1/60s', 'f/2.8']]
ap_set = [['1', 'f/22'],
          ['2', 'f/16'],
          ['3', 'f/11'],
          ['4', 'f/8.0'],
          ['5', 'f/5.6'],
          ['6', 'f/4.0'],
          ['7', 'f/2.8'],
          ['8', 'f/2.0']]
iso_set = [['1', '50'],
           ['2', '100'],
           ['3', '200'],
           ['4', '400'],
           ['5', '800'],
           ['6', '1600'],
           ['7', '3200'],
           ['8', '6400']]
shut_set = [['1', '1/4000s'],
            ['2', '1/2000s'],
            ['3', '1/1000s'],
            ['4', '1/500s'],
            ['5', '1/250s'],
            ['6', '1/125s'],
            ['7', '1/60s'],
            ['8', '1/30s']]

print('Here are the optimal settings for each type of weather as suggested by the sunny sixteen rule;')
print('\n')
time.sleep(1)
print('1')
print('Dusk') 
print('ISO: 50')
print('SHUTTER SPEED: 1/4000s')
print('APERTURE: f/22')
time.sleep(1.5)
print('2')
print('Sunset/Shade') 
print('ISO: 100')
print('SHUTTER SPEED: 1/2000s')
print('APERTURE: f/16')
time.sleep(1.5)
print('3')
print('Overcast')
print('ISO: 200')
print('SHUTTER SPEED: 1/1000s')
print('APERTURE: f/11')
time.sleep(1.5)
print('4')
print('Cloudy')
print('ISO: 400')
print('SHUTTER SPEED: 1/500s')
print('APERTURE: f/8')
time.sleep(1.5)
print('5')
print('Lightly Cloudy')
print('ISO: 800')
print('SHUTTER SPEED: 1/250s')
print('APERTURE: f/5.6')
time.sleep(1.5)
print('6')
print('Sunny')
print('ISO: 100')
print('SHUTTER SPEED: 1/2000s')
print('APERTURE: f/4')
time.sleep(1.5)
print('7')
print('Snow/Sand')
print('ISO: 3200')
print('SHUTTER SPEED: 1/60s')
print('APERTURE: f/2.8')
print('\n')

time.sleep(2)
print('Please enter the weather condition according to the number provided above it')

while b != '1' and b != '2' and b != '3' and b != '4' and b != '5' and b != '6' and b != '7':
  b = input(str("What's the weather like today?: "))
  if b != '1' and b != '2' and b != '3' and b != '4' and b != '5' and b != '6' and b != '7':
    print('Oops! You seem to have given an invalid answer. Please try again.')
    
print('\n')
print('Ok! Now this is where it gets complicated.') 
print("To help you out, I'm going to include explanations of what ISO, Shutter Speed, Aperture and F stop are.")

while what != '2':
  what =input('If you would like to skip this, press 1. If not press 2: ')
  if what != '2' and what != '1':
    print('Oops! You seem to have given an invalid answer. Please try again.')
  if what == '1':
    break
  if what == '2':
    print('explainy thingy')

while sett != 'ISO' and sett != 'Shutter Speed' and sett!= 'Aperture': 
  sett = input('What setting would you like me to reccomend?: ')
  if sett != 'ISO' and sett != 'Shutter Speed' and sett!= 'Aperture': 
    print('Oops! You seem to have given an invalid answer. Please try again.')
  if sett == 'ISO':
    print(ap_set)
    time.sleep(2)
    i = input('Please enter the Aperture (using the reference numbers): ')
    print(shut_set)
    time.sleep(2)
    w = input('Please enter the Shutter Speed (using the reference numbers): ')
    x = (int(b) - 1)
    tot = (int(b) - int(i))
    tot2 = (int(b) - int(w))
    yay = (tot - tot2)
    if tot - tot2 == 0:
      print('Your reccomended ISO is: ' + str((ap_set[x][1])))
    if tot >= 1 and tot != 0:
      print('You need to increase your Aperture and Shutter Speed by ' + str(yay ))
    if tot <= 1 and tot != 0:
      print('You need to decrease your Aperture and Shutter Speed by ' + str(yay))
  if sett == 'Shutter Speed':
    print(iso_set)
    time.sleep(2)
    l = input('Please enter the ISO (using the reference numbers): ')
    print(ap_set)
    time.sleep(2)
    k = input('Please enter the Aperture (using the reference numbers): ')
    x = (int(b) - 1)
    tot = (int(b) - int(l))
    tot2 = (int(b) - int(k))
    yay = (tot - tot2)
    if tot - tot2 == 0:
      print('Your reccomended Shutter Speed is: ' + str((ap_set[x][1])))
    if tot >= 1 and tot != 0:
      print('You need to increase your ISO and Aperture by ' + str(yay ))
    if tot <= 1 and tot != 0:
      print('You need to decrease your ISO and Aperture by ' + str(yay))
  if sett == 'Aperture':
    print(iso_set)
    time.sleep(2)
    m = input('Please enter the ISO (using the reference numbers): ')
    print(shut_set)
    time.sleep(2)
    y = input('Please enter the Shutter Speed (using the reference numbers): ')
    x = (int(b) - 1)
    tot = (int(b) - int(m))
    tot2 = (int(b) - int(y))
    yay = (tot - tot2)
    if tot - tot2 == 0:
      print('Your reccomended aperture is: ' + str((ap_set[x][1])))
    if tot >= 1 and tot != 0:
      print('You need to increase your ISO and Shutter Speed by ' + str(yay ))
    if tot <= 1 and tot != 0:
      print('You need to decrease your ISO and Shutter Speed by ' + str(yay))
