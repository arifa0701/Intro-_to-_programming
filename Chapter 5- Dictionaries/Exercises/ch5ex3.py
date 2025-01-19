#new project
glossary = {
    'string': 'A series of charcters',
    'comment': 'A program that python interpeter ignores',
    'list': 'Collection of items in an order',
    'loop': 'Work through a collection of items, one at a time',
    'dictionary': 'Collection of key value pairs',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")