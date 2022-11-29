import streamlit as st
import cursor,streamlit_functions

#Title for streamlit app
st.title("Clinic Database")
# CLinic class onject declaration
Clinic=cursor.clinic_database()
# Side bar intilatization
choice = st.sidebar.selectbox("Menu", ["Add", "View","Update", "Delete", "Any Function"])
#function calls 
if choice == "Add":
    streamlit_functions.Add(Clinic)
elif choice == "View":
    streamlit_functions.View(Clinic)
elif choice == "Delete":
    streamlit_functions.Delete(Clinic)
elif choice =="Any Function":
    streamlit_functions.AnyFunc(Clinic)
elif choice == "Update":
    streamlit_functions.Update(Clinic)