from threading import Event

class Foo:
    def __init__(self):
        self.event1, self.event2 = Event(), Event()

    def first(self, f):
        f()
        self.event1.set()

    def second(self, f):
        self.event1.wait()
        f()
        self.event2.set()

    def third(self, f):
        self.event2.wait()
        f()