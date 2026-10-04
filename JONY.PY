customer_age = int(input("Enter customer age: "))
country = input("Enter customer country: ").strip().lower()
cart_total_in_ksh = float(input("Enter cart total in Ksh: "))
membership_tier = input("Enter membership tier (regular, premium, vip): ").strip().lower()
shipping_cost = 0

if customer_age >= 18:
    print("Customer is eligible for purchase.")
else:
    print("Customer is not eligible for purchase.")
    raise SystemExit

if country in {"kenya", "uganda", "tanzania"}:
    print("Customer is eligible for delivery.")
else:
    print("Customer is not eligible for delivery.")

if membership_tier == "vip":
    print(f"VIP member: free shipping. Total cost: {cart_total_in_ksh}")
elif membership_tier == "premium":
    shipping_cost = 0 if cart_total_in_ksh >= 2000 else 200
    print(f"Premium member: shipping cost: {shipping_cost}. Total cost: {cart_total_in_ksh + shipping_cost}")
elif membership_tier == "regular":
    shipping_cost = 300
    discount = 0.1 * cart_total_in_ksh if cart_total_in_ksh >= 5000 else 0
    total_cost = cart_total_in_ksh - discount + shipping_cost
    print(f"Regular member: discount: {discount}. shipping cost: {shipping_cost}. total cost: {total_cost}")
else:
    print("Invalid membership tier. Please enter a valid tier (regular, premium, vip).")
         
        
