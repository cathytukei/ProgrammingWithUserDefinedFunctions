
def hotel_cost(num_nights): # Calculates the hotel cost based on the number of nights
  price_per_night = 100  # assuming price per night is £100
  return num_nights * price_per_night # returns total hotel price ie hotel_price

def plane_cost(city_flight): # Calculates the plane cost based on the chosen city
  prices = {"Mbale": 1000,"Kampala": 2000, "Jinja": 3000,} # creating a dictionary of 3 cities each with their price
  return prices.get(city_flight, 0)  # Returns 0 if the city the user inputs is not found and returns the cost of the city user inputs if found ie the plane_price

def car_rental(rental_days): # Calculates the total car rental cost based on rental days
  daily_rental_cost = 50  # Assuming the daily cost of rent is £50
  return rental_days * daily_rental_cost # returns the total cost of car rental ie the car_price


def holiday_cost(num_nights, city_flight, rental_days): # Calculates the total holiday cost based on individual costs
  hotel_price = hotel_cost(num_nights)
  plane_price = plane_cost(city_flight)
  car_price = car_rental(rental_days)
  total_cost = hotel_price + plane_price + car_price
  return total_cost # returns summation of all three individual costs

# Get user input
city_flight = input("Enter the city you'll be flying to (Mbale, Kampala, Jinja): ").title() # asks user to input the city of travel and concverts the first letter of the city to capital
num_nights = int(input("Enter the number of nights staying at the hotel: ")) # asks user to input number of nights at the hotel
rental_days = int(input("Enter the number of days renting a car: ")) # asks user to input the number of rental cays for the car

# Calculate total cost
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print holiday details
print(f"\n**Holiday Details**") # prints this heading on a new line
print(f"City: {city_flight}") # prints the city name
print(f"Number of Nights: {num_nights}") # prints number of flights
print(f"Rental Days: {rental_days}") # prints then number of rental days
print(f"Hotel Cost: £{hotel_cost(num_nights)}") # prints the hotel cost
print(f"Plane Cost: £{plane_cost(city_flight)}") # prints the flight cost
print(f"Car Rental Cost: £{car_rental(rental_days)}") # prints the price of the car rental
print(f"Total Holiday Cost: £{total_cost}") # prints the total cost of the holday
