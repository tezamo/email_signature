import streamlit as st

# Default IAMO link if none is provided
DEFAULT_IAMO_LINK = "https://www.iamo.de/en/home"

st.set_page_config(page_title="IAMO Email Signature Generator", page_icon="✉️", layout="centered")

st.title("✉️ IAMO Email Signature Generator")

# --- Input form ---
st.subheader("Personal Information")
prefix = st.selectbox("Prefix", ["", "Dr.", "Professor"])
name = st.text_input("Full Name (e.g., Miranda Svanidze)")
profession = st.text_input("Profession (e.g., Research Associate)")
phone_last_digit = st.text_input("Last Digit of Phone Number (e.g., 1)", max_chars=1)
email = st.text_input("Email Address")
iamo_link = st.text_input("IAMO Profile Link (Leave blank to use default)")

# Button to generate signature
if st.button("Generate Signature"):
    # Use default link if none provided
    profile_link = iamo_link.strip() if iamo_link.strip() else DEFAULT_IAMO_LINK

    # Build the email signature HTML
    signature_html = f"""
    <!-- Personal Signature -->
    <table>
       <tbody>
          <tr>
             <td style="border-right: 3px solid #005398;">
                <a href="https://www.iamo.de/en/home" target="_blank" rel="noopener">
                <img src="https://www.iamo.de/fileadmin/user_upload/Bilder_und_Dokumente/logos/iamo/logo.png" 
                     alt="IAMO Logo" width="100" border="0" />
                </a>
             </td>
             <td style="color: #3f3f3f; padding-left: 10px;">
                {prefix} {name}<br />
                {profession}<br /><br />
                Leibniz Institute of Agricultural Development in Transition Economies (IAMO)<br />
                Theodor-Lieser-Str. 2, 06120 Halle (Saale), Germany<br />
                Tel.: +49 345 2928-57{phone_last_digit}<br />
                <a style="color: #005398;" href="mailto:{email}">{email}</a>&nbsp;|&nbsp;
                <a style="color: #005398;" href="{profile_link}">{profile_link}</a>
             </td>
          </tr>
       </tbody>
    </table>
    <p>&nbsp;</p>
    """

    st.success("✅ Signature generated successfully!")
    st.markdown("### 📋 Copy your HTML below:")
    st.code(signature_html, language="html")

    # Preview
    st.markdown("### 🖼 Preview")
    st.markdown(signature_html, unsafe_allow_html=True)

# Footer
st.caption("Created with Streamlit • IAMO Signature Helper")
