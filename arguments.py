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
    )

    parser.add_argument(
        '-i',
        '--input',
        dest='input_file',
        metavar='<filename>',
        help='the input pdf file to take pages from',
        type=str,
    )

    parser.add_argument(
        '-p',
        '--page',
        dest='page_indexes',
        metavar='<page_index>',
        help='index of pages to append to output file',
        type=int,
        nargs='*',
    )

    parser.add_argument(
        '-c',
        '--create',
        dest='create',
        help='create (or override) a pdf file with name of the output file',
        action='store_true',
    )

    parser.add_argument(
        '-r',
        '--remove',
        dest='remove',
        help='remove pages from input pdf file',
        action='store_true',
    )

    validate_arguments(parser)

    return parser.parse_args()


def validate_arguments(parser: ArgumentParser) -> None:
    """Validate arguments"""
    args = parser.parse_args()

    if args.remove:
        if not args.input_file or not args.page_indexes:
            parser.error("When using --remove, then --input and --page is required")
    elif args.create:
        if not args.output_file:
            parser.error("When using --create, then --output is required")
    else:
        if args.output_file:
            if not args.input_file or not args.page_indexes:
                parser.error("When using --output, then both --input and --page is required")
