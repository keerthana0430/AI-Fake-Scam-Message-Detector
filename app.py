import streamlit as st
import pytesseract
import re
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


st.set_page_config(
    page_title="AI Scam Message Detector",
    layout="centered"
)


st.title("AI Scam Message Detector")

st.write(
    "Upload a screenshot of a message. "
    "The system will extract text using OCR "
    "and detect possible scam indicators."
)

st.divider()


SCAM_KEYWORDS = [
    "urgent",
    "otp",
    "password",
    "pin",
    "verify",
    "verification",
    "winner",
    "won",
    "lottery",
    "prize",
    "reward",
    "claim",
    "click",
    "blocked",
    "suspended",
    "kyc",
    "bank",
    "cash",
    "free",
    "immediately",
    "payment",
    "gift",
    "congratulations"
]


def find_suspicious_words(text):
    text = text.lower()

    found = []

    for word in SCAM_KEYWORDS:
        if word in text:
            found.append(word)

    return found


def find_links(text):
    return re.findall(
        r"(https?://[^\s]+|www\.[^\s]+)",
        text
    )


def calculate_risk(text, suspicious_words, links):
    text = text.lower()

    score = 0

    score += len(suspicious_words) * 8

    if links:
        score += 20

    if "urgent" in text:
        score += 15

    if "otp" in text:
        score += 20

    if "password" in text or "pin" in text:
        score += 20

    if "bank" in text:
        score += 10

    return min(score, 100)


def get_risk_level(score):

    if score >= 50:
        return "High Risk"

    elif score >= 25:
        return "Medium Risk"

    else:
        return "Low Risk"


uploaded_file = st.file_uploader(
    "Upload Message Screenshot",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        caption="Message Screenshot",
        use_container_width=True
    )

    st.divider()

   
    st.subheader("Extracted Text")

    try:

        extracted_text = pytesseract.image_to_string(image)
        extracted_text = extracted_text.strip()

    except Exception:

        st.error(
            "OCR failed. Please check Tesseract OCR installation."
        )

        st.stop()

    if extracted_text:

        st.text_area(
            "OCR Result",
            extracted_text,
            height=200
        )

    else:

        st.warning(
            "No readable text found in the image."
        )

   
    suspicious_words = find_suspicious_words(
        extracted_text
    )

    links = find_links(
        extracted_text
    )

    st.divider()

   
    st.subheader("Suspicious Indicators")

    if suspicious_words:

        st.warning(
            "Suspicious keywords detected:"
        )

        for word in suspicious_words:
            st.write(f"- {word}")

    else:

        st.write(
            "No suspicious keywords detected."
        )

  
    st.subheader("Link Check")

    if links:

        st.warning("Link detected:")

        for link in links:
            st.write(link)

    else:

        st.write("No links detected.")

   
    risk_score = calculate_risk(
        extracted_text,
        suspicious_words,
        links
    )

    risk_level = get_risk_level(
        risk_score
    )

    st.divider()

    st.subheader("Risk Analysis")

    st.metric(
        "Risk Score",
        f"{risk_score} / 100"
    )

    if risk_level == "High Risk":

        st.error(
            f"Risk Level: {risk_level}"
        )

    elif risk_level == "Medium Risk":

        st.warning(
            f"Risk Level: {risk_level}"
        )

    else:

        st.success(
            f"Risk Level: {risk_level}"
        )

    st.divider()

    
    st.subheader("Safety Tips")

    st.write("1. Never share OTP or PIN.")

    st.write("2. Do not click unknown links.")

    st.write(
        "3. Do not share passwords or banking details."
    )

    st.write(
        "4. Verify suspicious messages through official sources."
    )

    st.write(
        "5. Do not send money based only on a message."
    )