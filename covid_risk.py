age =  input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune =  input("Is your immune system too weak? ")


if (age == "True" or chronic == "True" or immune == "True"):
  print("\n", "Covid risk is True", "\n")
elif (age == "False" and chronic == "False" and immune == "False"):
  print("\n", "Covid risk is False", "\n")
