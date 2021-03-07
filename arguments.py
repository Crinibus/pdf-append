from argparse import ArgumentParser


def argparse_setup() -> ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = ArgumentParser()

    parser.add_argument(
        '-o',
        '--output',
        dest='output_file',
        metavar='<filename>',
        help='the output pdf file to create or append pages to',
        type=str,
        required=True,
    )

    parser.add_argument(
        '-i',
        '--input',
        dest='input_file',
        metavar='<filename>',
        help='the input pdf file to take pages from',
        type=str,
        required=True,
    )

    parser.add_argument(
        '-p',
        '--page',
        dest='page_index',
        metavar='<page_index>',
        help='index of pages to append to output file',
        type=int,
        required=True,
        nargs='*',
    )

    parser.add_argument(
        '-c',
        '--create',
        dest='create',
        help='create (or override) a pdf file with name of the output file',
        action='store_true',
    )

    return parser.parse_args()
