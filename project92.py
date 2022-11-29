import streamlit as st

def calculate_email(p, n, r):
  emi = p * (r/100) * (((1 + (r/100))**n)/(((1 + (r/100))**n) - 1))
  return round(emi, 3)

def calculate_outstanding_balance(p, n, r, m):
  r = r/100
  balance = (p * ((1 + r)**n) - ((1 + r)**m))/(((1 + r)**n) - 1)
  return balance

st.title("EMI Calculator App")
principal = st.slider("Principal Loan Amount", 1000, 1000000)
tenure = st.slider("Loan period (in years)", 1, 30)
roi = st.slider("Rate of Interest (in % per annum)", 1.00, 15.00)
m = st.slider("Period after which the Outstanding Loan Balance is calculated (in months)", 1, tenure * 12)
 
n = tenure * 12
r = roi/12

if st.button("Calculate EMI"):
	emi = calculate_email(principal, n, r)
	st.write("EMI:",emi)
 
if st.button("Calculate Outstanding Loan Balance"):
  olb = calculate_outstanding_balance(principal, n, r, m)
  st.write("Outstanding Loan Balance:", olb)
