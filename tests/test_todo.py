#Test 1: initially incomplete
def test_is_incomplete():
    t = Todo("Buy milk")
    t.is_complete() == False


#Test 2: marking complete works
def test_marking_as_complete_works():
    t = Todo("Buy milk")
    t.mark_complete()
    t.is_complete() == True