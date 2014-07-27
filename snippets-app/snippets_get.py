import logging
import argparse
import csv
import sys
import time


#set the log output file, and log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info(time.strftime("%c") + " Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug(time.strftime("%c") + " Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug(time.strftime("%c") + " Write successful")
    f.close()
    return name, snippet


#Read from csv file and return snippet
def get(name, filename):
    logging.info(time.strftime("%c") + " Reading {} from {}".format(name, filename))
    print(time.strftime("%c") + " Reading {} from {}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, "r+") as f:
        #create a dictionary from csv reader
        dict_snippets = dict(filter(None, csv.reader(f)))

    if name in dict_snippets:
        print("name : " + dict_snippets[name])
    else:
        print(name + " not in given csv file.")

    f.close()

    return None



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

    logging.debug("Constructing get parser")
    get_parser = subparsers.add_parser("get", help="Get a snippet")
    get_parser.add_argument("name", help="The name of the snippet we want to get")
    get_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippets file name")
    get_parser.set_defaults(command="get")

    return parser


def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored '{}' as '{}'".format(snippet, name))

    elif command == "get":
        name = arguments.pop("name")
        filename = arguments.pop("filename")
        get(name, filename)



if __name__ == "__main__":
    main()
