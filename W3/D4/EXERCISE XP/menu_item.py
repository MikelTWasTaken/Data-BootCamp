import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        """Insert item into the Menu_Items table."""
        with psycopg2.connect(database="restaurant_menu", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                    (self.name, self.price),
                )
                conn.commit()

    def delete(self):
        """Delete item from the Menu_Items table."""
        with psycopg2.connect(database="restaurant_menu", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM Menu_Items WHERE item_name = %s",
                    (self.name,),
                )
                conn.commit()

    def update(self, new_name, new_price):
        """Update the name and price of the item."""
        with psycopg2.connect(database="restaurant_menu", user="postgres", password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                    (new_name, new_price, self.name),
                )
                conn.commit()