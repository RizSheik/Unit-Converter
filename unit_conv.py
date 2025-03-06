import streamlit as st
import time

# Custom CSS for styling with animations and dark mode support
st.markdown(
    """
    <style>
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e1e1e, #343a40, #495057, #6c757d);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        color: white;
    }
    
    h1 {
        font-size: 36px;
        text-align: center;
        color: white;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(255, 75, 43, 0.4);
    }
    
    .stButton>button:hover {
       transform: scale(1.1);
       background: linear-gradient(45deg, #00c9ff, #92fe9d);
       color: black;
       box-shadow: 0 0 20px rgba(0, 201, 255, 0.8);
    }
    
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
        transition: transform 0.3s ease-in-out;
    }
    
    .result-box:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dark Mode Toggle
st.sidebar.markdown("## 🌓 Toggle Dark Mode")
dark_mode = st.sidebar.checkbox("Enable Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background: #121212 !important;
            color: white !important;
        }
        .stButton>button {
            background: linear-gradient(45deg, #1e88e5, #1565c0);
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #64b5f6, #42a5f5);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Title and description
st.markdown("<h1>Unit Converter Using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Convert between Length, Weight, and Temperature using this simple app.")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Dropdowns for selecting units
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches", "Centimeters", "Millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches", "Centimeters", "Millimeters"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_convert(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Feet": 3.28084, "Miles": 0.000621371, "Yards": 1.09361, "Inches": 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convert(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return None

# Button for conversion
if st.button("🔄️ Convert"):
    time.sleep(0.3)
    if from_unit == to_unit:
        st.warning("Please select different units for conversion.")
    else:
        result = (length_convert(value, from_unit, to_unit) if conversion_type == "Length" else
                  weight_convert(value, from_unit, to_unit) if conversion_type == "Weight" else
                  temperature_convert(value, from_unit, to_unit))
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; font-size: 14px;'>
        Developed by <a href='https://github.com/RizSheik' target='_blank'>Rizwan</a>
    </div>
""", unsafe_allow_html=True)