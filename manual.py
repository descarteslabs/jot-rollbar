import jot
from jot.rollbar import RollbarTarget

target = RollbarTarget("803940f4a5dd4df1a57bbe20c1cef9ed")
jot.init(target)

1/0
