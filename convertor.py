import csv

def pdf_to_csv(pdf_file, csv_file):
    with open(pdf_file, 'rb') as file:
        from llama_core.pdf import PdfReader
        reader = PdfReader(file)
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    lines = text.split('\n')
                    for line in lines:
                        writer.writerow(line.split())

pdf_to_csv('input.pdf', 'output.csv')
