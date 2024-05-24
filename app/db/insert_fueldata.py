import psycopg2

from app.db.config.config import load_config


def insert_fuellog(log):
    """Insert a new vendor into the vendors table"""

    sql = "INSERT INTO log(odometer, liter, price) VALUES(%s, %s, %s);"

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(
                    sql,
                    (
                        log["odometer"],
                        log["liter"],
                        log["price"],
                    ),
                )

                # commit the changes to the database
                conn.commit()

                return "Everything's good!!"
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    insert_fuellog()
