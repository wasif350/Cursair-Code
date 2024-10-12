import streamlit as st
import requests

# Backend API URL
BASE_URL = "https://79b8fe16-d2de-4d6a-baaf-67eebc9c2db4-00-24ny68vgriwu6.janeway.replit.dev"

# Streamlit App
st.title('Enhanced Code Editor')

# Code Generation
st.header("Code Generator")
prompt = st.text_area("Enter prompt here...")
language = st.selectbox("Select language", ["python", "javascript"])
if st.button("Generate Code"):
    response = requests.post(f"{BASE_URL}/generate_code/", json={"prompt": prompt, "language": language})
    if response.status_code == 200:
        st.code(response.json()["code"], language=language)
    else:
        st.error("Error generating code.")

# Code Optimizer
st.header("Code Optimizer")
code_to_optimize = st.text_area("Enter code to optimize")
if st.button("Optimize Code"):
    response = requests.post(f"{BASE_URL}/optimize_code/", json={"code": code_to_optimize})
    if response.status_code == 200:
        st.code(response.json()["optimized_code"], language="python")
    else:
        st.error("Error optimizing code.")

# Code Explainer
st.header("Code Explainer")
code_to_explain = st.text_area("Enter code to explain")
if st.button("Explain Code"):
    response = requests.post(f"{BASE_URL}/explain_code/", json={"code": code_to_explain})
    if response.status_code == 200:
        st.write(response.json()["explanation"])
    else:
        st.error("Error explaining code.")

# Collaboration
st.header("Code Collaborate")
session_id = st.text_input("Enter Collaboration Session ID")
collab_input = st.text_input("Enter message to collaborate")
if st.button("Send Collaboration Message"):
    if session_id and collab_input:
        response = requests.post(f"{BASE_URL}/collaborate/", json={"session_id": session_id, "message": collab_input})
        if response.status_code == 200:
            st.success("Message sent!")
        else:
            st.error("Error sending collaboration message.")
    else:
        st.warning("Please enter a session ID and message.")

# Debug Assistant
st.header("Debug Assistant")
debug_code = st.text_area("Enter code to debug")
if st.button("Debug Code"):
    try:
        with open("temp_debug_code.py", "w") as file:
            file.write(debug_code)
        result = subprocess.run(["python", "temp_debug_code.py"], capture_output=True, text=True)
        st.text(f"Output: {result.stdout}\nError: {result.stderr}")
    except Exception as e:
        st.error(f"Error debugging code: {e}")

# Testing Assistance
st.header("Testing Assistant")
test_code = st.text_area("Enter code for which you need unit tests")
if st.button("Generate Unit Tests"):
    response = requests.post(f"{BASE_URL}/generate_code/", json={"prompt": f"Write unit tests for the following code:\n{test_code}", "language": "python"})
    if response.status_code == 200:
        st.code(response.json()["code"], language="python")
    else:
        st.error("Error generating unit tests.")

# Educational Mode
st.header("Educational Mode")
edu_code = st.text_area("Enter code for educational explanation")
if st.button("Explain for Non-Technical Audience"):
    response = requests.post(f"{BASE_URL}/explain_code/", json={"code": edu_code})
    if response.status_code == 200:
        st.write("Educational Explanation: " + response.json()["explanation"])
    else:
        st.error("Error explaining code.")
