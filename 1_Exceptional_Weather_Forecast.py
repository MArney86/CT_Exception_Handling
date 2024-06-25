#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
def farenheit_to_celsius(farenheit): #define function to convert from farenheit to celsius
    try: #block of code we want to run but may throw error if user input is incorrect 
        celsius = (float(farenheit) - 32) * 5/9 #convert the temperature to celsius scale using the formula 
    except ValueError: #block to run if a ValueError occurs
        print("Input was not a number, please input numbers only") #user message about the wrong type of value being input
    #Task 3:
    else: #a block of code that runs if the try block throws no errors 
        print(f"The temperature {float(farenheit)}° Farenheit is {celsius}° Celsius") #print the temperature and the converted temperature in user friendly manner
    #Task 4:
    finally: #a block of code that runs whether any exceptions are thrown or not
        print("Thank you for using this Weather Forcast App") #Thank the user for using the app


#Task 1:
farenheit = input("Welcome to the Weather Forcast App \nPlease enter the temperature in Farenheit: ") #ask the user for the temperature in farenheit scale
farenheit_to_celsius(farenheit) #convert the temperature to celsius scale using the function defined in Task 2