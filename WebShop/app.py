from flask import Flask, request, render_template, jsonify
from hashlib import md5
import random
import mysql.connector


app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template('index.html')

@app.route("/logginn.html")
def login_route():
    return render_template('logginn.html')

@app.route("/handlekurv")
def kurv_route():
    return render_template('handlekurv.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("first")
    password = request.form.get("password")

    # Your authentication logic here

    print("Username:", username)
    print("Password:", password)

    return render_template('index.html')


@app.route("/Asus.html")
def produkt_route():
    return render_template('Asus.html')

@app.route("/IdeaPad.html")
def produkt1_route ():
    return render_template('IdeaPad.html')

@app.route("/airpods.html")
def produkt2_route ():
    return render_template('airpods.html')

@app.route("/iphone 14.html")
def produkt3_route ():
    return render_template('iphone 14.html')

@app.route("/vr briller.html")
def produkt4_route ():
    return render_template('vr briller.html')

@app.route("/Robot dog.html")
def produkt5_route ():
    return render_template('Robot dog.html')

@app.route("/gamingskjerm.html")
def produkt6_route ():
    return render_template('gamingskjerm.html')

@app.route("/intel.html")
def produkt7_route ():
    return render_template('intel.html')



<<<<<<< HEAD
 # Check if the cookie is already set
    cookie_id = request.cookies.get("cookie_id")
    if not cookie_id:
        # If the cookie is not set, create a new one and set it
        new_cookie = db.create_new_cookie()  # Assuming this method generates a new cookie ID
        db.add_cookie(new_cookie, request.base_url)  # Assuming this method stores the cookie in the database
        resp = make_response(render_template("index.html", cookie_login_ID=""))
        resp.set_cookie('cookie_id', new_cookie)  # Setting the cookie in the response
        return resp
    else:
        # If the cookie is already set, render the template with the cookie ID
        return render_template('index.html', cookie_login_ID=cookie_id)
    
    
    # Route for setting the cookie
@app.route('/', methods=['POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('index.html'))
        resp.set_cookie('userID', user)
        return resp
=======
# Define your database connection function
def db_connect():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            database="nettbutikk",
            user="root",
            password="EtVeldigBraPassord"
        )
        return connection
    except Exception as e:
        print("Error connecting to the DB:", e)

# Define your Flask routes
@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    data = request.get_json()
    cookie_id = create_new_cookie()
    url = data.get('url')
    add_cookie_to_db(cookie_id, url)
    return jsonify({'message': 'Cookie added successfully', 'cookie_id': cookie_id})
>>>>>>> 967c6ee155be09161b645af1c479a6fa9f94c407

@app.route('/click_cookie', methods=['POST'])
def click_cookie():
    data = request.get_json()
    cookie_id = data.get('cookie_id')
    click_cookie_update(cookie_id)
    return jsonify({'message': 'Cookie click updated'})

@app.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    data = request.get_json()
    cookie_id = data.get('cookie_id')
    delete_cookie(cookie_id)
    return jsonify({'message': 'Cookie deleted successfully'})

@app.route('/get_cookie_info', methods=['GET'])
def get_cookie_info():
    cookie_id = request.args.get('cookie_id')
    cursor = db_connect().cursor()
    cookie_info = get_cookie(cookie_id, cursor)
    cursor.close()
    if cookie_info:
        return jsonify({'cookie_info': cookie_info})
    else:
        return jsonify({'message': 'Cookie not found'})

@app.route('/get_number_of_people', methods=['GET'])
def get_number_of_people():
    total_visitors, total_clicked = get_number_of_people_from_db()
    return jsonify({'total_visitors': total_visitors, 'total_clicked': total_clicked})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
