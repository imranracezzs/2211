import streamlit as st

def calculate_electricity_bill(previous_units, current_units, customer_type):
    """Calculates electricity bill based on customer type and consumption."""

    no_of_units = current_units - previous_units

    if customer_type == "residential":
        rate = 3
        energy_charges = 50
        fixed_charges = 10
        customer_charges = 15
    elif customer_type == "commercial":
        rate = 5
        energy_charges = 100
        fixed_charges = 30
        customer_charges = 25
    elif customer_type == "industrial":
        rate = 8
        energy_charges = 150
        fixed_charges = 50
        customer_charges = 40
    else:
        st.write("Invalid customer type")
        return None  # Return None to indicate an error

    cost = no_of_units * rate
    duty_charges = no_of_units * 0.06
    bill_amount = cost + energy_charges + fixed_charges + customer_charges + duty_charges

    return {
        "no_of_units": no_of_units,
        "energy_charges": energy_charges,
        "fixed_charges": fixed_charges,
        "customer_charges": customer_charges,
        "duty_charges": duty_charges,
        "bill_amount": bill_amount,
    }

st.title("Electricity Bill Calculator")

# Use Streamlit for user input
previous_units = st.number_input("Enter the previous units", min_value=0)
current_units = st.number_input("Enter the current units", min_value=0, key="current_units")

if current_units < previous_units:
    st.error("Current units cannot be less than previous units. Please check your input.")
else:
    # Call the function to calculate the bill
    bill_details = calculate_electricity_bill(previous_units, current_units, st.selectbox("Customer type", ["residential", "commercial", "industrial"]))

    if bill_details:  # Check if function returned a value (indicating no errors)
        st.write("**Bill Details:**")
        for key, value in bill_details.items():
            st.write(f"{key.capitalize()}: {value:.2f}")  # Capitalize key and format with 2 decimal places