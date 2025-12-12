#Test 1: formats correctly

def test_format_correctly():

    entry = DiaryEntry("Monday", "Went to school")
    entry.format() == "Monday: Went to school"


#Test 2: counts words
def test_count_words():
    entry = DiaryEntry("A", "one two three")
    entry.count_words() == 3


#Test 3: calculates reading time
def test_calculates_reading_time():
    entry = DiaryEntry("A", "one two three four")
    entry.reading_time(2) == 2   # 4 words at 2wpm


#Test 4: checks if readable in time
def test_checks_if_readable_in_time():
    entry = DiaryEntry("A", "one two three four five")
    entry.readable_in(5, 1) == True
    entry.readable_in(2, 1) == False
