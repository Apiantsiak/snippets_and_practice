def attrdecorator(func):
    def fun(s, *args):
        class d:
            def __getattr__(s2, name):
                return func(s, *args, name)

        return d()

    return fun


class Thing(object):
    def __init__(self, name):
        self.name = name
        self.each = self

    @property
    @attrdecorator
    def is_a(self, obj):
        setattr(self, 'is_a_' + obj, True)

    @property
    @attrdecorator
    def is_not_a(self, obj):
        setattr(self, 'is_a_' + obj, False)

    @property
    @attrdecorator
    @attrdecorator
    def is_the(self, name1, name2):
        setattr(self, name1, name2)
        return self

    @attrdecorator
    def has(self, num, name):
        singular = name[:-1] if num > 1 else name
        thing = Thing(singular)
        setattr(thing, 'is_' + singular, True)
        obj = (thing,) * num if num > 1 else thing
        setattr(self, name, obj)
        return thing

    @property
    @attrdecorator
    def can(self, verb):
        def d(fnc, past=None):
            if past:
                setattr(self, past, [])

            def f(*args):
                global name
                name = self.name
                val = fnc(*args)
                if past:
                    getattr(self, past).append(val)
                return val

            setattr(self, verb, f)

        return d

    having = has
    being_the = is_the
    and_the = is_the
