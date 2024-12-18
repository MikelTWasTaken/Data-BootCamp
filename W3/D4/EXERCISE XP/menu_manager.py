import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        """Retrieve a single item by name."""
        with psycopg2.connect(database="restaurant_menu", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
                result = cur.fetchone()
                return result if result else None

    @classmethod
    def all_items(cls):
        """Retrieve all items from the Menu_Items table."""
        with psycopg2.connect(database="restaurant_menu", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Menu_Items")
                return cur.fetchall()