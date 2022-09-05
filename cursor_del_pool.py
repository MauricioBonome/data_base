from logger_base import log
from conexion import Conexion

class Cursor_del_pool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del metodo with __enter__")
        self._conexion = Conexion.obtertConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    def __exit__(self, tipo_exepcion, valor_excepcion, datalle_excepcion):
        log.debug("se ejecuta metodo __exit__")
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f"ocurrio una excepcion se hace rollback: {valor_excepcion} {tipo_exepcion}{datalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__=="__main__":
    with Cursor_del_pool() as cursor:
        log.debug("dentro del bloque with")
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())


