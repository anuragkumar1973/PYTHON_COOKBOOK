import streamlit as st
from pathlib import Path

# rec2_11.py
# Streamlit app: read welcome.txt from same folder, show email content, require approval before "sending"

st.set_page_config(page_title="Email Composer", layout="centered")

def load_welcome():
    base = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    fp = base / "welcome.txt"
    if not fp.exists():
        return None, fp
    try:
        return fp.read_text(encoding="utf-8"), fp
    except Exception as e:
        return f"Error reading file: {e}", fp

content, filepath = load_welcome()

st.header("Email Composer")
st.write(f"Reading: {filepath}")

if content is None:
    st.error(f"'welcome.txt' not found at {filepath}")
    st.stop()

if content.startswith("Error reading file:"):
    st.error(content)
    st.stop()

# Display editable email content
email_text = st.text_area("Email-content", value=content, height=300)

# Approval dropdown that must be set to 'Good to send email'
options = ["Select status", "Good to send email", "Needs edits", "Hold"]
status = st.selectbox("Approval status", options)

# Send button
if st.button("Send email"):
    if status != "Good to send email":
        st.warning('Please select "Good to send email" from the dropdown before sending.')
    else:
        # Simulate sending; in a real app integrate an email service here.
        st.success("Email sent (simulated).")
        st.subheader("Final email content")
        st.code(email_text)