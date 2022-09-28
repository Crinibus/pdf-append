from argparse import ArgumentParser


def argparse_setup() -> ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = ArgumentParser()

    parser.add_argument(
        "-o",
        "--output",
        dest="output_file",
        metavar="<filename>",
        help="the output pdf file to create or append pages to",
        type=str,
        default="",
    )

    parser.add_argument(
        "-i",
        "--input",
        dest="input_file",
        metavar="<filename>",
        help="the input pdf file to take pages from",
        type=str,
    )

    parser.add_argument(
        "-p",
        "--page",
        dest="page_indexes",
        metavar="<page_index>",
        help="index of pages to append to output file",
        type=int,
        nargs="*",
    )

    parser.add_argument(
        "-c",
        "--create",
        dest="create",
        help="create (or override) a pdf file with name of the output file",
        action="store_true",
    )

    parser.add_argument(
        "-a",
        "--append",
        dest="append",
        help="append pages from input pdf file to output file",
        action="store_true",
    )

    parser.add_argument(
        "-r",
        "--remove",
        dest="remove",
        help="remove pages from input pdf file",
        action="store_true",
    )

    parser.add_argument(
        "-d",
        "--duplicate",
        dest="duplicate",
        help="duplicate input pdf file",
        action="store_true",
    )

    validate_arguments(parser)

    return parser.parse_args()


def validate_arguments(parser: ArgumentParser) -> None:
    """Validate arguments"""
    args = parser.parse_args()

    if args.remove:
        if args.create or args.duplicate:
            parser.error("When using --remove, then either --create or --duplicate can't be used")
        elif not args.input_file or not args.page_indexes:
            parser.error("When using --remove, then --input and --page is required")
    elif args.create:
        if args.remove or args.duplicate:
            parser.error("When using --create, then either --remove or --duplicate can't be used")
        elif not args.output_file:
            parser.error("When using --create, then --output is required")
    elif args.duplicate:
        if args.create or args.remove:
            parser.error("When using --duplicate, then either --create or --remove can't be used")
        elif not args.input_file:
            parser.error("When using --duplicate, then --input is required")
    else:
        if args.output_file:
            if not args.input_file or not args.page_indexes:
                parser.error("When using --output, then both --input and --page is required")
