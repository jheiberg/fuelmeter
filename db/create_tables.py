import psycopg2

from db.config import load_config


def create_tables():
    """Create tables in the PostgreSQL database"""
    commands = [
        "CREATE TABLE log (timestamp TIMESTAMP PRIMARY KEY DEFAULT NOW(), odometer INTEGER NOT NULL, liter FLOAT NOT NULL, price FLOAT NOT NULL)"
    ]
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    create_tables()
