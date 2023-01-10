from sqlalchemy import create_engine, text


class DataBase:
    def __init__(self,
                 db_name='postgres',
                 db_user='postgres',
                 db_pass='postgres',
                 db_host='db',
                 db_port='5444'):
        db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
        self.engine = create_engine(db_string)

    def query(self, query_text):
        with self.engine.begin() as conn:
            return conn.execute(text(query_text))

    def insert_user(self,
                    name=None,
                    nickname=None,
                    age=None,
                    sex=None,
                    cp=None,
                    trtbps=None,
                    chol=None,
                    fbs=None,
                    restecg=None,
                    thalachh=None,
                    exng=None,
                    oldpeak=None,
                    slp=None,
                    caa=None):
        query = text("""
        WITH req_1 AS (
            INSERT INTO users(name, nickname, age, sex)
            VALUES (:name, :nickname, :age, :sex)
            RETURNING users.id AS user_id
        )
        INSERT INTO heart_attack(user_id, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa)
        SELECT req_1.user_id, :cp ,:trtbps, :chol, :fbs, :restecg, :thalachh, :exng, :oldpeak, :slp, :caa
        FROM req_1
        ;
        """)
        args = [name, nickname, age, sex, cp, trtbps, chol,
                fbs, restecg, thalachh, exng, oldpeak, slp, caa]
        keys = ['name', 'nickname', 'age', 'sex', 'cp', 'trtbps', 'chol',
                'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa']
        kwargs = {k: v for k, v in zip(keys, args)}

        with self.engine.begin() as conn:
            conn.execute(query, kwargs)


if __name__ == '__main__':
    data_base = DataBase(db_host='localhost')
    data_base.insert_user(name="Sasha")
    print(data_base.query('SELECT * FROM users  u INNER JOIN heart_attack h ON u.id = h.user_id').all())
