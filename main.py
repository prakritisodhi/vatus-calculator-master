# Changelog:
# Abdul Hadi - 20/09/17 - Added the distance function
# Abdul Hadi - 28/09/17 - Added the initial velocity, final velocity, acceleration and time function
# Abdul Hadi - 29/09/17 - Added a basic UI
# Abdul Hadi - 02/10/17 - Added rounding function


def distance_function():
    print("This will work out the distance for linear motion\n")
    null_value = input("What SUVAT letter do you not have?\nU, V, A, T\n")
    if null_value == "U":
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value for time?\n"))
        distance = ((v * t) - (0.5 * ((a * t) ** 2)))
        if distance < 0:
            distance = -distance
    elif null_value == "V":
        u = float(input("What is the value of the initial velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value of the time?\n"))
        distance = ((u * t) + (0.5 * (a * (t ** 2))))
        if distance < 0:
            distance = -distance
    elif null_value == "A":
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        t = float(input("What is the value of the time?\n"))
        distance = ((0.5 * (u + v)) * t)
        if distance < 0:
            distance = -distance
    elif null_value == "T":
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        distance = ((v ** 2) - (u ** 2) / (2 * a))
        if distance < 0:
            distance = -distance
    dec_place = int(input("How many decimal places do you want your answer too?\n"))
    distance = round(distance, dec_place) 
    print("The value for the distance , s ,  is:", (distance), "m\n")

def initial_velocity_function():
    print("This will work out the initial velocity for linear motion\n")
    null_value = input("What SUVAT letter do you not have?\nS, V, A, T\n")
    if null_value == "S":
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value for time?\n"))
        initial_velocity = (v - (a * t))
    elif null_value == "V":
        s = float(input("What is the value of the distance?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value of the time?\n"))
        initial_velocity = (s - (0.5 * a * t))
    elif null_value == "A":
        s = float(input("What is the value of the distance?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        t = float(input("What is the value of the time?\n"))
        initial_velocity = (((2 * s) / (t)) - v)
    elif null_value == "T":
        s = float(input("What is the value of the distance?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        initial_velocity = (((v ** 2) - (2 * a * s)) ** 0.5)
    dec_place = int(input("How many decimal places do you want your answer too?\n"))
    initial_velocity = round(initial_velocity, dec_place) 
    print("The value for the initial velocity , u , is:", (initial_velocity), "m/s\n")

def final_velocity_function():
    print("This will work out the final velocity for linear motion\n")
    null_value = input("What SUVAT letter do you not have?\nS, U, A, T\n")
    if null_value == "S":
        u = float(input("What is the value of the initial velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value for time?\n"))
        final_velocity = u + (a * t)
    elif null_value == "U":
        s = float(input("What is the value of the distance?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        t = float(input("What is the value of the time?\n"))
        final_velocity = (s - (0.5 * a * t))
    elif null_value == "A":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        t = float(input("What is the value of the time?\n"))
        final_velocity = (((2 * s) / (t)) - u)
    elif null_value == "T":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        final_velocity = (((u ** 2) + (2 * a * s)) ** 0.5)
    dec_place = int(input("How many decimal places do you want your answer too?\n"))
    fianl_velocity = round(final_velocity, dec_place) 
    print("The value for the final velocity , v ,  is:", (final_velocity), "m/s\n")

def acceleration_function():
    print("This will work out the acceleration for linear motion\n")
    null_value = input("What SUVAT letter do you not have?\nS, U, V, T\n")
    if null_value == "S":
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        t = float(input("What is the value for time?\n"))
        acceleration = ((v)-(u/t))
    elif null_value == "U":
        s = float(input("What is the value of the distance?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        t = float(input("What is the value of the time?\n"))
        acceleration = (((2*(s-(v*t)))/(t**2)))
    elif null_value == "V":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        t = float(input("What is the value of the time?\n"))
        acceleration = (((2*(s-(u*t)))/(t**2)))
    elif null_value == "T":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        acceleration = (((v**2)-(u**2)/(2*s)))
    dec_place = int(input("How many decimal places do you want your answer too?\n"))
    acceleration = round(acceleration, dec_place) 
    print("The value for the acceleration , a , is:", (acceleration), "m/s^2\n")

def time_function():
    print("This will work out the time for linear motion\n")
    null_value = input("What SUVAT letter do you not have?\nS, U, V, A\n")
    if null_value == "S":
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value for acceleration?\n"))
        time = ((v)-(u/a))
    elif null_value == "U":
        s = float(input("What is the value of the distance?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        time = ((((v**2)-(2*a*s)+v))/a)
    elif null_value == "V":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        a = float(input("What is the value of the acceleration?\n"))
        time = ((((u**2)+(2*a*s)-u))/a)
    elif null_value == "A":
        s = float(input("What is the value of the distance?\n"))
        u = float(input("What is the value of the initial velocity?\n"))
        v = float(input("What is the value of the final velocity?\n"))
        time = ((2*s)/(u+v))
    dec_place = int(input("How many decimal places do you want your answer too?\n"))
    time = round(time, dec_place) 
    print("The value for the time , t , is:", (time), "s\n")

user_choice = int(input("Welcome to the VATUS calculator\nWhat value do you want to calculate?\n1 = Distance\n2 = Initial Velocity\n3 = Final Velocity\n4 = Acceleration\n5 = Time\nPlease TYPE the appropriate number\n"))
user_continue = "YES"

while user_continue != "NO":
    if user_choice == 1:
        distance_function()
        user_continue = input("Do you want to do another calculation?\nTYPE YES to continue or NO to exit\n")
    if user_choice == 2:
        initial_velocity_function()
        user_continue = input("Do you want to do another calculation?\nTYPE YES to continue or NO to exit\n")
    if user_choice == 3:
        final_velocity_function()
        user_continue = input("Do you want to do another calculation?\nTYPE YES to continue or NO to exit\n")
    if user_choice == 4:
        acceleration_function()
        user_continue = input("Do you want to do another calculation?\nTYPE YES to continue or NO to exit\n")
    if user_choice == 5:
        time_function()
        user_continue = input("Do you want to do another calculation?\nTYPE YES to continue or NO to exit\n")

print("Thank you for using the VATUS calculator")
