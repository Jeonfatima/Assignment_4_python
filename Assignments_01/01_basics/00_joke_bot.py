def main():
    Joke = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    sorry = "Sorry I only tell jokes"
    prompt ="What do you want?"
   
    
    while True:  
        user_input = input(f"{prompt}").strip().lower()
        if user_input == "joke":
            print(Joke)
        elif user_input == "nothing":
            break
        else:
            print(sorry)

if __name__=="__main__":
    main()