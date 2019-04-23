# Thomas Martinson
# 818755425
# CS558
# Madachy
# Diet and Exercise Model

# import numpy as np
import matplotlib.pyplot as plot

timepoints = []
wpoints = []


rate = 0.5


dt = 1 # timestep

# initialization
time = 0
weight = 150

dw = 0


age = input("Please enter your age:")
gender = input("Please enter your gender (M,F):")
height = input("Please enter your height (inches):")
weight0 = input("Please enter your weight (lbs):")

exerciseLevel = input("Please enter the level of exercise you would like to model (1-5)\n1. sedentary (little or no exercise)\n2. lightly active (light exercise/sports 1-3 days/week)\n3. moderately active (moderate exercise/sports 3-5 days/week)\n4. very active (hard exercise/sports 6-7 days a week)\n5. extra active (very hard exercise/sports & physical job or 2x training)\n:")

deficitPercent = input("Please enter the % caloric deficit you would like to model (1-4)\n1. 5% below maintenance level\n2. 10% below maintenance level\n3. 15% below maintenance level\n4. 20% below maintenance level \n:")

totalTime = 30 * int(input("How many months would you like to model this diet for?"))

# print output header and starting values
print ("  Time  Weight   Change")
print ("%6.2f  %6.2f%6.2f " % (time, weight, dw))


# integration time loop
while time < totalTime: # run until a troop is eliminated
  # compute derivatives
  dw = -rate  # x attrition rate
  
  # increment time
  time += dt # time = time+ dt
  # update troop state variables
  weight += dw # calculate new weight
  
  
  if(weight<0): # edge case to prevent errors
    weight = 0
    break # stop looping
  
  
  print ("%6.2f  %6.2f  %6.2f " % (time, weight, dw))
  wpoints.append(weight)
  timepoints.append(time)
  
 
plot.xlabel('Time (days)')
plot.ylabel('Weight (lb)')
plot.plot(timepoints,wpoints)
plot.legend(loc='upper center')
plot.show()
plot.savefig('output.png')





