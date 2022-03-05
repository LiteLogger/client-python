import logging
from LiteLogger import LiteLoggerHandler

log = logging.getLogger(__name__)

API_KEY = 'your_api_key'
STREAM_NAME = 'Your Log Stream Name'

# create the LiteLogger Handler
llhandler = LiteLoggerHandler(
	STREAM_NAME,
	API_KEY,
)

# add handler to logger
log.addHandler(llhandler)

log.info('Some Log Message!', extra={
	'metadata': {'some_important_key': 'that keys value'},
	'tags': ['some tag', 'another tag']
})