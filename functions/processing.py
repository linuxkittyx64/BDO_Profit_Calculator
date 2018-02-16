import math

# PROCESSING
# PROCESSING

def flax_fabric():
    p_flax = float(input("\nWhat is the price of flax? (0 if using nodes)"))
    q_flax = float(input("How much flax are you going to process?"))
    p_flax_fabric = float(input("What is the selling price of flax fabric?"))
    q_flax = q_flax / 5
    q_flax_thread = math.floor(q_flax)
    q_flax_fabric = q_flax_thread / 10
    q_flax_fabric = math.floor(q_flax_fabric)

    # expenses of all flax bought
    expenses = q_flax * p_flax
    profit = p_flax_fabric * math.floor(q_flax_fabric) - expenses
    print("\nThe minimum amount of money you can make is: " + str(profit))

def cotton_fabric():
    p_cotton = float(input("\nWhat is the price of cotton? (0 if using nodes)"))
    q_cotton = float(input("How much cotton are you going to process?"))
    p_cotton_fabric = float(input("What is the selling price of cotton fabric?"))
    q_cotton = q_cotton / 5
    q_cotton_yarn = math.floor(q_cotton)
    q_cotton_fabric = q_cotton_yarn / 10
    q_cotton_fabric = math.floor(q_cotton_fabric)

    # expenses of all cotton bought
    expenses = q_cotton * p_cotton
    profit = p_cotton_fabric * q_cotton_fabric - expenses
    print("\nThe minimum amount of money you can make is: " + str(profit))