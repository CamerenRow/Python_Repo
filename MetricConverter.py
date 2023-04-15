options = int(input('What do you want to convert? (inches and centimeters(1) or Farenheit and Celcius(2)): '))

def Measurement():
    print('Measure')
    Measurement_Var = int(input('what do you want to convert? (inches to centimeters(1) or centimeters to inches(2)): '))

    if(Measurement_Var == 1):
        Inchlength = int(input('How long is your object in inches?: '))
        Centimeterlength = str(Inchlength * 2.54)
        print('Your object is ' + Centimeterlength + ' in centimeters')
    elif(Measurement_Var == 2):
        Centimeterlength = float(input('How long is your object in Centimeters?: '))
        Inchlength = str(Centimeterlength / 2.54)
        print('Your object is ' + Inchlength + ' in centimeters')
    else:
        print('Please type a valid number and try again')

def Temperature():
    Temperature_Var = int(input('what do you want to convert? (Farenheit to celcius(1) or celcius to Farenheit(2))?: '))
    if(Temperature_Var == 1):
        Farenheit = int(input('What temperature is your object in Farenheit?: '))
        Celcius = str((Farenheit - 32) * 5/9)
        print('Your object is ' + Celcius + ' degrees celcius.')
    elif(Temperature_Var == 2):
        Celcius = int(input('What temperature is your object in Celcius?: '))
        Farenheit = str((Celcius * 9/5) + 32)
        print('Your object is ' + Farenheit + ' degrees Farenheit.')
    else:
        print('Please type a valid number and try again')

if(options == 1):
    Measurement()
elif(options == 2):
    Temperature()
else:
    print('Enter a valid option')