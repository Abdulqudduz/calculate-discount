def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The price remains: ${original_price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
