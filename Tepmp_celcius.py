print("1.Celsius to Farenheit")
print("2.fareneit to celcius")
n=input("enter your choice")
if(n==1):
c=float(input("enter the temperature in celcius"))
f=9/5*c+32
print("TEMPERATURE in Farenheit is",round(f,2))
elif(n==2):
f=float(input("enter the temperature in farenheit"))
c=(f-32)*5/9
print("temperature in celcius is",round(c,2))
else
print("WRONG CHoice")



