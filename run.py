from apps.classic_levenstein import run
import logging as log


log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s')


log.info("Program started")
run()
log.info("Program finished")
