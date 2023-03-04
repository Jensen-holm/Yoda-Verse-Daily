from preach.preach import preach, center_multiline_output
import sys


def main():
    """
    Takes one command line argument
    which is the person you want the
    bible verse to be said by
    :return: prints the output from the api
    """
    person = sys.argv[1]
    center_multiline_output(
        preach(person=person)
    )


if __name__ == "__main__":
    main()
