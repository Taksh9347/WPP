def is_valid_price(price):
    if price.count('.') > 1:  # float value cant hv more than one decimal points
        return False
    else :
        return True

dict = {}
while True:
    product = input("Enter the product name (or 'q' to quit): ").strip()
    if product.lower() == 'q':
        break
    if product in dict:
        print(f"Product '{product}' already exists with a price of {dict[product]}.")
    else:
        while True:
            price = input(f"Enter the price for '{product}': ").strip()
            if is_valid_price(price):
                price = float(price) 
                dict[product] = price
                break   
            else:
                print("Invalid price")
while True:
    find_prod = input("\nEnter Product name to check its price (or 'q' to quit): ").strip()
    if find_prod.lower() == 'q':
        print("END")
        break
    if find_prod in dict:
        print(f"Price of {find_prod} = {dict[find_prod]}.")
    else:
       print(f"'{find_prod}' is not in the dictionary.")