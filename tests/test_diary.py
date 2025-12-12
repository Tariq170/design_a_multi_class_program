from lib.diary import Diary
from lib.diary_entry import DiaryEntry

#Test 1: adds and retrieves entries
def test_add_plus_retrieve_entries():
    d = Diary()
    e = DiaryEntry("A", "Hello")
    d.add(e)
    assert d.all() == [e]


#Test 2: filters readable entries
def test_filters_readable_entries():
    d = Diary()
    e1 = DiaryEntry("Short", "one two")
    e2 = DiaryEntry("Long", "one two three four five six")

    d.add(e1)
    d.add(e2)

    assert d.entries_readable(2, 1) == [e1]