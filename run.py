from functions.cooking import *
from functions.processing import *

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