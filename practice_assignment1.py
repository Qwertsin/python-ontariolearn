"""
practice_assignment1.py


"""
# defines cars as an int variable and sets value to 100
cars = 100
# defines space_in_a_car as a floating point variable and sets value to 4.0
space_in_a_car = 4.0
# defines drivers as an int variable and sets value to 30
drivers = 30
# defines passengers as an int variable and sets value to 90
passengers = 90
# defines cars_not_driven as cars less drivers and is an int
cars_not_driven = cars - drivers
# defines cars_driven as the current value of drivers which is an int value of 30
cars_driven = drivers
# defines carpool_capacity as the product of cars driven (int 30) and space_in_a_car (float 4.0) result is (float 120.0)
carpool_capacity = cars_driven * space_in_a_car
# defines average_passengers_per_car as the quotient of passengers (int 90) and cars driven (int 30) result is (float 3)
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")


"""
1 The error in the script was that carpool_capacity was referenced incorrectly in the 3rd println()
2 It not necessary to make the variable space_in_a_car a floating point due the measurement being humans
 (which are non-divisible). The equation that the variable is used in (multiplication) will also not yield
  a decimal when integers / whole numbers are always used.
3 Floating point means that variable is stored as a decimal.
4 done above
5 '=' is called equals
6 '_' is an underscore
  
 




"""
