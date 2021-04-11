import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG) # 对logging级别进行设置
logger=logging.getLogger(__name__)

logger.info('Start reading database')
res={'join':55,'tom':66}
logger.debug('Records:%s'%res)
logger.info('update:')
logger.info('finish update')