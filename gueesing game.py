import random
secret_number = random.randint(1, 10)
guess=int(input("enter number"))
attempts=3
print("welcome to the number gussing game! ")
print("iam thinking of a number between 1 and 10")
print(f"you have{attempts} attempts to guess it correctly,\n")
while True:
  guess=int(input("enter number"))
  if guess== secret_number:
    print("guess is correct")
    continue
  elif guess> secret_number:
   print("guess number is high")
  else:
   print("guess number is low")

number=int(input("enter number to get multiplication table"))
print(f"\nmultiplication table for {nnumber}")
for i in range(1,11)
    result=number*i
    print(f"{number}*{i}={result}")
def calculate_bmi(weight,height):
  """calculate and returns the BMI"""
  BMI=weight/(height**2)
  return BMI
  user_ weight=float(input("enter weight in kg"))
  user_height=float(input("enter height in meters"))
  calcualted bmi=calculate_bmi(user_weight,user_hight)
print("your BMI is :{claculated_bmi:2f}")

