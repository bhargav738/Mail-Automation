# Bulk Resume Email Sender 📧

This Python script automates sending personalized job application emails with your resume attached to multiple recipients from a CSV file.

---

## 🚀 Features
- Sends bulk emails using Gmail SMTP.
- Customizes each email with recipient's name and company.
- Attaches your resume (PDF) automatically.
- Reads recipients’ details from a CSV file.

---

## 📂 Project Structure
├── send_emails.py # Main script
├── Bhargav_Resume_PBI.pdf # Your resume (replace with actual file path)
├── d.csv # CSV file with recipient details
└── README.md # Documentation


---

## ⚙️ Requirements
- Python 3.7+
- Gmail account (with **App Password** if 2FA enabled)

Install required libraries (standard libraries only):
```bash
No extra installation needed (uses smtplib, csv, email built-ins).


📝 CSV Format
Name,Email,Company
John Doe,johndoe@example.com,Google
Jane Smith,janesmith@example.com,Microsoft

🔑 Gmail Setup
Enable 2-Step Verification on your Gmail.

Generate an App Password (16-character code).

Replace the PASSWORD in the script with this app password.

