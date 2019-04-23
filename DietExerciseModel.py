# Thomas Martinson
# 818755425
# CS558
# Madachy
# Diet and Exercise Model

# import numpy as np
import matplotlib.pyplot as plot

timepoints = []
xpoints = []
ypoints = []


rate = 0.5


dt = 1 # timestep

# initialization
time = 0
x = 10000

dx = 0


age = input("Please enter your age:")
gender = input("Please enter your gender (M,F):")
height = input("Please enter your height (inches):")
weight0 = input("Please enter your weight (lbs):")

exerciseLevel = input("Please enter the level of exercise you would like to model (1-5)\n1. sedentary (little or no exercise)\n2. lightly active (light exercise/sports 1-3 days/week)\n3. moderately active (moderate exercise/sports 3-5 days/week)\n4. very active (hard exercise/sports 6-7 days a week)\n5. extra active (very hard exercise/sports & physical job or 2x training)\n:")

deficitPercent = input("Please enter the % caloric deficit you would like to model (1-4)\n1. 5% below maintenance level\n2. 10% below maintenance level\n3. 15% below maintenance level\n4. 20% below maintenance level \n:")

totalTime = 30 * int(input("How many months would you like to model this diet for?"))

# print output header and starting values
print ("  Time  Weight   Change")
print ("%6.2f  %6.2f%6.2f " % (time, x, dx))


# integration time loop
while time < totalTime: # run until a troop is eliminated
  # compute derivatives
  dx = -rate  # x attrition rate
  
  # increment time
  time += dt # time = time+ dt
  # update troop state variables
  x += dx # x = x + dx*dt
  if(x<0):
    x = 0
  
  
  print ("%6.2f  %6.2f  %6.2f " % (time, x, dx*dt))
  xpoints.append(x)
  timepoints.append(time)
  
 
plot.xlabel('Time (days)')
plot.ylabel('Weight (lb)')
plot.plot(timepoints,xpoints)
plot.legend(loc='upper center')
plot.show()
plot.savefig('output.png')





