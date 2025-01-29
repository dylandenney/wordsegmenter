from dylanswordsegmenter import dp_segment_with_longest_match, to_pascal_case

def test_dp_segment():
    assert dp_segment_with_longest_match("testtablename") == ["test", "table", "name"]
    assert dp_segment_with_longest_match("userprofile") == ["user", "profile"]

def test_to_pascal_case():
    assert to_pascal_case(["test", "table", "name"]) == "TestTableName"
    assert to_pascal_case(["user", "profile"]) == "UserProfile"
    assert to_pascal_case(["bass", "head"]) == "BassHead"
