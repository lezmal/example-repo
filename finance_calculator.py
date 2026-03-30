import math
#explain / provide calculator options to user
print ('Investment - to calculate the amount you\'ll earn on your investment. \nbond - to calculate the amount you\'ll have to pay on home loan. \n ')

#ask user which calcultor option they want to use, allow any case input, convert input to lowercase
calculator_option = input('\nEnter either "Investment" or "bond" from the menu above to proceed :').lower()
if calculator_option == "investment" :
  #ask user for for relevent information for the necessary investment calculation
  print ("kindly provide the following information to proceed with your investment calculation : ")
  p = float (input("how much would you like to invest? : "))
  t = int (input("how many years do you wish to invest for? : "))
  i = float (input ("what is your prefered interest rate? :"))
#get user option on investment type and convert to preffered cases
  interest = input ("Would you prefer Simple or Compound interest? :").lower()
  r = i/100 #converted to percentage
  if interest == "simple" :
    total_amount = p*(1 + r*t)
    #print out answer using format method
    print("\nyour total investment after {0} years is : {1} H$".format(t,total_amount))
    
    #calculation for compound interest
  elif interest == "compound" : 
    total_amount = p*math.pow((1+r),t)
    print("\nyour Total investment after {0} years is : {1} H$".format(t,total_amount))
 #display appropriate error message for wrong user selection
  else :
    print ("incorrect selection, kindly select the investment option you want from the list above")

#bond repayment calculator
elif calculator_option == "bond" :
  #ask user for for relevent information for the necessary bond calculation
  print ("kindly provide the following information to proceed with your investment calculation : ")
  p= float(input("What is the present value of the bond? : "))
  ai = float(input("What is your prefered interest rate? : ")) #annual interest(ai)
  n = int(input("how many months will it take to repay your bond? :"))
  i = (ai/100)/12  #annual interest(ai) converted to percentage and devided by 12 months
  repayment = (i*p)/(1-(1+i)**(-n))
  print("\nyour monthly repayment is : " + str(repayment) + "H$")

  #display an appropriate error message for wrong user input 
else :
  print (' You have chosen an invalid option. Please Enter either "Investment" or "Bond" from the above menu to proceed :')

