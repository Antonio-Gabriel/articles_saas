from ..database.postgres import DbConnectionHandler


class DbConnectionFactory:
    """factory of connection"""

    @classmethod
    def create(cls):
        """create connection factory object"""
        return DbConnectionHandler().get_session()
