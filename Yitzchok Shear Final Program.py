
# Import requests json and time to use throughout the pogram.
import requests
import json
import time

print("Program starting...")
time.sleep(0.5)

print("""
****WELCOME TO THE WEATHER PROGRAM***
""")

time.sleep(0.5)
# Use a function to get the data for our weather program.
def weather_data(base_url, api_key):
    
    city_name = input("Enter city name: ")
    # If statement to make sure the user only entered letters when entering a city..
    if city_name.replace(" ", "").isalpha() == False:
      print("Please enter valid city name: ")
      time.sleep(0.5)
      print("Please try again, with letters only.")
      city_name = input("Enter city name: ")

    zip_code = input("Enter zip code: ")
    # If statement to make sure the user only entered numbers when entering a zip code.
    if zip_code.isdigit() == False:
      print("Please enter a valid zip code.")
      time.sleep(0.5)
      print("Please try again, with numbers only.")
      zip_code = input("Enter zip code: ")
    # Elif statement to make sure the zip code the user entered is exactly 5 digits.  
    elif len(zip_code) != 5:
      print("Please enter exactly 5 digits for zip code.")
      time.sleep(0.5)
      zip_code = input("Enter zip code: ")
    
    quit = False
    # While loop to loop through the program until the user wants to stop.
    while quit == False:
      # Try block to try out the data and check if it works.
      try:
        complete_url = base_url + city_name + ','+ zip_code + "&appid=" + api_key
        # Use requests to get data from the website.
        response = requests.get(complete_url)
        # Use json to make the data readable to the user.
        w_data = response.json()

        description = w_data['weather'][0]['description']
        humidity = w_data['main']['humidity']
        wind = w_data['wind']['speed']
        # We convert kelvin to fahrenheit.
        temp = (w_data['main']['temp'] - 273.15) * (9/5) + 32
        temp_min = (w_data['main']['temp_min'] - 273.15) * (9/5) + 32
        temp_max = (w_data['main']['temp_max'] - 273.15) * (9/5) + 32
        feels_like = (w_data['main']['feels_like'] - 273.15) * (9/5) + 32

        print("\n")
        print("Loading your weather data...\n")

        time.sleep(.75)

        print("---------------------------")
        print("Today's Forecast for {}".format(city_name))
        print("---------------------------\n")
        print("Day:\t\t{}".format(description))
        print("Temp now:\t{}".format(round(temp,1)))
        print("Humidity:\t{}".format(humidity))
        print("Temp low:\t{}".format(round(temp_min,1)))
        print("Temp high:\t{}".format(round(temp_max,1)))
        print("Wind:\t\t{}mph".format(wind))
        print("Feels like:\t{}".format(round(feels_like,1)))
      # Except key to send back a message to the user if a key error was found.
      except KeyError:
        print('Sorry. The weather data was not found for the info you entered.')
      # Except key to send a message back to to the user if any other error happens.
      except Exception:
        print('Sorry. Something went wrong.')
       
      user_input = input("Would you like to try again? (Y|N) ")
      # If statement to loop through the program again if the user enters "Y" and wants to find weather data another time.
      if user_input.upper() == 'Y':
        city_name = input("Enter city: ")
         # If statement to make sure the user only entered letters when entering a city..
        if city_name.replace(" ", "").isalpha() == False:
          print("Please enter valid city name: ")
          time.sleep(0.5)
          print("Please try again, with letters only.")
          city_name = input("Enter city name: ")

        zip_code = input("Enter zip code: ")
        # If statement to make sure the user only entered numbers when entering a zip code.
        if zip_code.isdigit() == False:
          print("Please enter a valid zip code.")
          time.sleep(0.5)
          print("Please try again, with numbers only.")
          zip_code = input("Enter zip code: ")
         # Elif statement to make sure the zip code the user entered is exactly 5 digits.    
        elif len(zip_code) != 5:
          print("Please enter exactly 5 digits for zip code.")
          time.sleep(0.5)
          zip_code = input("Enter zip code: ")
      # Elif statemet to end the program if the user enters "N" and wants to quit.

      elif user_input.upper() == 'N':
        print("Program exiting...")
        time.sleep(.75)
        print("See you next time!")
        quit = True
      # Else statement to tell the user the entered an invalid input if they don't enter "Y" or "N".   
      else:
        print("Invalid input")
        city_name = input("Enter city: ")
        zip_code = input("Enter zip code: ")


# Use a main fuction to execute the weather_data function.
def main():
    api_key = '55592219da64379c5a1872dccb250590'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

    weather_data(base_url, api_key)


# If statement to make sure we are on the main terminal.
if __name__ == "__main__":
    main()