-- SQL Code (Schema):

-- Switch to the newly created database

-- Drop tables with CASCADE to automatically remove dependent objects
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS inventory CASCADE;
DROP TABLE IF EXISTS location_menu_items CASCADE;
DROP TABLE IF EXISTS menu_items CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS user_roles CASCADE;
DROP TABLE IF EXISTS roles CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS order_statuses CASCADE;
DROP TABLE IF EXISTS user_addresses CASCADE;
DROP TABLE IF EXISTS address_types CASCADE;
DROP TABLE IF EXISTS user_profiles CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS locations CASCADE;

-- =========================
-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	is_active BOOLEAN DEFAULT TRUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    phone_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- Order Status Lookup Table
CREATE TABLE order_statuses (
    order_status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_status_name VARCHAR(50) UNIQUE
);

-- =========================
-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    order_status_id INT,
    total_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (order_status_id) REFERENCES order_statuses(order_status_id) ON DELETE CASCADE
);

-- =========================
-- User Profiles Table
CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    date_of_birth DATE,
    profile_picture_url VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- =========================
-- Categories Table
CREATE TABLE categories (
    category_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category_name VARCHAR(100),
    description TEXT,
    parent_category_id INT DEFAULT NULL,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- =========================
-- Menu Items Table
CREATE TABLE menu_items (
    item_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category_id INT,
    item_name VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2),
    image_url VARCHAR(255),
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);


-- =========================
-- Inventory Table for Menu Items
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    item_id INT,
    quantity_available INT,
    reorder_level INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
);

-- =========================
-- Order Items Table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    item_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
);

-- =========================
-- Roles Table
CREATE TABLE roles (
    role_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    role_name VARCHAR(50)
);

-- =========================
-- User Roles Table
CREATE TABLE user_roles (
    user_role_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    role_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

CREATE TABLE locations (
    location_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    location_name VARCHAR(100),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE location_menu_items (
    location_menu_item_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    location_id INT,
    item_id INT,
    is_available BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
);

-- =========================
-- Address Types Lookup Table
CREATE TABLE address_types (
    address_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    address_type_name VARCHAR(50) UNIQUE
);

-- =========================
-- User Addresses Table
CREATE TABLE user_addresses (
    address_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    address_type_id INT,
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (address_type_id) REFERENCES address_types(address_type_id) ON DELETE CASCADE
);


-- Insert Order Statuses
INSERT INTO order_statuses (order_status_name) VALUES
('Pending'), ('Processing'), ('Completed');

-- Insert Users
INSERT INTO users (first_name, last_name, email, password_hash, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', 'hashed_password_1', '555-1234'),
('Jane', 'Smith', 'jane.smith@example.com', 'hashed_password_2', '555-5678');

-- Insert User Profiles
INSERT INTO user_profiles (user_id, date_of_birth, profile_picture_url) VALUES
(1, '1985-05-15', 'https://example.com/images/john_doe.png'),
(2, '1990-07-22', 'https://example.com/images/jane_smith.png');

-- Insert Address Types
INSERT INTO address_types (address_type_name) VALUES
('Home'), ('Work');

-- Insert User Addresses
INSERT INTO user_addresses (user_id, address_type_id, address_line1, city, state, postal_code, country) VALUES
(1, 1, '789 Maple St', 'Charlotte', 'NC', '28205', 'USA'),
(2, 2, '101 Pine St', 'Charlotte', 'NC', '28211', 'USA');

-- Insert Locations
INSERT INTO locations (location_name, address_line1, city, state, postal_code, phone_number) VALUES
('Corner Bakery Cafe - Park Crossing', '123 Main St', 'Charlotte', 'NC', '28210', '704-123-4567'),
('Corner Bakery Cafe - Uptown', '456 Elm St', 'Charlotte', 'NC', '28202', '704-234-5678');

-- Insert Categories
INSERT INTO categories (category_name, description) VALUES
('Breakfast', 'Delicious breakfast items'),
('Lunch', 'Tasty lunch options'),
('Sides', 'Perfect accompaniments to your meal'),
('Beverages', 'Refreshing drinks');

-- Insert Menu Items
INSERT INTO menu_items (category_id, item_name, description, price, image_url) VALUES
(1, 'Avocado Toast', 'Smashed avocado on toast with toppings', 6.99, 'https://example.com/images/avocado_toast.png'),
(1, 'Pancakes', 'Fluffy pancakes with syrup', 5.99, 'https://example.com/images/pancakes.png'),
(2, 'Turkey Sandwich', 'Turkey sandwich with lettuce and tomato', 7.99, 'https://example.com/images/turkey_sandwich.png'),
(3, 'Bacon', 'Crispy bacon strips', 2.99, 'https://example.com/images/bacon.png'),
(4, 'Coffee', 'Freshly brewed coffee', 2.50, 'https://example.com/images/coffee.png');


-- Insert Inventory for Menu Items
INSERT INTO inventory (item_id, quantity_available, reorder_level) VALUES
(1, 50, 10), -- Avocado Toast
(2, 40, 10), -- Pancakes
(3, 30, 5),  -- Turkey Sandwich
(4, 100, 20),-- Bacon
(5, 200, 50);-- Coffee


-- Associate Menu Items with Locations
INSERT INTO location_menu_items (location_id, item_id, is_available) VALUES
(1, 1, TRUE), -- Avocado Toast at Park Crossing
(1, 2, TRUE), -- Pancakes at Park Crossing
(2, 3, TRUE), -- Turkey Sandwich at Uptown
(2, 4, TRUE), -- Bacon at Uptown
(1, 5, TRUE); -- Coffee at Park Crossing

-- Insert Orders
INSERT INTO orders (user_id, order_status_id, total_price) VALUES
(1, 1, 15.48),
(2, 1, 9.99);

-- Insert Order Items
INSERT INTO order_items (order_id, item_id, quantity, price) VALUES
(1, 1, 1, 6.99), -- Avocado Toast for John Doe
(1, 4, 1, 2.99), -- Bacon for John Doe
(2, 3, 1, 7.99); -- Turkey Sandwich for Jane Smith

-- Insert Roles
INSERT INTO roles (role_name) VALUES
('Admin'), ('Customer');

-- Assign Roles to Users
INSERT INTO user_roles (user_id, role_id) VALUES
(1, 2), -- John Doe is a Customer
(2, 2); -- Jane Smith is a Customer


