from lib.todo import Todo
from lib.todo_list import TodoList

#Test 1: adds tasks
def test_adds_task():
    tl = TodoList()
    t = Todo("Buy milk")
    tl.add(t)
    assert tl.incomplete() == [t]


#Test 2: separates complete and incomplete
def test_seperates_complete_and_incomplete_tasks():
    t1 = Todo("A")
    t2 = Todo("B")
    t2.mark_complete()

    tl = TodoList()
    tl.add(t1)
    tl.add(t2)

    assert tl.incomplete() == [t1]
    assert tl.complete() == [t2]