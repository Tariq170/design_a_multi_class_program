class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
    # entry: instance of DiaryEntry

    def all(self):
        return self.entries
    # returns a list of entries

    def entries_readable(self, wpm, minutes):
        result = []
        for entry in self.entries:
            if entry.readable_in(wpm, minutes):
                result.append(entry)
        return result        
    # returns a list of entries that can be fully read
    # within the given time and reading speed

