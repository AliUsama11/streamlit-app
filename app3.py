import streamlit as st

def main():
    st.title("Streamlit App")
    name = st.text_input("Enter your name:")
    button = st.button("Submit")

    if button:
        st.write(f"Goodbye, {name}!")

if __name__ == "__main__":
    main()
