import logging
import logging.config

import module


logging.config.fileConfig('logging.ini')

bar = module.Bar()
bar.bar()

foo = module.Foo()
foo.foo()

logger = logging.getLogger(__name__)
logger.debug("test")

