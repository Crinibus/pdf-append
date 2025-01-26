from typing import List
from pypdf import PdfReader, PdfWriter
from arguments import argparse_setup


def create_pdf(filename: str):
    pdf_writer = PdfWriter()
    with open(filename, "wb") as file:
        pdf_writer.write(file)


def append_pages_to_pdf(page_indexes: List[int], input_pdf_name: str, output_pdf_name: str):
    pdf_writer = get_all_pages(output_pdf_name)

    pdf = PdfReader(input_pdf_name)

    for index in page_indexes:
        pdf_writer.add_page(pdf.get_page(index - 1))

    write_pdf(output_pdf_name, pdf_writer)

    print(f"Appended page(s) from {input_pdf_name} to {output_pdf_name}")


def remove_pages_from_pdf(page_indexes: List[int], pdf_name: str):
    pdf = PdfReader(pdf_name)

    pdf_writer = PdfWriter()

    for index in range(pdf.get_num_pages()):
        if index + 1 not in page_indexes:
            pdf_writer.add_page(pdf.get_page(index))

    write_pdf(pdf_name, pdf_writer)

    print(f"Removed page(s) from {pdf_name}")


def duplicate_pdf(input_pdf_name: str, output_pdf_name: str = ""):
    pdf = PdfReader(input_pdf_name)

    pdf_writer = PdfWriter()

    for index in range(pdf.get_num_pages()):
        pdf_writer.add_page(pdf.get_page(index))

    if output_pdf_name == "":
        input_basename = input_pdf_name.split(".pdf")[0]
        output_pdf_name = f"{input_basename}(1).pdf"

    write_pdf(output_pdf_name, pdf_writer)

    print(f"Duplicated {input_pdf_name}")


def get_all_pages(pdf_name: str) -> PdfWriter:
    pdf = PdfReader(pdf_name)

    pdf_writer = PdfWriter()
    for page in range(pdf.get_num_pages()):
        pdf_writer.add_page(pdf.get_page(page))

    return pdf_writer


def write_pdf(filename: str, pdf_writer: PdfWriter):
    with open(filename, "wb") as out_pdf:
        pdf_writer.write(out_pdf)


if __name__ == "__main__":
    args = argparse_setup()

    if args.create:
        create_pdf(args.output_file)
    if args.remove:
        remove_pages_from_pdf(args.page_indexes, args.input_file)
    if args.duplicate:
        duplicate_pdf(args.input_file, args.output_file)
    if args.append:
        append_pages_to_pdf(args.page_indexes, args.input_file, args.output_file)
