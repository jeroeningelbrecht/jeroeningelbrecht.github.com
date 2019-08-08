def string_interning():
    s1 = 'hello world'
    s2 = 'hello world'
    assert s1 is s2


string_interning()
