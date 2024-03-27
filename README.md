**Campus Market Web Application**

This repository contains a Flask web application for managing users and products in a campus market scenario. Users can authenticate, add new users, add products, update passwords, search for products, and delete products.

### Features

1. **User Authentication**: Users can log in with their username and password.
2. **User Management**: Administrators can add new users to the system.
3. **Product Management**: Administrators can add, view, and delete products.
4. **Password Security**: User passwords are hashed for security using bcrypt.
5. **Search Functionality**: Users can search for products by name.

### Technologies Used

- Python
- Flask
- MongoDB
- bcrypt

### Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/your_username/campus-market.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up MongoDB and configure the connection URI in `app.py`.

4. Run the application:

   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000` to access the application.

### Usage

- Log in with the provided sample username and password (admin / 123).
- Navigate through the different routes to manage users and products.
- Add new users or products using the respective forms.
- Update passwords or delete products as needed.
- Search for products by name using the search functionality.


