##import tkinter as tk
##
##root = tk.Tk()           # create the main window
##root.title("My First App")
##root.geometry("320x160") # width x height (optional)
##
##label = tk.Label(root, text="Hello, Tkinter!")
##label.pack(pady=10)
##
##root.mainloop()          # start the event loop

import tkinter as tk
root = tk.Tk()
root.title("my firt app")
root.geometry("320x160")

label = tk.Label(root, text = "hello, tkinter!")
label.pack(pady = 10)

root.mainloop()



##def interst_input():
##    annual_rate = float(input("enter annual rate of interst:"))
##    monly_payment = float(input("\n enter montly payment:"))
##    beg_balance = float(input("\n enter beg. of monthly balance:"))
##    return [annual_rate, monly_payment, beg_balance]
##
##def calculate_input(inputs):
##    paid_interest = inputs[0] * inputs[2] /100 /12
##    reduction = inputs[1] - paid_interest
##    end = inputs[2] - reduction
##    return [paid_interest, reduction, end]
##
##def output(inputs):
##    print(f"interst of this month: {inputs[0]:.2f}\n")
##    print(f"reduction of principle: {inputs[1]:.2f}\n")
##    print(f"end of this month: {inputs[2]:.2f}")
##    return
##
##def main():
##
##    output(calculate_input(interst_input()))
##    return 0
##    
##        
##main()



##def fahrenheit_to_celsius(f):
##    return (f-32)*5/9
##
##temp = int(input("temp = "))
##print(f"changed temp =  {fahrenheit_to_celsius(temp)}")


##temp = input()
##print("temp = " + str(fahrenheit_to_celsius(int(temp))))

##temp2 = 55
##print(fahrenheit_to_celsius(temp2))
