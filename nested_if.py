whether = input("Enter the whether: ")
time_of_day = input("Enter the time: ")
if whether == "sunny":
    if time_of_day == "day":
       print("you can play with your car toy.")
    else:
       print("its night. time to sleep.")
elif whether == "rainy":
   print("you can play with your boat toy.")
elif whether == "snowy"and time_of_day == "night":
   print("you can play with me.")
else:
   print("you can play with your snow man.")