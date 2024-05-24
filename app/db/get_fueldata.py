import psycopg2

from app.db.config.config import load_config


def get_fuellogs():
    """Retrieve data from the log table"""
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT timestamp, odometer, liter, price FROM log ORDER BY timestamp"
                )
                rows = cur.fetchall()

                log_list = []
                for row in rows:
                    log_dict = dict()
                    log_dict["timestamp"] = row[0]
                    log_dict["odometer"] = row[1]
                    log_dict["liter"] = row[2]
                    log_dict["price"] = row[3]

                    log_list.append(log_dict)

            return log_list

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    get_fuellogs()
