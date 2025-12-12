from lib.todo import Todo

#Test 1: initially incomplete
def test_is_incomplete():
    t = Todo("Buy milk")
    assert t.complete() == False


#Test 2: marking complete works
def test_marking_as_complete_works():
    t = Todo("Buy milk")
    t.mark_complete()
    assert t.complete() == True