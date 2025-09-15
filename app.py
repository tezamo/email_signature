import streamlit as st

st.set_page_config(page_title="IAMO Signature Generator", page_icon="✉️", layout="centered")
st.title("✉️ IAMO Email Signature Generator")

# --- Inputs ---
st.subheader("Personal Information")

# 1. Prefix options + custom
prefix_choice = st.selectbox("Choose Prefix", ["Dr.", "Professor", "Other"])
custom_prefix = ""
if prefix_choice == "Other":
    custom_prefix = st.text_input("Enter custom prefix")
prefix = custom_prefix if prefix_choice == "Other" else prefix_choice

first_name = st.text_input("First Name")
family_name = st.text_input("Family Name")
profession = st.text_input("Profession (e.g., Research Associate)")
phone_last3 = st.text_input("Last 3 digits of phone (e.g., 571)", max_chars=3)

email_name = st.text_input("IAMO Email (name before @iamo.de)")
has_page = st.checkbox("Has IAMO profile page?")
iamo_link = ""
if has_page:
    iamo_link = st.text_input("IAMO Profile Link (e.g., https://www.iamo.de/institut/mitarbeitende/details/svanidze)")

# --- Generate signature ---
if st.button("Generate Signature"):
    # Build IAMO display link and href
    if has_page and iamo_link.strip():
        display_link = f"www.iamo.de/{family_name.lower()}"
        href_link = iamo_link.strip()
    else:
        display_link = "www.iamo.de"
        href_link = "https://www.iamo.de/en/home"

    # Assemble HTML
    signature_html = f"""
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
                {prefix} {first_name} {family_name}<br />
                {profession}<br /><br />
                Leibniz Institute of Agricultural Development in Transition Economies (IAMO)<br />
                Theodor-Lieser-Str. 2, 06120 Halle (Saale), Germany<br />
                Tel.: +49 345 2928-{phone_last3}<br />
                <a style="color: #005398;" href="mailto:{email_name}@iamo.de">{email_name}@iamo.de</a>&nbsp;|&nbsp;
                <a style="color: #005398;" href="{href_link}">{display_link}</a>
             </td>
          </tr>
       </tbody>
    </table>
    <p>&nbsp;</p>
    """

    # Show rendered preview only
    st.markdown("### 🖼 Signature Preview")
    st.markdown(signature_html, unsafe_allow_html=True)

    # Hidden copy button (Streamlit trick using text_area + copy)
    st.download_button(
        label="📋 Copy Signature HTML",
        data=signature_html,
        file_name="signature.html",
        mime="text/html"
    )
    st.caption("Click 'Copy Signature HTML' to copy or download your signature.")
