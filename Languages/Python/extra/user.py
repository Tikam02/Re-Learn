# user.py

from library import Base


assert hasattr(Base,'foo'), "You broke it fool"

class Derived(Base):
    def bar(self):
        return self.foo()
