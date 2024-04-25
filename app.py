import os
from joblib import load
import streamlit as st
import sklearn
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="e-commerce-shipping",
                   layout="wide",
                   page_icon="🚚")

# Getting the absolute working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Construct absolute path to the model file
model_path = os.path.join(working_dir, 'saved_models', 'ecom.sav')

# Load the saved model
try:
    ecom_model = load(model_path)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    ecom_model = None  # Assign None to ecom_model if loading fails
  
# Sidebar for navigation
with st.sidebar:
    selected = option_menu('E-commerce Shipping Prediction System',
                           ['Reached.on.Time_Y.N'],
                           menu_icon='wrapped-gift',
                           icons=['person'],
                           default_index=0)

# E-commerce Shipping Prediction Page
if selected == 'Reached.on.Time_Y.N':

    # Page title
    st.title('E-commerce Shipping Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Customer_care_calls = st.text_input('Customer_care_calls')

    with col2:
        Customer_rating = st.text_input('Customer_rating')

    with col3:
        Cost_of_the_Product = st.text_input('Cost_of_the_Product')

    with col1:
        Prior_purchases = st.text_input('Prior_purchases')

    with col2:
        Product_importance = st.text_input('Product_importance')

    with col3:
        Gender = st.text_input('Gender')

    with col1:
        Discount_offered = st.text_input('Discount_offered')

    with col2:
        Weight_in_gms = st.text_input('Weight_in_gms')

    with col3:
        Warehouse_block_0 = st.text_input('Warehouse_block_0')

    with col1:
        Warehouse_block_1 = st.text_input('Warehouse_block_1')

    with col2:
        Warehouse_block_2 = st.text_input('Warehouse_block_2')

    with col3:
        Warehouse_block_3 = st.text_input('Warehouse_block_3')

    with col1:
        Warehouse_block_4 = st.text_input('Warehouse_block_4')

    with col2:
        Mode_of_Shipment_0 = st.text_input('Mode_of_Shipment_0')

    with col3:
        Mode_of_Shipment_1 = st.text_input('Mode_of_Shipment_1')

    with col1:
        Mode_of_Shipment_2 = st.text_input('Mode_of_Shipment_2')

    # Code for Prediction
    Time_YN = ''

    # Creating a button for Prediction
    if ecom_model and st.button('Reached.on.Time_Y.N'):

        user_input = [Customer_care_calls, Customer_rating, Cost_of_the_Product, Prior_purchases, Product_importance,
                      Gender, Discount_offered, Weight_in_gms, Warehouse_block_0, Warehouse_block_1, Warehouse_block_2,
                      Warehouse_block_3, Warehouse_block_4, Mode_of_Shipment_0, Mode_of_Shipment_1, Mode_of_Shipment_2]

        user_input = [float(x) for x in user_input]

        Time_YN = ecom_model.predict([user_input])

        if Time_YN[0] == 1:
            Time_YN = 'The Product Will Reach On Time'
        else:
            Time_YN = 'The Product Will Not Reach On Time'

    st.success(Time_YN)
