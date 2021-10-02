while True:
    magnitude1 = input('Input a magnitude rate: ') #Here you must input a magnitude of earthqake
    try:
        magnitude = float(magnitude1)
    except ValueError:
        print('Input a number that more than 0')
        continue 
    if (magnitude == 0):
        print('No earthquake. Try again')
        continue
    elif (0 < magnitude <= 2):
        print('Micro earthquake')    #Somewhere here you'll get the result(descriptor)
        break
    elif (2 < magnitude <= 3):
        print('Very minor earthquake')    
        break
    elif (3 < magnitude <= 4):
        print('Minor earthquake')    
        break
    elif (4 < magnitude <= 5):
        print('Light earthquake')    
        break
    elif (5 < magnitude <= 6):
        print('Moderate earthquake')    
        break
    elif (6 < magnitude <= 7):
        print('Strong earthquake')    
        break
    elif (7 < magnitude <= 8):
        print('Major earthquake')    
        break
    elif (8 < magnitude <= 10):
        print('Great earthquake')    
        break
    elif (magnitude > 10):
        print('Meteoroic earthquake')    
        break
    else:
        print('Magnitude cant be negative')
        continue
