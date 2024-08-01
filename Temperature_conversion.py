def my_function(temperature,unit1,unit2):
    if unit1=="celsius" and unit2=="fahrenheit":
        return(temperature *9/5)+32
    elif unit1=="fahrenheit" and unit2=="Celsius":
        return(temperature*9/5)-32
    elif unit1==unit2:
        return temperature
    else:
        print("Not valid")

temperature=input("Enter the temperature:")
unit1=input("Enter the unit in which you want to convert the temperature:")
unit2=input("Enter the unit of temperature:")
print(my_function(temperature,unit1,unit2))
    

