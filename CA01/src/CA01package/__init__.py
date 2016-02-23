from StarCatalog import StarCatalog
import time

catalog = StarCatalog()

catalog.loadCatalog("sao.txt",9.0)

catalog.emptyCatalog()

time.sleep(5)