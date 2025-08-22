print("Welcome to the Python Coffee Shop!")

customer_willing = "Yes"
while customer_willing == "Yes":
    customer_willing = input("would you like to order(Yes / No)")
    if customer_willing == "Yes":
        customer_name = input("What is your name? ")
        print("Hello, " + customer_name + "! Let's order some coffee.")
                                 
        price_coffee = 3.50
        price_latte = 4.00
        price_mocha = 5.00
        valid_choice = ("coffee","latte","mocha")
         
        print("Coffee: $" + str(price_coffee))
        print("Latte: $" + str(price_latte))
        print("Mocha: $" + str(price_mocha))
         
        choice = input("What would you like to order? (coffee/latte/mocha): ").lower()
        while choice not in valid_choice:
             print("Sorry, we do not have that,please try again!\n")
             choice = input("What would you like to order? (coffee/latte/mocha): ").lower()

        if choice == "coffee":
             cost = price_coffee
        elif choice == "latte":
             cost = price_latte
        else:
            #choice == "mocha":
            cost = price_mocha
         
        quantity = int(input("How many cups would you like? "))
        student_identity = input("Are you a student(Yes / No)?")
        if student_identity == "Yes":
             total_cost = cost * quantity * 0.9
             print(" you get student discount: 10% off")
        else:
             total_cost = cost * quantity

        if quantity > 1:
             print("You get a discount of $1.00!")
             total_cost -= 1.00
         
        print("Your total is: $" + str(total_cost))
        print("Thank you, " + customer_name + "! Please come again.\n")
    else:
        print("Thank you\n")

                        
