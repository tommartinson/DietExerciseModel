# Thomas Martinson
# 818755425
# CS558
# Madachy
# Diet and Exercise Model

# import numpy as np
import matplotlib.pyplot as plot

timepoints = []
wpoints = []

dt = 1 # timestep

# initialization
time = 0
dw = 0


age = float(input("Please enter your age:"))
gender = input("Please enter your gender (m,f):")
height = float(input("Please enter your height (inches):"))
weight = float(input("Please enter your weight (lbs):"))

exerciseLevel = int(input("\nPlease enter the level of exercise you would like to model (1-5)\n1. sedentary (little or no exercise)\n2. lightly active (light exercise/sports 1-3 days/week)\n3. moderately active (moderate exercise/sports 3-5 days/week)\n4. very active (hard exercise/sports 6-7 days a week)\n5. extra active (very hard exercise/sports & physical job or 2x training)\n:"))

deficitPercent = float(input("Please enter the % caloric deficit you would like to model:"))

totalTime = 30 * int(input("Please enter how many months you would like to model this diet for:"))


# Basal Metabolic Rate Calculation
# Men: BMR = 66 + (6.23 x weight in pounds) + (12.7 x height in inches) - (6.8 x age in years)
# Women: BMR = 655 + (4.35 x weight in pounds) + (4.7 x height in inches) - (4.7 x age in years)

BMR = 0
if (gender == 'm'):
    BMR = 66 + (6.23*weight) + (12.7*height) - (6.8*age)
else:
    BMR = 655 + (4.35*weight) + (4.7*height) - (4.7*age)
    
print("\n\nYour Basal Metabolic Rate (BMR) is:",int(BMR),"calories")

# Calculate BMR and Exercise Total
if (exerciseLevel == 1):
    BMR = BMR*1.2
elif(exerciseLevel == 2):
    BMR = BMR*1.375
elif(exerciseLevel == 3):
    BMR = BMR*1.55
elif(exerciseLevel == 4):
    BMR = BMR*1.725
else:
    BMR = BMR*1.9

print("Your BMR + calories burned from exercise is:",int(BMR),"calories" )
print("This is the amount of calories you should be eating each day to stay at your same weight.")


# Caloric Deficit Calculations

deficit = deficitPercent/100
print("Eating at a",deficitPercent,"% caloric deficit would mean eating",int(BMR*deficit),"less calories per day.")
print("Therefore, you would be eating,",(int)(BMR-BMR*deficit),"calories per day.")
print("This is what your change in weight would look like over time.")

# Calculating actual weight change
# 3500 calories = 1 lb of fat
netCalsLost = BMR*deficit
netWeightLost = netCalsLost/3500

# print output header and starting values
print ("   \nTime   Weight   Change(lb) Change(cals)")
print ("%6.2f  %6.2f   %6.3f       %6.2f" % (time, weight, dw, 0.00))


# time loop
while time < totalTime: # run for alloted time 
    # total caloric deficit = amount of calories taken in through food and 
    # subtract the amount of calories burned from working out and the amount 
    # of calories burned from the RMR.
    # caloric deficit = food - (workoutCals + BMRCals)
    # 3500 calories = 1 lb of fat
    
    # compute derivatives
  #--------------------------------------------------
  if (gender == 'm'):
    BMR = 66 + (6.23*weight) + (12.7*height) - (6.8*age)
  else:
    BMR = 655 + (4.35*weight) + (4.7*height) - (4.7*age)
  

  if (exerciseLevel == 1):
    BMR = BMR*1.2
  elif(exerciseLevel == 2):
    BMR = BMR*1.375
  elif(exerciseLevel == 3):
    BMR = BMR*1.55
  elif(exerciseLevel == 4):
    BMR = BMR*1.725
  else:
    BMR = BMR*1.9
  netCalsLost = BMR*deficit
  netWeightLost = netCalsLost/3500
  #-----------------------------------------------------
  # increment time
  time += dt # time = time+ dt
  # update troop state variables
  dw = -netWeightLost  # x attrition rate
  weight += dw # calculate new weight
  
  
  if(weight<0): # edge case to prevent errors
    weight = 0
    break # stop looping
  
  
  print ("%6.2f  %6.2f   %6.3f      %6.2f" % (time, weight, dw, -netCalsLost))
  wpoints.append(weight)
  timepoints.append(time)
  
print("\nA healthy amount of week to lose per week is about 1-2 pounds.")
print("According to this model, you would lose about%6.2f lbs per week." %(dw*-7))


plot.xlabel('Time (days)')
plot.ylabel('Weight (lb)')
plot.plot(timepoints,wpoints)
plot.show()
plot.savefig('output.png')
