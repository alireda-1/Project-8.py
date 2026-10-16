main_name="ali"
main_password="TheBesT"
name=input("Please inter your name: \n")
password=input("Please inter the password :\n")
if name.lower()==main_name and password==main_password:
  print("welcome back")
elif name==main_name and password!=main_password:
  print("Incorrect password!")
elif name!= main_name and password==main_password:
  print(" Incorrect name !")
else:
  print("Soory, try again")