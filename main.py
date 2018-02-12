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


# COOKING
# COOKING

def aloe_yogurt():
    q_aloe_yogurt = int(input("\nHow much aloe yogurt are you going to make?"))
    p_aloe = int(input("What is the price of 1 aloe? (0 if using nodes"))
    p_aloe = p_aloe * 5
    p_milk = int(input("What is the price of 1 milk? (0 if gathering)"))
    p_milk = p_milk * 2
    p_aloe_yogurt = int(input("What is the selling price of aloe yogurt?"))
    P_3_LEV_AGENTS = 60
    P_3_SUGAR = 60
    #expenses for 1 aloe yogurt
    expenses = p_aloe + p_milk + P_3_LEV_AGENTS + P_3_SUGAR
    profit = p_aloe_yogurt - expenses
    print("\nThe minimum amount of money you can make is: " + str(profit))

def beer():
    q_beer = int(input("\nHow many grains do you have?"))
    q_beer = q_beer / 5
    q_beer = math.floor(q_beer)
    p_grain = int(input("What is the price of 1 of the type of grain you are going to use? (0 if using node)"))
    p_beer = int(input("What is the selling price of beer?"))
    p_grain = p_grain * 5
    P_1_SUGAR = 20
    P_2_LEV_AGENTS = 40
    P_6_MIN_WATER = 180
    #expenses for 1 beer
    expenses = p_grain + P_1_SUGAR + P_2_LEV_AGENTS + P_6_MIN_WATER
    profit = q_beer * (p_beer - expenses)
    print("\nThe minimum amount of money you can make is: " + str(profit))

def fruit_wine():
    print("\nFruit wine requires you to make essence of liquor and exotic herbal wine,")
    int(input("(Press 1 if making previous ingredients. Press 2 if purchasing previous ingredients)."))

def milk_tea():
    x = int(input("\nDo you want to calculate the profitability if you make tea with fine scent then "
                  "turn that into milk tea? (Press 1 for yes (tea w fine scent - ingredient based), "
                  "\n2 (tea w fine scent - quantity based), and 0 for no)"))
    if x == 0:
        q_m_tea = int(input(("How many tea with fine scent are you going to use?")))
        q_m_tea = q_m_tea / 2
        q_m_tea = math.floor(q_m_tea)
        p_tea = int(input("What is the price of tea with fine scent? (0 if made yourself)"))
        p_tea = p_tea * 2
        p_c_honey = int(input("What is the price of 1 cooking honey/wild beehive? (0 if using node/gathering)"))
        p_c_honey = p_c_honey * 3
        p_milk = int(input("What is the price of 1 milk? (0 if gathering)"))
        p_milk = p_milk * 3
        make_flour = int(input("Are you making your own flour? (Press 1 for yes and 0 for no)"))
        if make_flour == 1:
            p_flour = int(input("What is the price of 1 grain? (0 if using node/gathering)"))
        elif make_flour == 0:
            p_flour = ("What is the price of 1 flour?")
        p_flour = p_flour * 2
        p_m_tea = int(input("What is the selling price of 1 milk tea?"))
        # expenses for 1 milk tea
        expenses = p_tea + p_c_honey + p_milk + p_flour
        profit = q_m_tea * (p_m_tea - expenses)
    elif x == 1:
        # tea with fine scent based off of quantity of flowers/fruits
        q_tea = int(input("How many flowers/fruit do you have? (write the amount of the one you have the least of)"))
        q_tea = q_tea / 4
        q_tea = math.floor(q_tea)
        p_flower = int(input("What is the price of 1 flower you are going to use? (0 if gathering)"))
        p_flower = p_flower * 4
        p_fruit = int(input("What is the price of 1 fruit you are going to use? (0 if using node)"))
        p_fruit = p_fruit * 4
        p_c_honey = int(input("What is the price of 1 cooking honey? (0 if using node)"))
        p_c_honey = p_c_honey * 3
        p_tea = int(input("What is the selling price of 1 tea with fine scent?"))
        P_7_MIN_WATER = 210
        # expenses per 1 tea
        expenses = p_flower + p_fruit + p_c_honey + P_7_MIN_WATER
        profit = q_tea * (p_tea - expenses)
        print("\nThe minimum amount of money you can make from tea with fine scent alone is: " + str(profit))
        # MILK TEA STARTS HERE
        # MILK TEA STARTS HERE
        q_m_tea = q_tea
        q_m_tea = q_m_tea / 2
        q_m_tea = math.floor(q_m_tea)
        p_tea = int(input("What is the price of tea with fine scent? (0 if made yourself)"))
        p_tea = p_tea * 2
        p_c_honey = int(input("What is the price of 1 cooking honey/wild beehive? (0 if using node/gathering)"))
        p_c_honey = p_c_honey * 3
        p_milk = int(input("What is the price of 1 milk? (0 if gathering)"))
        p_milk = p_milk * 3
        make_flour = int(input("Are you making your own flour? (Press 1 for yes and 0 for no)"))
        if make_flour == 1:
            p_flour = int(input("What is the price of 1 grain? (0 if using node/gathering)"))
        elif make_flour == 0:
            p_flour = ("What is the price of 1 flour?")
        p_flour = p_flour * 2
        p_m_tea = int(input("What is the selling price of 1 milk tea?"))
        # expenses for 1 milk tea
        expenses = p_tea + p_c_honey + p_milk + p_flour
        profit = q_m_tea * (p_m_tea - expenses)
        print("\nThe minimum amount of money you can make from milk tea is: " + str(profit))
    elif x == 2:
        pass



