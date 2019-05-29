import logging

class Bar:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')


class Foo:
	def __init__(self):
	    self.logger = logging.getLogger("{0}.Foo".format(__name__))

	def foo(self):
	    self.logger.info('Hi, foo')