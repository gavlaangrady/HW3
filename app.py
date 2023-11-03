# Import necessary libraries
from flask import Flask, render_template, jsonify
import psycopg2

# Initialize the Flask app
app = Flask(__name)

# PostgreSQL database connection configuration
db_config = {
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'port': 'your_db_port'
}

# Route for updating basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()

        cursor.close()
        conn.close()

        return "Success!"
    except Exception as e:
        return str(e)

# Route for displaying unique fruits from basket_a and basket_b
@app.route('/api/unique')
def unique_fruits():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Get unique fruits from basket_a
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a")
        basket_a_fruits = [row[0] for row in cursor.fetchall()]

        # Get unique fruits from basket_b
        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b")
        basket_b_fruits = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        # Render an HTML table to display unique fruits
        return render_template('unique_fruits.html', basket_a_fruits=basket_a_fruits, basket_b_fruits=basket_b_fruits)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
