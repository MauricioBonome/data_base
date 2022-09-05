import logging as log


log.basicConfig(level= log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()

                ])

if __name__ == "__main__":
    log.debug("mensaje a nivel debug")
    log.info("mensaje a nive info")
    log.warning("mensaje warning")
    log.error("error")
    log.critical("mensaje critico")