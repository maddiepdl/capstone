from flask import Flask, jsonify, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
import database

# tells Flask where my built React files live
app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)

database.init_db()

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    return app.send_static_file("index.html")

@app.route("/get_products")    # fetch product table data & return JSON
def get_products():
    conn = database.get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        select * from product
    """)

    rows = cur.fetchall()

    cur.close()     # important to close cursor & connection
    conn.close()

    return jsonify(rows)

@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.get_json()

    conn = database.get_connection()
    cur = conn.cursor()

    # %s required for psycopg2
    cur.execute("""
        insert into product
            (name, price, quantity)
        values
            (%s, %s, %s)
    """, (data["name"], data["price"], data["quantity"]))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Product created!"}), 201

@app.route("/update_product/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()

    conn = database.get_connection()
    cur = conn.cursor()

    cur.execute("""
        update product
        set name = %s, price = %s, quantity = %s
        where id = %s
    """, (data["name"], data["price"], data["quantity"], id))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Product updated!"}), 201

if __name__ == "__main__":
    app.run(debug=True)