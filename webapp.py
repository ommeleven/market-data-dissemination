import streamlit as st
import ctypes

# Load the C++ shared library
lib = ctypes.CDLL('./example.so')

# Define the argument and return types for the C++ function
lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
lib.add.restype = ctypes.c_int

# Streamlit UI
st.title("C++ Function Call from Streamlit")
a = st.number_input("Enter first number:", value=0)
b = st.number_input("Enter second number:", value=0)

if st.button("Add"):
    result = lib.add(a, b)
    st.write(f"The result is: {result}")
