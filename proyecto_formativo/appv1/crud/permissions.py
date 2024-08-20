# Crear un usuario
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

#consultar permisos de un rol por modulo
def get_permissions(db: Session, rol: str, module: str):

    try:
        sql = text("SELECT p_select, p_insert, p_updste, p_delete FROM permissions WHERE rol_name = :rol AND module_name =:module")
        result = db.execute(sql, {"rol":rol, "module":module}).fetchone()
        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario")