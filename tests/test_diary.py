from lib.diary import Diary
from lib.diary_entry import DiaryEntry

'''#Test 1: adds and retrieves entries
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

    assert d.entries_readable(2, 1) == [e1]'''


def test_diary_returns_phone_numbers():
    d = Diary()
    d.add(DiaryEntry("A", "text", "07123456789"))
    d.add(DiaryEntry("B", "text2"))
    d.add(DiaryEntry("C", "text3", "07987654321"))

    assert d.all_phone_numbers() == ["07123456789", "07987654321"]
