import streamlit as st

st.title("Online Food Delivery System")
st.write("23CS028 - SHAURYA JUNEJA")

menu = {
    "Burger": (150, "Fast Food"),
    "Pizza": (300, "Fast Food"),
    "Pasta": (250, "Italian"),
    "Ice Cream": (100, "Dessert"),
    "Salad": (120, "Healthy"),
}

orders = []
unique_customers = set()

# Display the item menu
def display_menu():
    st.subheader("Menu:")
    for item, (price, category) in menu.items():
        st.write(f"{item}: Rs. {price} ({category})")

# Placing an order
def place_order():
    display_menu()
    customer_name = st.text_input("Enter your name:")

    if customer_name:
        unique_customers.add(customer_name)

    item_list = []
    total_bill = 0
    item = st.text_input("Enter the item you want to order (or 'done' to finish):")

    while item.lower() != 'done':
        if item in menu:
            item_list.append(item)
            total_bill += menu[item][0]
            item = st.text_input("Enter the item you want to order (or 'done' to finish):")  # Repeat item input
        else:
            st.error("Item not available. Please choose from the menu.")
            item = st.text_input("Enter the item you want to order (or 'done' to finish):")  # Repeat item input

    if item_list:
        order_id = len(orders) + 1
        orders.append((order_id, customer_name, item_list, total_bill))
        st.success(f"Order placed successfully! Your total bill is Rs. {total_bill}.")
    else:
        st.warning("No items selected. Order not placed.")

# Display the total revenue
def display_total_revenue():
    total_revenue = sum(order[3] for order in orders)
    st.subheader(f"Total Revenue Generated: Rs. {total_revenue}")

# Display the list of customers
def display_unique_customers():
    st.subheader("Unique Customers:")
    for customer in unique_customers:
        st.write(customer)

# Display all orders
def display_orders():
    st.subheader("Orders:")
    for order_id, customer_name, item_list, total_bill in orders:
        st.write(f"Order ID: {order_id}, Customer: {customer_name}, Items: {', '.join(item_list)}, Total Bill: Rs. {total_bill}")

# Main program starts here
def main():
    menu_choice = st.sidebar.radio(
        "Choose an option",
        ("Place an Order", "Display Total Revenue", "Display Unique Customers", "Display All Orders", "Exit")
    )

    if menu_choice == "Place an Order":
        place_order()
    elif menu_choice == "Display Total Revenue":
        display_total_revenue()
    elif menu_choice == "Display Unique Customers":
        display_unique_customers()
    elif menu_choice == "Display All Orders":
        display_orders()
    elif menu_choice == "Exit":
        st.write("Exiting the system. Goodbye!")

if __name__ == "__main__":
    main()
