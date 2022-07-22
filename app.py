import streamlit as st
def calculate(a,b,c):
    maxnumber=max([a,b,c])
    st.write("""## Max of the given Numbers is """+ str(maxnumber))
st.write("""
# Finds the max of the given three numbers
# """)
a=st.number_input("First Number")
b=st.number_input("Second Number")
c=st.number_input("Third Number")
st.button("Calculate", on_click=calculate(a,b,c))
