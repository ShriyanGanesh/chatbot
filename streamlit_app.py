import streamlit as st
from openai import OpenAI



# Sample data for fish inventory
fish_inventory = {
    "Salmon": {"price": 20, "stock": 10},
    "Tuna": {"price": 15, "stock": 8},
    "Cod": {"price": 12, "stock": 5},
    "Trout": {"price": 18, "stock": 7},
}

# Shopping cart dictionary
cart = {}

# Function to add fish to the cart
def add_to_cart(fish, quantity):
    if fish in fish_inventory and fish_inventory[fish]["stock"] >= quantity:
        cart[fish] = cart.get(fish, 0) + quantity
        fish_inventory[fish]["stock"] -= quantity
        st.success(f"Added {quantity} {fish}(s) to the cart.")
    else:
        st.error(f"Not enough stock for {fish}.")

# Function to display the catalog
def display_catalog():
    st.header("Fish Catalog")
    for fish, details in fish_inventory.items():
        st.write(f"**{fish}** - ${details['price']} per piece")
        st.write(f"Stock: {details['stock']}")
        quantity = st.number_input(f"Enter quantity for {fish}", min_value=0, max_value=details['stock'], key=fish)
        if st.button(f"Add {fish} to Cart", key=f"add_{fish}"):
            add_to_cart(fish, quantity)

# Function to display the shopping cart
def display_cart():
    st.header("Shopping Cart")
    if cart:
        total_cost = 0
        for fish, quantity in cart.items():
            price = fish_inventory[fish]["price"]
            total = price * quantity
            total_cost += total
            st.write(f"**{fish}** - {quantity} pcs - ${total}")
        st.write(f"**Total Cost:** ${total_cost}")
        if st.button("Checkout"):
            st.success("Order placed successfully!")
            cart.clear()
    else:
        st.write("Your cart is empty.")

# Streamlit app layout
def main():
    st.title("Online Fish Selling App")
    
    menu = ["Catalog", "Cart"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Catalog":
        display_catalog()
    elif choice == "Cart":
        display_cart()

if __name__ == '__main__':
    main()




    

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
