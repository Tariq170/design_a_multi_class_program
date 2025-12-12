1.Problem

Record diary entries

Read past diary entries

Select entries to read based on time and reading speed

Keep a todo list

Extract all mobile phone numbers contained in diary entries



2.Classes
Class: DiaryEntry

Represents one diary entry.

Methods
__init__(self, title, contents)
# title: string
# contents: string

format()
# returns "title: contents"

count_words()
# returns number of words in the entry

reading_time(wpm)
# wpm: positive int
# returns estimated minutes to read the entry

readable_in(wpm, minutes)
# returns True if entry can be read fully within the given minutes



Class: Diary

Stores multiple DiaryEntry objects.

Methods
add(entry)
# entry: instance of DiaryEntry

all()
# returns a list of entries

entries_readable(wpm, minutes)
# returns a list of entries that can be fully read
# within the given time and reading speed



Class: Todo

Represents a single task.

Methods
__init__(self, task)
# task: string
# initially incomplete

mark_complete()
# marks the task as complete

is_complete()
# returns True/False



Class: TodoList

Stores many Todo objects.

Methods
add(todo)
# todo: instance of Todo

incomplete()
# returns list of tasks not completed

complete()
# returns list of tasks completed




Class: PhoneNumberExtractor

Extracts phone numbers from diary entries.

Methods
extract(diary_entries)
# diary_entries: list of DiaryEntry
# returns list of phone numbers found (format: 07XXXXXXXXX)





3.Tests
### Tests for DiaryEntry

Test 1: formats correctly

entry = DiaryEntry("Monday", "Went to school")
entry.format() == "Monday: Went to school"


Test 2: counts words

entry = DiaryEntry("A", "one two three")
entry.count_words() == 3


Test 3: calculates reading time

entry = DiaryEntry("A", "one two three four")
entry.reading_time(2) == 2   # 4 words at 2wpm


Test 4: checks if readable in time

entry = DiaryEntry("A", "one two three four five")
entry.readable_in(5, 1) == True
entry.readable_in(2, 1) == False

### Tests for Diary

Test 1: adds and retrieves entries

d = Diary()
e = DiaryEntry("A", "Hello")
d.add(e)
d.all() == [e]


Test 2: filters readable entries

d = Diary()
e1 = DiaryEntry("Short", "one two")
e2 = DiaryEntry("Long", "one two three four five six")

d.add(e1)
d.add(e2)

d.entries_readable(2, 1) == [e1]

### Tests for Todo

Test 1: initially incomplete

t = Todo("Buy milk")
t.is_complete() == False


Test 2: marking complete works

t = Todo("Buy milk")
t.mark_complete()
t.is_complete() == True

### Tests for TodoList

Test 1: adds tasks

tl = TodoList()
t = Todo("Buy milk")
tl.add(t)
tl.incomplete() == [t]


Test 2: separates complete and incomplete

t1 = Todo("A")
t2 = Todo("B")
t2.mark_complete()

tl = TodoList()
tl.add(t1)
tl.add(t2)

tl.incomplete() == [t1]
tl.complete() == [t2]

### Tests for PhoneNumberExtractor

Test 1: extracts one number

d = Diary()
e1 = DiaryEntry("Day", "Spoke to Sam 07123456789")
d.add(e1)

extractor = PhoneNumberExtractor()
extractor.extract(d.all()) == ["07123456789"]


Test 2: extracts multiple numbers

e1 = DiaryEntry("A", "Call 07111111111")
e2 = DiaryEntry("B", "Text 07222222222")

extractor.extract([e1, e2]) == ["07111111111", "07222222222"]
