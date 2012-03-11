import operator
from itertools import product

class Rel(object):
    def __init__(self, *tuples):
        self.tuples = list(tuples)


    def __add__(self, tuples):
        return Rel(self.tuples + tuples)


    def __repr__(self):
        return repr(self.tuples)


    def project(self, *attrs):
        just_keys = lambda d: dict((k,v) for k,v in d.iteritems() if k in attrs)
        return Rel(*map(just_keys, self.tuples))


    def rename(self, before, after):
        altered_key = lambda d: dict((k if k != before else after, v)
                                     for k,v in d.iteritems())
        return Rel(*map(altered_key, self.tuples))


    def make_op(self, key, value):
        attr, op = key.split('__')
        return lambda d: getattr(operator, op)(d.get(attr), value)


    def select(self, **operations):
        ops = [self.make_op(k,v) for k,v in operations.iteritems()]
        passes = lambda d: all(op(d) for op in ops)
        return Rel(*filter(passes, self.tuples))


    def natural_join(self, other):
        def tups():
            for first, second in product(self.tuples, other.tuples):
                same = first.viewkeys() & second.viewkeys()
                if same and all(first[k] == second[k] for k in same):
                    d = dict()
                    d.update(first)
                    d.update(second)
                    yield d
        return Rel(*list(tups()))
