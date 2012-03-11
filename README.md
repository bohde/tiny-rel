tiny-rel
--------
  A tiny relational algebra implementation for Python

Example
-------
    >>> from tiny_rel import Rel
    >>> actors = Rel({"first": "Jeff", "last": "Bridges"},
                     {"first": "John", "last": "Goodman"},
                     {"first": "Steve", "last": "Buscemi"})
    >>> actors += [{"first": "Juliane", "last": "Moore"}]

    >>> actors.project('last')
        [{"last": "Bridges"},
         {"last": "Goodman"},
         {"last": "Buscemi"},
         {"last": "Moore"}]

    >>> actors.select(last__gt="Goldblum")
        [{"first": "John", "last": "Goodman"},
         {"first": "Juliane", "last": "Moore"}]

    >>> actors.rename('first', 'lololol')
        [{"lololol": "Jeff", "last": "Bridges},
         {"lololol": "John", "last": "Goodman"},
         {"lololol": "Steve", "last": "Buscemi"},
         {"lololol": "Juliane", "last": "Moore"}]

    >>> movies = Rel({'title': 'The Big Lebowski',
                      'year': 1997},
                     {'title', "Dr Seuss' The Lorax",
                      'year': 2012})

    >>> seen = Rel({'name': 'Josh', 
                    'title', 'The Big Lebowski'},
                   {'name': 'Josh',
                    'title': 'The Importance of Being Earnest'},
                   {'name': 'Alice',
                    'title': 'The Big Lebowski'},
                   {'name': 'Alice',
                    'title': "Dr Seuss' The Lorax"})

    >>> years_seen = movies.natural_join(seen).project('name', 'year')
        [{'name': 'Josh',
          'year': 1997},
         {'name': 'Alice',
          'year': 1997},
         {'name': 'Alice',
          'year': 2012}]
