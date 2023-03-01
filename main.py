import verse.get as bible
import yoda.get as yoda


querystring = {
    "Verse": "1",
    "chapter": "1",
    "Book": "Luke",
}


def main(verse_query: dict[str, str]) -> str:
    verse = bible.get_verse(query=verse_query)
    translated = yoda.translate(verse)
    return translated


if __name__ == "__main__":
    print(main(querystring))
