import streamlit as st

def main():
    st.title("Hello World")

    st.button("click me")

    st.checkbox("Check me")

    if st.button("click"):
        st.write("buton clicked")

age = st.number_input("enter your age", min_value=0,max_value=100)
st.write("your age is",age)

message = st.text_area("enter a message")

if st.button("Success"):
    st.success("Operation was successfull")

if __name__=="__main__":
    main()








































