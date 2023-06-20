import logging

# config the loggin settings within the blueprint
bp_logger = logging.getLogger('blueprint_name')
bp_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s')


# Add a logging handler to specity where the log messages should be written
file_handler = logging.FileHandler('blueprint.log')
file_handler.setFormatter(formatter)
bp_logger.addHandler(file_handler)


# Start using logging statements within your blueprint code
bp_logger.info('Log message')
bp_logger.warning('Watch out!')
bp_logger.error('Error message')
