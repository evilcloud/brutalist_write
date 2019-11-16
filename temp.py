def solve(meal_cost, tip_percent, tax_percent):
    # totalCost = int(meal_cost + (meal_cost*(tip_percent/100)) + (meal_cost*(tax_percent/100)))
    tip_amount = meal_cost * (tip_percent / 100)
    tax_percent = meal_cost * (tax_percent / 100)
    totalCost = meal_cost + tip_amount + tax_percent
    
    print(round(totalCost))
    
solve(10.25, 17, 5)