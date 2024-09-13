from sqlalchemy import String, Integer, Column, TIMESTAMP, text, ForeignKey
from .database import Base

class Curso_Aluno(Base):
    __tablename__ = 'curso_aluno'

    id_aluno = Column(Integer, ForeignKey('alunos.id'), autoincrement=True)
    id_curso = Column(Integer,ForeignKey('curso.id'),nullable=False)
    