import streamlit as st
import requests as r

response = r.get('http://backend:8000/')

st.write(f"{response.json()['message']}")

st.write('hot reload')
