import csv
import pdfkit

class ReportGenerator:
    @staticmethod
    def export_to_csv(data, filename):
        # Expects data as a list of dictionaries
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    @staticmethod
    def export_to_pdf(html_content, filename):
        # Convert HTML content to a PDF file
        pdfkit.from_string(html_content, filename)