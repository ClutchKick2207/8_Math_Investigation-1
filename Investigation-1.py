import time

time.sleep(0.1) #Allows for some look-ahead into code for linting (more for the programmer)

#Setting all variables to an intial state (because cache)
light = ""
funky = ""
function = ""
x = ""
y = ""
restart = False
ss = ""
ap = ""
xxx = ""
yyy = ""
calculation1 = ""
calculation2 = ""

#Default/Baseline values for lighting conditions
listy = [["Dusk", "50", "1/4000s", "f/22"], ["Sunset/Shade", "100", "1/2000s", "f/16"], ["Overcast", "200", "1/1000s", "f/11"], ["Cloudy", "400", "1/500s", "f/8.0"], ["Lightly Cloudy", "800", "1/250s", "f/5.6"], ["Sunny", "1600", "1/125s", "f/4.0"], ["Snow/Sand", "3200", "1/60s", "f/2.8"], ["Default", "6400", "1/30s", "f/2.0"]]
listyv2 = [["Dusk", 50, 4000, 22], ["Sunset/Shade", 100, 2000, 16], ["Overcast", 200, 1000, 11], ["Cloudy", 400, 500, 8.0], ["Lightly Cloudy", 800, 250, 5.6], ["Sunny", 1600, 125, 4.0], ["Snow/Sand",3200, 60, 2.8], ["Default", 6400, 30, 2.0]]

#How to access these the above list, and also is helpful as Dictionaries are easier to navigate in this instance
dictionary = {"Dusk": 0, "Sunset/Shade":1, "Overcast": 2, "Cloudy": 3, "Lightly Cloudy": 4, "Sunny": 5, "Snow/Shade": 6, "Default": 7}

#All the different "Stops" (Going in order from darkest to brightest)
stops_ISO = {50: 1, 100: 2, 200: 3, 400: 4, 800: 5, 1600: 6, 3200: 7, 6400: 8}
stops_Ap = {22.0: 1, 16.0: 2, 11.0: 3, 8.0: 4, 5.6: 5, 4.0: 6, 2.8: 7, 2.0: 8}
stops_SS = {4000: 1, 2000: 2, 1000: 3, 500: 4, 250: 5, 125: 6, 60: 7, 30: 8} 


#Code Begins:
if restart == False:
  while funky != "Suggest All" and funky != "Suggest ISO" and funky != "Suggest Aperature" and funky != "Suggest Shutter-Speed" and funky != "Check my values":
    print("Please enter the function that you would like this program to run (between Suggest All, Suggest ISO, Suggest Aperature and Suggest Shutter-Speed):")
    funky = input('What function do you choose?: ')
    if funky != "Suggest All" and funky != "Suggest ISO" and funky != "Suggest Aperature" and funky != "Suggest Shutter-Speed" and funky != "Check my values":
      print('That input seems to be invalid, please try again!')
    print(f"You entered: {funky}")
    time.sleep(2)



#This code block is for the function "Suggest All":
if funky == "Suggest All":
  print("Please enter the lighting condition (between Dusk, Sunset/Shade, Overcast, Cloudy, Lighty Cloudy, Sunny, Snow/Sand, Default):")
  while light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default":
    light = input("What are the current lighting conditions? ")
    if light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default":
      print("Your information seems to be invalid, please try again...")
  print(f"You entered {light}")

  time.sleep(2)
  n = str(light)
  x = int((dictionary[n]))
  y = (listy[x-1])

  print(f"For the lighting condition {n}, I would recommend your ISO to be {y[1]}, your Shutter Speed to be {y[2]} and your Aperature to be {y[3]}")

  restart = input("Do you want for this program to repeat? (Y/N): ")
  if restart == 'N':
    print("Goodbye, and take some good photos!")
    time.sleep(5)
    restart = True
    exit()
  if restart == 'Y':
    print('Program is going to continue')
    print("\n")
    print("\n")
    time.sleep(2)
    restart = False
      


#This code block is for "Suggest ISO"
if funky == "Suggest ISO":
  while light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default":
    print("Please enter the lighting condition (between Dusk, Sunset/Shade, Overcast, Cloudy, Lighty Cloudy, Sunny, Snow/Sand, Default):")
    light = input("What are the current lighting conditions? ")
    if light != "Dusk" and light != "Sunset/Shade" and light != "Overcast" and light != "Cloudy" and light != "Lightly Cloudy" and light != "Sunny" and light != "Snow/Sand" and light != "Default":
      print("Your information seems to be invalid, please try again.")
    
  print(f'You entered the lighting condition: {light}')
  time.sleep(2)

  while ss != 30 and ss != 60 and ss != 125 and ss != 250 and ss != 500 and ss != 1000 and ss != 2000 and ss != 4000:
    ss = int(input('Please enter your shutter speed (Please just enter the number): '))
    if ss != 30 and ss != 60 and ss != 125 and ss != 250 and ss != 500 and ss != 1000 and ss != 2000 and ss != 4000:
      print("Please only enter the number present (e.g. 1000 instead of 1/1000s)")
    print(f"You entered {ss}")

  while ap != 2.0 and ap != 2.8 and ap != 4.0 and ap != 5.6 and ap != 8 and ap != 11 and ap != 16 and ap != 22:
    ap = float(input('Please enter your aperature (Please just enter the number): '))
    if ap != 2.0 and ap != 2.8 and ap != 4.0 and ap != 5.6 and ap != 8.0 and ap != 11.0 and ap != 16.0 and ap != 22.0:
      print("Please only enter the number present (e.g. 2.0 instead of f/2.0)")
    print(f"You entered {ap}")

  n = str(light)
  x = int((dictionary[n]))
  y = (listy[x])
  m = (listyv2[x])


  #This is the main 'logic' towards the program:
  if ap == y[-1] and ss == y[2]:
    print(f'Your current settings match the stored baseline, so I would recommend you use {y[1]} as your ISO.')
    time.sleep(1)
  else:
    print('The program will now calculate what setting you should use for your ISO...')
    calculation1 = m[-1]
    calculation2 = m[2]
    

  restart = input("Do you want for this program to repeat? (Y/N): ")
  if restart == 'N':
    print("Goodbye, and take some good photos!")
    time.sleep(5)
    restart = True
    exit()
  if restart == 'Y':
    print('Program is going to continue')
    print("\n")
    print("\n")
    time.sleep(2)
    restart = False
