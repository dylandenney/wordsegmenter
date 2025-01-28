from my_word_segmenter.segmenter import dp_segment, to_pascal_case

def test_dp_segment():
    assert dp_segment("testtablename") == ["test", "table", "name"]
    assert dp_segment("userprofile") == ["user", "profile"]

def test_to_pascal_case():
    assert to_pascal_case(["test", "table", "name"]) == "TestTableName"
