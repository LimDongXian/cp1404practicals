"""
programming language
Estimate: 30 minutes
Actual:   40 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

for language in languages:
    if ProgrammingLanguage.is_dynamic(language):
        print(language.name)
