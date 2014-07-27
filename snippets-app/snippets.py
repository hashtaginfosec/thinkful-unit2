import logging
import argparse
import csv
import sys
import datetime


#set the log output file, and log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet


def make_parser():
    """
    Construct the commandline parameter
    """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(help="Available commands")

    #subparser for put command
    logging.debug("Constructing put parser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")
    put_parser.set_defaults(command="put")

    return parser


def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    print(command)

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored '{}' as '{}'".format(snippet, name))


if __name__ == "__main__":
    main()