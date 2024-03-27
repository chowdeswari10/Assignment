from flask import Flask, jsonify, request, make_response, redirect, url_for, render_template
from bson import ObjectId
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)

# MongoDB connection setup
uri = "mongodb+srv://mchowdeswari007:WByzp9MbIq7mFdoy@cluster0.3wm2fac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.Campus_market  # Replace 'your_database_name' with your actual database name

# Sample username and password
sample_username = "admin"
sample_password = "123"  # You can change this to any password you prefer

# Check if the sample user already exists
if not db.users.find_one({'username': sample_username}):
    # Hash the password
    hashed_password = bcrypt.hashpw(sample_password.encode('utf-8'), bcrypt.gensalt())
    # Insert the sample user into the database
    db.users.insert_one({'username': sample_username, 'password': hashed_password})
    print("Sample user inserted successfully.")

# Define routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.users.find_one({'username': username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            # Authentication successful, redirect to home page
            return redirect(url_for('home'))
        else:
            # Authentication failed, render login page with error message
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    # Fetch product details from the database
    products = db.products.find()
    # Here you can choose a sample product to pass to the template,
    # or you can fetch a specific product from the database
    sample_product = db.products.find_one()  # Fetching a sample product
    return render_template('home.html', products=products, product=sample_product)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        db.users.insert_one({'username': username, 'password': hashed_password})
        return redirect(url_for('home'))
    else:
        return render_template('add_user.html')

@app.route('/products', methods=['GET'])
def get_products():
    products = db.products.find()
    output = []
    for product in products:
        output.append({'_id': str(product['_id']), 'name': product['name'], 'price': product['price'], 'description': product['description']})
    return jsonify({'result': output})

@app.route('/products/<product_name>', methods=['GET'])
def get_product_by_name(product_name):
    product = db.products.find_one({'name': product_name})
    if product:
        output = {'_id': str(product['_id']), 'name': product['name'], 'price': product['price'], 'description': product['description']}
    else:
        output = 'No such product'
    return jsonify({'result': output})

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        db.products.insert_one({'name': name, 'price': price, 'description': description})
        return redirect(url_for('home'))
    else:
        return render_template('add_product.html')

@app.route('/update_password', methods=['POST'])
def update_password():
    username = request.form['username']
    new_password = request.form['new_password']

    # Hash the new password
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    # Update the user's password in the database
    result = db.users.update_one({'username': username}, {'$set': {'password': hashed_password}})

    if result.modified_count > 0:
        return jsonify({'message': 'Password updated successfully'})
    else:
        return jsonify({'message': 'Failed to update password. User not found or password unchanged'})

@app.route('/delete_product/<product_name>', methods=['DELETE'])
def delete_product(product_name):
    db.products.delete_one({'name': product_name})
    # Redirect back to the home page after successful deletion
    return redirect(url_for('home'))

# Flask Route for searching product
@app.route('/search_product', methods=['GET'])
def search_product():
    search_query = request.args.get('search')
    product = db.products.find_one({'name': search_query})
    if product:
        # Product found, render a template with the product details
        return render_template('product_details.html', product=product)
    else:
        # Product not found, display an error message or redirect to the home page
        return "<h2>Product not found</h2>"

if __name__ == '__main__':
    app.run(debug=True)