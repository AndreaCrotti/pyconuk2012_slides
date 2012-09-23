from tempfile import mktemp
from os import remove

class TempFile:
    """Create a temporary file with the given content and remove it on exit
    """
    def __init__(self, content=None):
        self.content = content or ""
        self.temp_file = mktemp()

    def __enter__(self):
        with open(self.temp_file, 'w') as wr:
            wr.write(self.content)

        return self.temp_file

    def __exit__(self, type, value, traceback):
        remove(self.temp_file)


def with_context_manager():
    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print "<%s>" % name
        yield
        print "</%s>" % name
