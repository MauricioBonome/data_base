

from conexion import Conexion
from persona import Persona
from logger_base import log
from cursor_del_pool import Cursor_del_pool



class PersonaDao:
    """
    Dao (data Acces Object
    Crud (Create-Read-Update-Delete)
    """
    _SELECCIONAR ='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR='INSERT INTO persona (nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre =%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
         with Cursor_del_pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls, persona):
        with Cursor_del_pool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona a insertada: {persona}")
            return cursor.rowcount
    @classmethod
    def actualizar (cls, persona):
        with Cursor_del_pool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona Actualizada:{persona}")
            return cursor.rowcount
    @classmethod
    def eliminar (cls,persona):
        with Cursor_del_pool() as cursor:
            valores =(persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"objeto eliminado: {persona}")
            return cursor.rowcount


if __name__ == "__main__":
    # insertar un registro

    # persona1 = Persona(nombre="Alejandra", apellido="Najera", email="p@gmail.com")
    # personas_insertadas = PersonaDao.insertar(persona1)
    # log.debug(f"Personas Insertadas:{personas_insertadas}")

    #actualizar registros

    # persona1 = Persona(13,"Roberto Mauricio", "Bonome","cjjuarez@mail.com")
    # personas_actualizadas = PersonaDao.actualizar(persona1)
    # log.debug(F"personas actualizadas {personas_actualizadas}")

    #eliminar un registro

    # persona1 = Persona(id_persona=33)
    # personas_eliminadas = PersonaDao.eliminar(persona1)
    # log.debug(f"Personas elimanadas : {personas_eliminadas}")
    # seleccionar un registro
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
