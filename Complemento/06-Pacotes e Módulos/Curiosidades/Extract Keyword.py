from flashtext import KeywordProcessor

doc = """
    Hello, there. I'm the better python programmer in this world.
    Anything more, you can send me an email.
"""

p = KeywordProcessor()
p.add_keyword('email')
found = p.extract_keywords(doc)
print("Result: ", found)

p = KeywordProcessor(case_sensitive=False)
p.add_keyword('email', 'message')
found = p.replace_keywords(doc)
print(found)
