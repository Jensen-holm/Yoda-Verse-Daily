from verse.get import get_verse


def main():
    querystring = {"Verse": "1", "chapter": "1", "Book": "Luke"}
    return get_verse(qs=querystring)


if __name__ == "__main__":
    print(main())
