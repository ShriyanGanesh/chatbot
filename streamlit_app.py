import streamlit as st

# Sample data for products
product_catalog = {
    "Salmon": {"price": 20, "stock": 10, "image": "images/salmon.jpg"},
    "Tuna": {"price": 15, "stock": 8, "image": "images/tuna.jpg"},
    "Cod": {"price": 12, "stock": 5, "image": "images/cod.jpg"},
    "Trout": {"price": 18, "stock": 7, "image": "images/trout.jpg"},
}

# Shopping cart dictionary
cart = {}

# Function to add products to the cart
def add_to_cart(product, quantity):
    if product in product_catalog and product_catalog[product]["stock"] >= quantity:
        cart[product] = cart.get(product, 0) + quantity
        product_catalog[product]["stock"] -= quantity
        st.success(f"Added {quantity} {product}(s) to the cart.")
    else:
        st.error(f"Not enough stock for {product}.")

# Function to display the product catalog
def display_catalog():
    st.header("Product Catalog")
    for product, details in product_catalog.items():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(details["image"], width=150)
        with col2:
            st.write(f"**{product}**")
            st.write(f"Price: ${details['price']} per piece")
            st.write(f"Stock: {details['stock']}")
            quantity = st.number_input(f"Quantity for {product}", min_value=0, max_value=details['stock'], key=product)
            if st.button(f"Add {product} to Cart", key=f"add_{product}"):
                add_to_cart(product, quantity)
        st.markdown("---")

# Function to display the shopping cart
def display_cart():
    st.header("Shopping Cart")
    if cart:
        total_cost = 0
        for product, quantity in cart.items():
            price = product_catalog[product]["price"]
            total = price * quantity
            total_cost += total
            st.write(f"**{product}** - {quantity} pcs - ${total}")
        st.write(f"**Total Cost:** ${total_cost}")
        if st.button("Checkout"):
            st.success("Order placed successfully!")
            cart.clear()
    else:
        st.write("Your cart is empty.")

# Streamlit app layout
def main():
    st.title("Online Shopping App")

    menu = ["Catalog", "Cart"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Catalog":
        display_catalog()
    elif choice == "Cart":
        display_cart()

if __name__ == '__main__':
    main()
