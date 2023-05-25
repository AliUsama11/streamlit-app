import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.subheader("Welcome to my app!")

    # Add a slider widget
    value = st.slider("Select a value", 0, 100, 50)

    st.write("You selected:", value)

if __name__ == "__main__":
    main()