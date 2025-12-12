
#Test 1: adds tasks
def test_adds_task():
    tl = TodoList()
    t = Todo("Buy milk")
    tl.add(t)
    tl.incomplete() == [t]


#Test 2: separates complete and incomplete
def test_seperates_complete_and_incomplete_tasks():
    t1 = Todo("A")
    t2 = Todo("B")
    t2.mark_complete()

    tl = TodoList()
    tl.add(t1)
    tl.add(t2)

    tl.incomplete() == [t1]
    tl.complete() == [t2]