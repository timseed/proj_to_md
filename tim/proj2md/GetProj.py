import argparse
from datetime import datetime, timedelta
from os import path


def file_exists(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x


def dir_exists(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not path.isdir(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} is not a valid directory".format(x))
    return x


def valid_date(s):
    try:
        val_date = datetime.strptime(s, "%Y-%m-%d")
        if val_date - datetime.now() > timedelta(days=15):
            msg = "Date {0} too far in the future".format(s)
            raise argparse.ArgumentTypeError(msg)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def valid_string(s):
    try:
        return s.lower().strip()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def valid_TF(s):
    try:
        if s in [True, False]:
            return s
    except ValueError:
        msg = "Not a valid Boolean: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def get_arguments():
    parser = argparse.ArgumentParser(description="Project to md")
    parser.add_argument(
        "-d",
        "--directory",
        dest="dir",
        required=True,
        metavar="Directory",
        type=dir_exists,
        help="Project directory",
    )
    parser.add_argument(
        "-t",
        "--types",
        action="append",
        dest="file_types",
        help="Output only file types [py] default. Use multiple -t to add more file types",
        required=False,
        default=["py"]
    )
    args = parser.parse_args()
    return args
