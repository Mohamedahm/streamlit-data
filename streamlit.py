import streamlit as st
from fpdf import FPDF

# Define the Streamlit app
def app():
    # Set the app title
    st.title("PDF Generator App")

    # Create a textbox for the user to enter text
    text = st.text_input("Enter text:")

    # Create a button to generate the PDF
    if st.button("Generate PDF"):
        # Initialize the PDF object
        pdf = FPDF()

        # Add a page to the PDF
        pdf.add_page()

        # Set the font and font size
        pdf.set_font("Arial", size=12)

        # Add the text to the PDF
        pdf.cell(200, 10, txt=text, ln=1)

        # Save the PDF
        pdf.output("output.pdf")

        # Display a success message to the user
        st.success("PDF generated successfully.")

# Run the Streamlit app
if __name__ == "__main__":
    app()
