import streamlit as st

# App Title
st.title("CDC Morphine Milligram Equivalent (MME) Calculator")

# Introduction
st.write("""
This application helps healthcare providers calculate the total Morphine Milligram Equivalent (MME) for opioid prescriptions. By inputting the type and dosage of opioids, the app provides the MME to help ensure safe prescribing practices in line with CDC guidelines.
""")

# Opioid conversion factors (examples, not exhaustive)
opioid_conversion_factors = {
    "Morphine": 1,
    "Hydrocodone": 1,
    "Oxycodone": 1.5,
    "Oxymorphone": 3,
    "Codeine": 0.15,
    "Fentanyl (transdermal mcg/hr)": 2.4,
    "Methadone (1-20 mg/day)": 4,
    "Methadone (21-40 mg/day)": 8,
    "Methadone (41-60 mg/day)": 10,
    "Methadone (≥61-80 mg/day)": 12,
}

# Collecting Opioid Information
st.header("Opioid Prescription Information")

opioid_type = st.selectbox("Select Opioid Type", options=list(opioid_conversion_factors.keys()))
dosage = st.number_input("Dosage (mg per day or mcg/hr for fentanyl)", min_value=0.0, step=0.1, value=0.0)

# Calculate MME
st.header("Calculated MME")

if opioid_type and dosage > 0:
    conversion_factor = opioid_conversion_factors[opioid_type]
    mme = dosage * conversion_factor
    st.write(f"The total MME is: {mme} mg/day")
else:
    st.write("Please enter valid opioid type and dosage.")

st.write("""
### General Guidelines:
1. **Assess Risk**: Regularly evaluate risk factors for opioid-related harms.
2. **Monitor Therapy**: Continuously monitor patients and adjust therapy as needed.
3. **Use the Lowest Effective Dose**: Prescribe the lowest effective dose to manage pain.
4. **Consider Tapering**: When appropriate, consider tapering opioids to lower dosages or discontinuing use.

Refer to the full [CDC guidelines](https://www.cdc.gov/drugoverdose/prescribing/guideline.html) for detailed information.
""")