def tea_with_fine_scent_ingredients():
    #tea with fine scent based off of quantity of flowers/fruits
    q_tea = int(input("How many flowers/fruit do you have? (write the amount of the one you have the least of)"))
    q_tea = q_tea / 4
    q_tea = math.floor(q_tea)
    p_flower = int(input("What is the price of 1 flower you are going to use? (0 if gathering)"))
    p_flower = p_flower * 4
    p_fruit = int(input("What is the price of 1 fruit you are going to use? (0 if using node)"))
    p_fruit = p_fruit * 4
    p_c_honey = int(input("What is the price of 1 cooking honey? (0 if using node)"))
    p_c_honey = p_c_honey * 3
    p_tea = int(input("What is the selling price of 1 tea with fine scent?"))
    P_7_MIN_WATER = 210
    #expenses per 1 tea
    expenses = p_flower + p_fruit + p_c_honey + P_7_MIN_WATER
    profit = q_tea * (p_tea - expenses)
    print("\nThe minimum amount of money you can make is: " + str(profit))


def tea_with_fine_scent_product():
    q_tea = int(input("How many tea with fine scent would you like to make?"))
    p_flower = int(input("What is the price of 1 flower you are going to use? (0 if gathering)"))
    p_flower = p_flower * 4
    p_fruit = int(input("What is the price of 1 fruit you are going to use? (0 if using node)"))
    p_fruit = p_fruit * 4
    p_c_honey = int(input("What is the price of 1 cooking honey? (0 if using node)"))
    p_c_honey = p_c_honey * 3
    p_tea = int(input("What is the selling price of 1 tea with fine scent?"))
    P_7_MIN_WATER = 210
    #expenses per 1 tea
    expenses = p_flower + p_fruit + p_c_honey + P_7_MIN_WATER
    profit = q_tea * (p_tea - expenses)
    print("\nThe minimum amount of money you can make is: " + str(profit))


print("BDO Profit Calculator")
print("These profits are not deducting market tax, and are not considering higher skill levels or critical hits "
      "(i.e. Cold Draft Beer).\n")
print("What are you going to do?\n1. Process\n2. Cook\n")
select_task = int(input("(Press 1 or 2)..."))

if select_task == 1:
    print("What would you like to process?\n1. Cotton\n2. Flax")
    task = int(input("(Press 1 or 2)..."))
    if task == 1:
        cotton_fabric()
    elif task == 2:
        flax_fabric()
    else:
        int(input("Please press 1 or 2..."))
elif select_task == 2:
    print("What would you like to cook?")
    task = int(input("1. Aloe Yogurt\n2. Beer (grain based)\n3. Fruit Wine\n4. Tea with Fine Scent (quantity - "
                     "fruit/flower based)\n5. Tea with Fine Scent (quantity - product based)\n"
                     "6. Milk Tea"))
    if task == 1:
        aloe_yogurt()
    elif task == 2:
        beer()
    elif task == 3:
        fruit_wine()
    elif task == 4:
        tea_with_fine_scent_ingredients()
    elif task == 5:
        tea_with_fine_scent_product()
    elif task == 6:
        milk_tea()