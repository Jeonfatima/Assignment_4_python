import math
def main():
    MERCURY_GRAVITY = 0.376
    VENUS_GRAVITY = 0.889
    MARS_GRAVITY = 0.378
    JUPITER_GRAVITY = 2.36
    SATURN_GRAVITY = 1.081
    URANUS_GRAVITY = 0.815
    NEPTUNE_GRAVITY = 1.14
    EARTH_GRAVITY = 1.0

   # prompt the user to imput weigth and planet

    earth_weight = float(input("Enter you weight on earth : "))
    print("mercury, venus, mars, jupiter, saturn, uranus, neptune, earth")
    planet = input("Which planet do you want to convert you weight into from above ?").strip().lower()


    # determine gravity constant based on user input
    if planet == "mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "neptune":
        gravity_constant = NEPTUNE_GRAVITY
    elif planet == "earth":
        gravity_constant = EARTH_GRAVITY
    else:
        print("Incorrect planet input")
    

    #calculate equivalent weight
    planetray_weight = earth_weight * gravity_constant
    rounded_answer = round(planetray_weight,2)

    #Didplay calculated and rounded answer
    print(f"Your equivalant weight on {planet} is {rounded_answer}kg")

if __name__=="__main__":
    main()
