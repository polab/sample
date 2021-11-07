
age = False 
chronic = False
immune = False

#age =  input("Are you a cigarette addict older than 75 years old? ")
#chronic = input("Do you have a severe chronic disease? ")
#immune =  input("Is your immune system too weak? ")

age = bool(age)
chronic = bool(chronic)
immune = bool(immune)


#print(type(age))
#print(type(chronic))
#print(type(immune))

if (age == True or chronic == True or immune == True):
  print("\n", "Covid risk is True")
elif (age == False and chronic == False and immune == False):
  print("Covid risk is False")
