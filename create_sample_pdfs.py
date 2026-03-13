import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Ensure documents folder exists
os.makedirs("documents", exist_ok=True)

styles = getSampleStyleSheet()

docs = {
    "HR_policy.pdf": [
        "HR Policy Document",
        "Working Hours: Employees are expected to work 9 hours per day including a 1 hour break.",
        "Code of Conduct: Employees must maintain professional behaviour in the workplace.",
        "Remote Work: Employees can work remotely with manager approval.",
        "Equal Opportunity: The company provides equal employment opportunities."
    ],

    "Leave_policy.pdf": [
        "Leave Policy",
        "Annual Leave: Employees are entitled to 20 days of paid leave per year.",
        "Sick Leave: Employees can take up to 10 days of sick leave annually.",
        "Maternity Leave: Eligible employees can take 26 weeks of maternity leave.",
        "Emergency Leave: Up to 5 days of emergency leave may be granted."
    ],

    "Employee_handbook.pdf": [
        "Employee Handbook",
        "Welcome to the company handbook.",
        "Dress Code: Employees should maintain a professional appearance.",
        "Communication: All official communication should happen through company email.",
        "Performance Reviews: Employees receive performance evaluations twice a year."
    ]
}

for name, content in docs.items():

    story = []

    for line in content:
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    pdf = SimpleDocTemplate(f"documents/{name}")
    pdf.build(story)

print("PDF files created successfully!")