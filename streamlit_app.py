import streamlit as st

#Menu dictionary
menu = {
    "Burger": (150, "Fast Food"),
    "Pizza": (300, "Fast Food"),
    "Pasta": (250, "Italian"),
    "Ice Cream": (100, "Dessert"),
    "Salad": (120, "Healthy"),
}

#Session state
if "orders" not in st.session_state:
    st.session_state.orders = []
if "unique_customers" not in st.session_state:
    st.session_state.unique_customers = set()

#Display all menu items
def display_menu():
    st.subheader("Menu")
    for item, (price, category) in menu.items():
        st.write(f"**{item}**: Rs. {price} ({category})")

#Place order
def place_order():
    st.subheader("Place an Order")
    customer_name = st.text_input("Enter your name")
    
    selected_items = st.multiselect("Select items from the menu", list(menu.keys()))
    total_bill = sum(menu[item][0] for item in selected_items)
    
    if st.button("Confirm Order"):
        if customer_name and selected_items:
            order_id = len(st.session_state.orders) + 1
            st.session_state.orders.append((order_id, customer_name, selected_items, total_bill))
            st.session_state.unique_customers.add(customer_name)
            st.success(f"Order placed successfully! Your total bill is Rs. {total_bill}.")
        else:
            st.warning("Please enter your name and select at least one item.")

#Display total revenue
def display_total_revenue():
    total_revenue = sum(order[3] for order in st.session_state.orders)
    st.subheader("Total Revenue Generated")
    st.write(f"Rs. {total_revenue}")

#Display all customers (no repetition because of set)
def display_unique_customers():
    st.subheader("Unique Customers")
    if st.session_state.unique_customers:
        for customer in st.session_state.unique_customers:
            st.write(customer)
    else:
        st.write("No customers yet.")

#Display all orders
def display_orders():
    st.subheader("All Orders")
    if st.session_state.orders:
        for order_id, customer_name, item_list, total_bill in st.session_state.orders:
            st.write(f"**Order ID:** {order_id}  |  **Customer:** {customer_name}  |  **Items:** {', '.join(item_list)}  |  **Total Bill:** Rs. {total_bill}")
    else:
        st.write("No orders placed yet.")


def main():
    st.title("Online FoodKart Delivery System")
    st.write("Shaurya Juneja")
    menu_choice = st.sidebar.radio("Navigate", ["Menu", "Place an Order", "Total Revenue", "Unique Customers", "All Orders"])
    
    if menu_choice == "Menu":
        display_menu()
    elif menu_choice == "Place an Order":
        place_order()
    elif menu_choice == "Total Revenue":
        display_total_revenue()
    elif menu_choice == "Unique Customers":
        display_unique_customers()
    elif menu_choice == "All Orders":
        display_orders()

if __name__ == "__main__":
    main()
