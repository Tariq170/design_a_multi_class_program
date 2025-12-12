class DiaryEntry:

    def __init__(self, title, contents, phone_number=None):
        # title: string
        # contents: string
        self.title= title
        self.contents = contents
        self.phone_number = phone_number

    def format(self):
        return f"{self.title}: {self.contents}, phone_number:{self.phone_number if self.phone_number else "N/A"}"
    # returns "title: contents"

    def count_words(self):
        return len(self.contents.split())

    # returns number of words in the entry


    def reading_time(self, wpm):
        if wpm <= 0:
            raise ValueError("wpm must be positive")
        return -(-self.count_words() // wpm)
    # wpm: positive int
    # returns estimated minutes to read the entry

    def readable_in(self, wpm, minutes):
        return self.reading_time(wpm) <= minutes
    # returns True if entry can be read fully within the given minutes