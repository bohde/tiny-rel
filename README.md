tiny-rel
--------
  A tiny relational algebra implementation for Python

Example
-------
  
   >>> from tiny_rel import rel
   >>> actors = rel({"first": "Jeff", "last": "Bridges},
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
