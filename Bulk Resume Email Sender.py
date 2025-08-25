import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# --- CONFIGURATION ---
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'your user name'         # <-- Replace with your email
PASSWORD = 'password'            # <-- Use an App Password if Gmail 2FA is enabled

FROM_EMAIL = USERNAME
RESUME_PATH = "your resume path"           # <-- Replace with your actual resume file path

# --- EMAIL TEMPLATE ---
def create_message(recipient_name, company, to_email):
    subject = f"Application for Data Analyst Role at {company}"

    body = f"""Dear {recipient_name},

I am writing to express my interest in the Data Analyst position at {company}. As a Microsoft Certified Data Analyst and Data Engineer with nearly four years of experience in BI reporting, ETL processes, and data-driven decision-making, I bring a proven ability to streamline workflows, optimize reporting, and deliver actionable insights.

In my current role at Aptean, I have designed executive dashboards, built centralized data warehouses reducing maintenance efforts by 70%, and automated workflows using Python, cutting manual effort by 80%. My expertise in Power BI, SQL, Azure Data Factory and data modeling, combined with a track record of cost savings and process improvement, makes me confident in my ability to contribute to your team’s success.

I would be glad to discuss how I can add value to {company}.

Best regards,
Bhargav Mallareddi
📞 9553558381
📧 bhargavmallaredddi76@gmail.com
LinkedIn
"""
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach resume
    with open(RESUME_PATH, 'rb') as file:
        part = MIMEApplication(file.read(), Name='Bhargav_Mallareddi_Resume.pdf')
    part['Content-Disposition'] = 'attachment; filename="Bhargav_Mallareddi_Resume.pdf"'
    msg.attach(part)

    return msg

# --- READ CSV AND SEND EMAILS ---
def send_bulk_emails(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(USERNAME, PASSWORD)
        for row in reader:
            recipient_name = row['Name']
            to_email = row['Email']
            company = row['Company']
            msg = create_message(recipient_name, company, to_email)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
            print(f"Sent to {to_email}")
        server.quit()

if __name__ == "__main__":
    # Ensure your CSV has columns: Name, Email, Company
    send_bulk_emails("your csv file path")
    #can you update the code by accessing the terminal errors
