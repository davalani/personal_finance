from sqlalchemy import Column, String, Boolean, ForeignKey
from models.base_class import Base
from sqlalchemy.orm import relationship

class Permission(Base):
    __tablename__ = 'permissions'
    role_name = Column(String(15), ForeignKey('roles.rol_name') , primary_key=True)
    module_name = Column(String(15), ForeignKey('modules.module_name') , primary_key=True)
    p_select = Column(Boolean, default=True)
    p_insert = Column(Boolean, default=True)
    p_update = Column(Boolean, default=True)
    p_delete = Column(Boolean, default=True)

    role = relationship("Role") #Define una relación con el modelo role
    module = relationship("Module")#Define una relación con el modelo module
