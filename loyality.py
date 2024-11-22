# Existing customer loyalty data
loyalty_points = {
    "Sajid": 120,
    "Roopesh": 85,
    "Koushik": 50,
    "Lakshmi": 64,
    "Sathvik": 12,
}

def main():
    # Input details
    name = input("Enter customer name: ")
    bill = int(input("Enter bill amount (in Rs.): "))
    coupon = input("Enter coupon code (if any): ")

    # Calculate loyalty points
    points_from_bill = bill // 100
    points_from_coupon = 20 if coupon == "123476" else 0
    total_earned_points = points_from_bill + points_from_coupon

    # Check if the customer is in the database
    prior_points = loyalty_points.get(name, 0)
    total_points = prior_points + total_earned_points

    # Calculate cashback and remaining points
    cashback = (total_points // 100) * 100
    remaining_points = total_points % 100

    # Display results
    print("\n--- Loyalty Points Summary ---")
    print(f"Customer: {name}")
    print(f"Points Earned Today: {total_earned_points}")
    print(f"Total Points: {total_points}")
    print(f"Cashback: Rs. {cashback}")
    print(f"Remaining Points: {remaining_points}")

    # Update database
    loyalty_points[name] = remaining_points

# Run the program
main()

