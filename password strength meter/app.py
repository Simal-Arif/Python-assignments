import re
import streamlit as st

# page styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
# Custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}
    .stButton button:hover {background-color:red; color: white;}
</style>
""",unsafe_allow_html=True) 

#page title and description 
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level.")

# function to check password meter
def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score  += 1 # increased score by 1 
    else: 
        feedback.append("Password should be atleast 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
    else:
            feedback.append("Password should include both upper case and lower case letters.")

    if re.search(r"\d", password):
            score += 1
    else:
            feedback.append("Password should include at least one number (0-9).")

         # special characters
    if re.search(r"[!@#$%^&*]", password):
            score += 1
    else:
            feedback.append("Include at least one special character (!@#$%^&*).")

        # Display results
    if score == 4:
            st.success("Strong Password - Your password is secure.")
    elif score == 3:
            st.info("Moderate Password - Consider improving security by adding more features.")
    else:
            st.error("Weak Password - Follow the suggestions below to strength it.")

        # feedback
    if feedback:
        with st.expander("Improve your password"):
            for item in feedback: 
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong.")

# Working of button 
if st.button("Check strength"):
    if password:
        check_password(password)
    else:
        st.warning("Please enter a password first!")  # show warning if password is empty
