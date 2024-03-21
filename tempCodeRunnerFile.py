import PyPDF2

def extract_and_rearrange(pdf_path, output_path):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)

        # Add code to extract data from the wave-like structure and rearrange it
        # For simplicity, let's assume the wave-like data is in a table format

        # Your extraction and rearrangement logic here...

        pdf_writer.addPage(page)

    # Save the modified PDF
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Example usage
pdf_path = 'C:\Users\Akshay Pachpute\Desktop\Clutter\Certified, TL, Hybrid Seed Procurement & Sale Price 3.pdf'
output_path = 'C:Users/Akshay Pachpute/Desktop/Clutter/hi.pdf'
extract_and_rearrange(pdf_path, output_path)
