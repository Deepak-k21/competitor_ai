from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Spacer
from reportlab.lib import colors

def create_pdf(report_text, filename="competitor_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []
    
    elements.append(Paragraph(report_text, styles["Normal"]))
    elements.append(Spacer(1, 12))
    
    doc.build(elements)
    return filename