# if statements are conditional. 
# inside the if statement only executes if the condition 
# evaluates to True. 
# indention is critical. 
# all statements inside the if must have same indention. 
pressure = 52

if pressure > 50:
  print("WARNING! High Pressure")
  print("I like cashews.")

# after an if, you can also have elif and/or else statements
if pressure > 50:
  print("WARNING! High Pressure")
elif(pressure > 30 and pressure <= 50):   # short for else if 
  print("Normal Pressure")
  print("I like macademias.")
# else will execute only when if and elif statements all evaluate to False. 
else:
  print("Low Pressure.")
