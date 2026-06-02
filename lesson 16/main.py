import streamlit as st

def main():
    st.title("Hello World")

    st.button("click me")

    st.checkbox("Check me")

    if st.button("click"):
        st.write("buton clicked")

if __name__=="__main__":
    main()