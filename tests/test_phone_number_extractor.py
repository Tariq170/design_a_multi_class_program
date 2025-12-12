#Test 1: extracts one number
def test_extracts_one_number():
    d = Diary()
    e1 = DiaryEntry("Day", "Spoke to Sam 07123456789")
    d.add(e1)

extractor = PhoneNumberExtractor()
extractor.extract(d.all()) == ["07123456789"]


#Test 2: extracts multiple numbers
def test_extracts_multiple_numbers():
    e1 = DiaryEntry("A", "Call 07111111111")
    e2 = DiaryEntry("B", "Text 07222222222")

    extractor.extract([e1, e2]) == ["07111111111", "07222222222"]
