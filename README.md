# AI Fake / Scam Message Detector

## Overview

AI Fake / Scam Message Detector is an OCR-based web application developed using Python and Streamlit.

The main purpose of this project is to analyze screenshots of messages and identify possible scam or fraudulent indicators.

Users can upload a screenshot of an SMS, WhatsApp message, email message, banking alert, reward message, KYC notification, or any other text-based message.

The application extracts the text from the screenshot using Tesseract OCR and analyzes the extracted text using rule-based scam detection.

The system checks for:

- Scam-related keywords
- Urgent language
- OTP requests
- Password requests
- PIN requests
- Banking-related words
- Suspicious URLs
- Prize or reward messages
- Account blocking or suspension messages
- KYC-related messages
- Payment-related messages

After analyzing the message, the application calculates a risk score between 0 and 100.

The result is classified into:

- Low Risk
- Medium Risk
- High Risk

The application also provides basic safety recommendations.

---

# Project Title

## AI Fake / Scam Message Detector

![Uploading image.png…]()


# Problem Statement

Scam and phishing messages are becoming increasingly common.

Scammers often send messages pretending to be banks, government organizations, delivery companies, shopping websites, payment services, or other trusted organizations.

Examples include:

```text
Your bank account has been blocked.
Verify your account immediately.
Project Objective

The main objective of this project is to create a simple application that can analyze message screenshots and identify possible scam indicators.

The project has the following objectives:

Accept screenshots as input.
Extract text from screenshots using OCR.
Detect suspicious scam-related keywords.
Detect URLs.
Calculate a risk score.
Classify the message.
Display detected indicators.
Provide safety recommendations.
Create a foundation for future machine learning integration.

Technologies Used
Programming Language

Python

User Interface

Streamlit

OCR

Tesseract OCR

Python OCR Library

Pytesseract

Image Processing

Pillow

Text Pattern Detection

Python Regular Expressions
Project Architecture

The system follows this architecture:
User
 |
 v
Upload Screenshot
 |
 v
Image Processing
 |
 v
Tesseract OCR
 |
 v
Extracted Text
 |
 +--------------------+
 |                    |
 v                    v
Keyword Detection   URL Detection
 |                    |
 +---------+----------+
           |
           v
      Risk Calculation
           |
           v
    Risk Classification
           |
           v
      Final Result
           |
           v
      Safety Tips

Disclaimer

This project is developed for educational and demonstration purposes.

The result produced by this application should not be considered a guaranteed security decision.

A Low Risk message may still be malicious.

A High Risk message may not necessarily be fraudulent.

Users should always verify important information using official sources.

Never share OTPs, passwords, PINs, or banking credentials with unknown persons or suspicious websites.

AUTHOR:
KEERTHANA.P
