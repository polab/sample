num = input("\n" + "Please enter check if it is an Armstrong number: ")
power = len(num)
tot = 0

if num.isnumeric() == False:
  print("\n" + "It is an invalid entry. Don't use non-numeric, float, or negative values!" + "\n")
else:
  for i in num:
    i = int(i)
    tot += i**power

  if int(num) == tot:
    print(f'{num} is an Armstrong number')
  elif int(num) != tot:
    print(f'{num} is not an Armstrong number')

