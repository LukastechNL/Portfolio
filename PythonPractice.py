A few graphs made for data visualization practice
-------------------------------------------------

GRAPH 1
-------
import matplotlib.pyplot as plt
import seaborn as sns


years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 1.08]
oranges = [0.5, 0.6, 0.34, 0.89, 0.63, 0.55, 0.98]

plt.plot( years, apples)
plt.plot(years, oranges)
plt.xlabel('Years')
plt.ylabel('Apples')
plt.title('Apples Production Over Years')
plt.legend(['apples'])
plt.show()


GRAPH 2
-------
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips_df = sns.load_dataset("tips")
print(tips_df)
sns.barplot(x="day", y="total_bill",hue = 'sex', data=tips_df)
plt.show()


GRAPH 3
-------
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

flo_df = sns.load_dataset('iris')
sns.pairplot(flo_df, hue='species')
plt.show()


GRAPH 4
-------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

Duration = [8, 6, 7, 8, 5, 9, 8]
Energy = [100, 70, 85, 100, 60, 95, 100]
Comfort = [100, 80, 90, 100, 70, 100, 100]

# Create a DataFrame
Sle_df = pd.DataFrame({'Duration': Duration, 'Energy': Energy, 'Comfort': Comfort})

# Calculate the correlation matrix
correlation_matrix = Sle_df.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('How Sleep Quality Can Be Affected')
plt.show()

# Open an interactive window for the plot
plt.show()

A minimal number guessing game
------------------------------
import random

number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
  print("You guessed correctly!")

while guess != number:
  if guess < number:
    print("Your guess was too low. Try again.")
    guess = int(input("Guess a number between 1 and 10: "))
  elif guess > number:
    print("Your guess was too high. Try again.")
    guess = int(input("Guess a number between 1 and 10: "))

A minimal calculator
--------------------
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  choice = input("Enter choice: ")

  if choice in ('1', '2', '3', '4'):
    try: 
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input, please enter a number.")
      continue
  elif choice not in('1', '2', '3', '4'):
      print(f"{choice} is not a valid input")
      continue

  if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))
  elif choice == '2':
        print(num1, '+' , num2, '=', subtract(num1, num2))
  elif choice == '3':
      print(num1, '*', num2, '=', multiply(num1, num2))
  elif choice == '4':
      if num2 == 0:
          print(f"{num2} is not a valid input")
          continue
      print(num1, '/', num2, '=', divide(num1, num2))

  next = input("Enter a new calculation? (yes/no): ")
  if next == "no":
      break

Another graph for comparing coorelations
----------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = [['Hours slept',	'Temp',	'Lighting',	'Blanket',	'How I woke up'],
['8',	'Normal',	'None',	'Light',	'Energized'],
['5',	'Normal',	'Dim',	'Heavy',	'Uncomfortable'],
['8',	'Cold',	'None',	'Heavy',	'Energized'],
['8',	'Hot',	'Bright',	'Light',	'Uncomfortable'],
['8',	'Hot',	'Dim',	'Light',	'Energized'],
['9',	'Hot',	'Dim',	'Light',	'Energized'],
['3',	'Normal',	'None',	'Light',	'Tired'],
['4',	'Normal',	'None',	'Heavy',	'Tired'],
['8',	'Cold',	'None',	'Light',	'Energized'],
['8',	'Cold',	'Dim',	'Heavy',	'Energized'],
['6',	'Normal',	'None',	'Light',	'Comfortable'],
['7',	'Normal',	'Dim',	'Light',	'Comfortable'],
['8',	'Hot',	'Dim',	'Heavy',	'Uncomfortable'],
['5',	'Hot',	'None',	'Light',	'Tired'],
['4',	'Hot',	'Bright',	'Heavy',	'Uncomfortable'],
['8',	'Normal',	'Bright',	'Light',	'Tired'],
['8',	'Cold',	'None',	'Heavy',	'Energized'],
['5',	'Cold',	'Dim',	'Heavy',	'Energized'],
['8',	'Normal',	'None',	'Light',	'Comfortable'],
['8',	'Hot',	'None',	'Heavy',	'Uncomfortable'],
['4',	'Hot',	'None',	'Light',	'Tired'],
['3',	'Cold',	'None',	'Heavy',	'Tired'],
['5',	'Normal',	'Bright',	'Heavy',	'Uncomfortable'],
['9',	'Normal',	'Dim',	'Heavy',	'Comfortable'],
['10',	'Normal',	'Bright',	'',	'Tired'],
['2',	'Normal',	'Dim',	'Heavy',	'Tired'],
['10',	'Hot',	'Dim',	'Heavy',	'Uncomfortable'],
['8',	'Normal',	'None',	'Light',	'Energized'],
['8',	'Normal',	'Bright',	'Light',	'Uncomfortable']]

df = pd.DataFrame(data)

print(df)

# hours_vs_woke = {}
# for row in data[1:]:
#   hours = int(row[0])  # Convert hours to integer
#   woke = row[4]
#   if woke in hours_vs_woke:
#     hours_vs_woke[woke].append(hours)
#   else:
#     hours_vs_woke[woke] = [hours]
# 
# print("\nTotal time slept vs Wake up notes:")
# for woke, hours in hours_vs_woke.items():
#     average_hours = sum(hours) / len(hours)
#     print(f"Wake up notes: {woke}, Average time slept: {average_hours:.2f} hours")


# Now let's plot a bargraph of average sleep time vs average wake up time
#This is purely to understand how many hours ia a good sleep for me

# plt.bar(
#     list(hours_vs_woke.keys()), 
#     [sum(hours) / len(hours) for hours in hours_vs_woke.values()]
# )
# 
# plt.xlabel("Wake up Notes")
# 
# plt.ylabel("Average Total Sleep Time (hours)")
# 
# plt.title("Average Total Sleep Time vs Wake up Notes")
# 
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# 
# plt.tight_layout()  # Adjust layout to prevent labels from overlapping
# 
# plt.show()

hours_vs_lighting = {}
for row in data[1:]:
  hours = int(row[0])  # Convert hours to integer
  lighting = row[2]
  if lighting in hours_vs_lighting:
    hours_vs_lighting[lighting].append(hours)
  else:
    hours_vs_lighting[lighting] = [hours]

print("\nTotal time slept vs Lighting:")
for lighting, hours in hours_vs_lighting.items():
    average_hours = sum(hours) / len(hours)
    print(f"Lighting: {lighting}, Average time slept: {average_hours:.2f} hours")

plt.figure(figsize=(8, 6))  # Adjust figure size if needed
plt.boxplot([hours_vs_lighting[lighting] for lighting in hours_vs_lighting], labels=hours_vs_lighting.keys(), patch_artist=True,
            boxprops= (facecolor='lightblue', edgecolor='blue'),
            capprops=(color='blue'),
            whiskerprops=(color='blue'),
            flierprops=(marker='o', markerfacecolor='blue', markersize=8))
plt.xlabel("Lighting")
plt.ylabel("Total Sleep Time (hours)")
plt.title("Total Sleep Time vs Lighting (Boxplot)")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.tight_layout()
plt.show()

To change hours vs lighting to hours vs woke change lines 40 to 73 to non-comments and make lines 75 to 100 comments