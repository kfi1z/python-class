
current_users=["sackeyfio_joshua","Benzo_11z","valentino_marley","Bobe_owusu","kofi_adom"]
new_users=["maison_jay","ella_mei","benzo_11z","bobe_owusu","atsu_wavy"]

current_users=[user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is unavailable,you need to enter a different username")
    else:
        print(f"{new_user} is available")



for number in range(1,101):
     if number %3==0 and number%5==0:
        print("fizzbuzz")  
     elif number % 5==0:
        print("buzz")
     elif number & 3==0:
        print("fizz")   
     else:
        print(number)        
