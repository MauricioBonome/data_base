from logger_base import log
import sys
from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Maturano321'
    _DB_PORT ='5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user = cls._USERNAME,
                                                      password= cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE
                                                )
                log.debug(F"creacion del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"ocurrio un error al obtener el pool{e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtertConexion(cls):
        conexion = cls.obtenerPool().getconn() # es para solicitar un solo usuario de conexion
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion) #regresar el objeto de coneccion si el usuario ya no lo esta utilizando
        log.debug(f"regresamos la conexion al pool: {conexion}")

    @classmethod
    def cerrarConecciones(cls):
        cls.obtenerPool().closeall()


if __name__=="__main__":
        conexion1= Conexion.obtertConexion()
        Conexion.liberarConexion(conexion1)
        conexion2 = Conexion.obtertConexion()
        conexion3 = Conexion.obtertConexion()
        Conexion.liberarConexion(conexion3)
        conexion4 = Conexion.obtertConexion()
        conexion5 = Conexion.obtertConexion()
        Conexion.liberarConexion(conexion5)
