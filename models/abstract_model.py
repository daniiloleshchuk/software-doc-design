from db import Base, Session


class AbstractModel(Base):
    __abstract__ = True

    def save(self, session=None):
        session.add(self)
        session.commit()

    @classmethod
    def get_by_pk(cls, pk, session=None):
        session = Session() if not session else session
        return session.query(cls).filter_by(pk=pk).first()
