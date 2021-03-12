from typing import List
from PyPDF2 import PdfFileReader, PdfFileWriter
from arguments import argparse_setup


def create_pdf(filename: str):
    pdf_writer = PdfFileWriter()
    with open(filename, "wb") as file:
        pdf_writer.write(file)


def add_page_to_pdf(page_index: int, input_pdf_name: str, output_pdf_name: str):
    pdf_writer = PdfFileWriter()

    pdf = PdfFileReader(input_pdf_name)

    pdf_writer.addPage(pdf.getPage(page_index-1))

    write_pdf(output_pdf_name, pdf_writer)

    print(f"Added page {page_index} from pdf {input_pdf_name} to pdf {output_pdf_name}")


def append_pages_to_pdf(page_indexes: List[int], input_pdf_name: str, output_pdf_name: str):
    pdf_writer = get_all_pages(output_pdf_name)

    pdf = PdfFileReader(input_pdf_name)

    for index in page_indexes:
        pdf_writer.addPage(pdf.getPage(index-1))

    write_pdf(output_pdf_name, pdf_writer)

    print(f"Appended page(s) from {input_pdf_name} to {output_pdf_name}")


def remove_pages_from_pdf(page_indexes: List[int], pdf_name: str):
    pdf = PdfFileReader(pdf_name)

    pdf_writer = PdfFileWriter()

    for index in range(pdf.getNumPages()):
        if index+1 not in page_indexes:
            pdf_writer.addPage(pdf.getPage(index))
    
    write_pdf(pdf_name, pdf_writer)

    print(f"Removed page(s) from {pdf_name}")


def get_all_pages(pdf_name: str) -> PdfFileWriter:
    pdf = PdfFileReader(pdf_name)

    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    
    return pdf_writer


def write_pdf(filename: str, pdf_writer: PdfFileWriter):
    with open(filename, "wb") as out_pdf:
        pdf_writer.write(out_pdf)


if __name__ == "__main__":
    args = argparse_setup()

    if args.create:
        create_pdf(args.output_file)

    if args.remove:
        remove_pages_from_pdf(args.page_indexes, args.input_file)
    else:
        append_pages_to_pdf(args.page_indexes, args.input_file, args.output_file)
