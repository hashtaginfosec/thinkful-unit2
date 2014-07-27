import logging
import argparse
import csv
import sys


#set the log output file, and log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """Store a snippet with an associated name in the CSV file"""
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file ".format(name, snippet))
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

    return parser


def main():
    """
    Main function
    """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])


if __name__ == "__main__":
    main()