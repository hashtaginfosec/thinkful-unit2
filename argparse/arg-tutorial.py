import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", nargs="+", help="Creates a local account")
parser.add_argument("-d", "--delete", nargs="+", help="Deletes a local account")

args = parser.parse_args()

if args.add:
    for each_user in args.add:
        print("Creating user " + each_user)
elif args.delete:
    for each_user in args.add:
        print("Deleting user " + each_user)
else:
    parser.print_help()