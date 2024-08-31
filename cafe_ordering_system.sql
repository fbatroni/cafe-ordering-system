-- SQL Code (Schema):

-- Switch to the newly created database

-- Drop tables with CASCADE to automatically remove dependent objects
DROP TABLE IF EXISTS customization_choices CASCADE;
DROP TABLE IF EXISTS customization_options CASCADE;
DROP TABLE IF EXISTS customization_choice_types CASCADE;
DROP TABLE IF EXISTS discount_types CASCADE;
DROP TABLE IF EXISTS menu_item_add_ons CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS inventory CASCADE;
DROP TABLE IF EXISTS featured_items CASCADE;
DROP TABLE IF EXISTS location_menu_items CASCADE;
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS menu_items CASCADE;
DROP TABLE IF EXISTS order_item_customizations CASCADE;
DROP TABLE IF EXISTS order_item_add_ons CASCADE;
DROP TABLE IF EXISTS add_on_inventory CASCADE;
DROP TABLE IF EXISTS add_ons CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS user_roles CASCADE;
DROP TABLE IF EXISTS roles CASCADE;
DROP TABLE IF EXISTS audit_logs CASCADE;
DROP TABLE IF EXISTS delivery_details CASCADE;
DROP TABLE IF EXISTS delivery_method_types CASCADE;
DROP TABLE IF EXISTS order_status_history CASCADE;
DROP TABLE IF EXISTS order_promotions CASCADE;
DROP TABLE IF EXISTS promotions CASCADE;
DROP TABLE IF EXISTS payments CASCADE;
DROP TABLE IF EXISTS payment_methods CASCADE;
DROP TABLE IF EXISTS payment_statuses CASCADE;
DROP TABLE IF EXISTS payment_method_types CASCADE;
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
-- Add-Ons Table
CREATE TABLE add_ons (
    add_on_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    add_on_name VARCHAR(100),
    price DECIMAL(10, 2),
    description TEXT,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- Menu Item Add-Ons Table
CREATE TABLE menu_item_add_ons (
    menu_item_id INT,
    add_on_id INT,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id) ON DELETE CASCADE,
    PRIMARY KEY (menu_item_id, add_on_id)
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
-- Add-On Inventory Table
CREATE TABLE add_on_inventory (
    inventory_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    add_on_id INT,
    quantity_available INT,
    reorder_level INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id) ON DELETE CASCADE
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
-- Order Item Add-Ons Table
CREATE TABLE order_item_add_ons (
    order_item_add_on_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_item_id INT,
    add_on_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_item_id) REFERENCES order_items(order_item_id) ON DELETE CASCADE,
    FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id) ON DELETE CASCADE
);

-- =========================
-- Discount Types Lookup Table
CREATE TABLE discount_types (
    discount_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    discount_type_name VARCHAR(50) UNIQUE
);

-- =========================
-- Promotions Table
CREATE TABLE promotions (
    promotion_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    promotion_code VARCHAR(50) UNIQUE,
    description TEXT,
    discount_type_id INT,
    discount_value DECIMAL(10, 2),
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (discount_type_id) REFERENCES discount_types(discount_type_id) ON DELETE CASCADE
);

-- =========================
-- Order Promotions Table
CREATE TABLE order_promotions (
    order_promotion_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    promotion_id INT,
    discount_applied DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id) ON DELETE CASCADE
);

-- =========================
-- Customization Choice Types Lookup Table
CREATE TABLE customization_choice_types (
    customization_choice_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    customization_choice_type_name VARCHAR(50) UNIQUE
);

-- =========================
-- Customization Options Table
CREATE TABLE customization_options (
    customization_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    item_id INT,
    customization_name VARCHAR(100),
    choice_type_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE,
    FOREIGN KEY (choice_type_id) REFERENCES customization_choice_types(customization_choice_type_id) ON DELETE CASCADE
);

-- =========================
-- Customization Choices Table
CREATE TABLE customization_choices (
    choice_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    customization_id INT,
    choice_name VARCHAR(100),
    additional_price DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (customization_id) REFERENCES customization_options(customization_id) ON DELETE CASCADE
);

-- =========================
-- Order Item Customizations Table
CREATE TABLE order_item_customizations (
    order_item_customization_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_item_id INT,
    customization_choice_id INT,
    FOREIGN KEY (order_item_id) REFERENCES order_items(order_item_id) ON DELETE CASCADE,
    FOREIGN KEY (customization_choice_id) REFERENCES customization_choices(choice_id) ON DELETE CASCADE
);

-- =========================
-- Reviews Table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    item_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
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

-- =========================
-- Audit Logs Table
CREATE TABLE audit_logs (
    audit_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    action_taken VARCHAR(255),
    table_name VARCHAR(255),
    record_id INT,
    action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
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

CREATE TABLE featured_items (
    featured_item_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    item_id INT,
    is_featured BOOLEAN DEFAULT FALSE,
    feature_start_date DATE,
    feature_end_date DATE,
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

-- =========================
-- Payment Method Types Lookup Table
CREATE TABLE payment_method_types (
    payment_method_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    payment_method_type_name VARCHAR(50) UNIQUE
);

-- =========================
-- Payment Status Lookup Table
CREATE TABLE payment_statuses (
    payment_status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    payment_status_name VARCHAR(50) UNIQUE
);

-- =========================
-- Payment Methods Table
CREATE TABLE payment_methods (
    method_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id INT,
    payment_method_type_id INT,
    card_number VARCHAR(50),
    expiration_date DATE,
    cardholder_name VARCHAR(100),
    billing_address_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (payment_method_type_id) REFERENCES payment_method_types(payment_method_type_id) ON DELETE CASCADE,
    FOREIGN KEY (billing_address_id) REFERENCES user_addresses(address_id) ON DELETE SET NULL
);

-- =========================
-- Payments Table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    payment_method_type_id INT,
    payment_status_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (payment_method_type_id) REFERENCES payment_method_types(payment_method_type_id) ON DELETE CASCADE,
    FOREIGN KEY (payment_status_id) REFERENCES payment_statuses(payment_status_id) ON DELETE CASCADE
);

-- =========================
-- Order Status History Table
CREATE TABLE order_status_history (
    status_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    order_status_id INT,
    status_change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (order_status_id) REFERENCES order_statuses(order_status_id) ON DELETE CASCADE
);

-- =========================
-- Delivery Method Types Lookup Table
CREATE TABLE delivery_method_types (
    delivery_method_type_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    delivery_method_type_name VARCHAR(50) UNIQUE
);

-- =========================
-- Delivery Details Table
CREATE TABLE delivery_details (
    delivery_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    order_id INT,
    delivery_address_id INT,
    delivery_method_type_id INT,
    estimated_delivery_time TIMESTAMP,
    actual_delivery_time TIMESTAMP DEFAULT NULL,
    delivery_fee DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (delivery_address_id) REFERENCES user_addresses(address_id) ON DELETE SET NULL,
    FOREIGN KEY (delivery_method_type_id) REFERENCES delivery_method_types(delivery_method_type_id) ON DELETE CASCADE
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

-- Insert Add-Ons
INSERT INTO add_ons (add_on_name, price, description) VALUES
('Extra Bacon', 1.50, 'Add extra bacon to your meal'),
('Cheese', 0.75, 'Add cheese to your sandwich'),
('Whipped Cream', 0.50, 'Add whipped cream to your drink');

-- Associate Menu Items with Add-Ons
INSERT INTO menu_item_add_ons (menu_item_id, add_on_id) VALUES
(1, 1), -- Avocado Toast with Extra Bacon
(2, 2), -- Pancakes with Cheese
(4, 3); -- Coffee with Whipped Cream

-- Insert Inventory for Menu Items
INSERT INTO inventory (item_id, quantity_available, reorder_level) VALUES
(1, 50, 10), -- Avocado Toast
(2, 40, 10), -- Pancakes
(3, 30, 5),  -- Turkey Sandwich
(4, 100, 20),-- Bacon
(5, 200, 50);-- Coffee

-- Insert Inventory for Add-Ons
INSERT INTO add_on_inventory (add_on_id, quantity_available, reorder_level) VALUES
(1, 100, 20), -- Extra Bacon
(2, 80, 15),  -- Cheese
(3, 60, 10);  -- Whipped Cream

-- Associate Menu Items with Locations
INSERT INTO location_menu_items (location_id, item_id, is_available) VALUES
(1, 1, TRUE), -- Avocado Toast at Park Crossing
(1, 2, TRUE), -- Pancakes at Park Crossing
(2, 3, TRUE), -- Turkey Sandwich at Uptown
(2, 4, TRUE), -- Bacon at Uptown
(1, 5, TRUE); -- Coffee at Park Crossing

-- Insert Featured Items
INSERT INTO featured_items (item_id, is_featured, feature_start_date, feature_end_date) VALUES
(1, TRUE, '2024-08-01', '2024-08-31'), -- Avocado Toast
(5, TRUE, '2024-08-01', '2024-08-31'); -- Coffee

-- Insert Orders
INSERT INTO orders (user_id, order_status_id, total_price) VALUES
(1, 1, 15.48),
(2, 1, 9.99);

-- Insert Order Items
INSERT INTO order_items (order_id, item_id, quantity, price) VALUES
(1, 1, 1, 6.99), -- Avocado Toast for John Doe
(1, 4, 1, 2.99), -- Bacon for John Doe
(2, 3, 1, 7.99); -- Turkey Sandwich for Jane Smith

-- Insert Order Item Add-Ons
INSERT INTO order_item_add_ons (order_item_id, add_on_id, quantity, price) VALUES
(1, 1, 1, 1.50), -- Extra Bacon on Avocado Toast
(2, 2, 1, 0.75); -- Cheese on Bacon

-- Insert Payment Method Types
INSERT INTO payment_method_types (payment_method_type_name) VALUES
('Credit Card'), ('PayPal');

-- Insert Payment Statuses
INSERT INTO payment_statuses (payment_status_name) VALUES
('Completed'), ('Pending');

-- Insert Payment Methods for Users
INSERT INTO payment_methods (user_id, payment_method_type_id, card_number, expiration_date, cardholder_name, billing_address_id) VALUES
(1, 1, '4111111111111111', '2025-01-01', 'John Doe', 1),
(2, 2, 'jane.smith@paypal.com', NULL, 'Jane Smith', 2);

-- Insert Payments
INSERT INTO payments (order_id, payment_method_type_id, payment_status_id, amount) VALUES
(1, 1, 1, 15.48),
(2, 2, 2, 9.99);

-- Insert Discount Types
INSERT INTO discount_types (discount_type_name) VALUES
('Percentage'), ('Flat Amount');

-- Insert Promotions
INSERT INTO promotions (promotion_code, description, discount_type_id, discount_value, start_date, end_date) VALUES
('SUMMER20', '20% off summer special', 1, 20.00, '2024-08-01', '2024-08-31');

-- Associate Orders with Promotions
INSERT INTO order_promotions (order_id, promotion_id, discount_applied) VALUES
(1, 1, 3.10); -- 20% off on Avocado Toast and Bacon

-- Insert Order Status History
INSERT INTO order_status_history (order_id, order_status_id) VALUES
(1, 1), -- Initial status
(1, 2), -- Status changed to processing
(1, 3); -- Status changed to completed

-- Insert Delivery Method Types
INSERT INTO delivery_method_types (delivery_method_type_name) VALUES
('Delivery'), ('Pickup');

-- Insert Delivery Details
INSERT INTO delivery_details (order_id, delivery_address_id, delivery_method_type_id, estimated_delivery_time, actual_delivery_time, delivery_fee) VALUES
(1, 1, 1, '2024-08-01 10:00:00', '2024-08-01 09:45:00', 2.50);

-- Insert Customization Choice Types
INSERT INTO customization_choice_types (customization_choice_type_name) VALUES
('Single'), ('Multiple');

-- Insert Customization Options
INSERT INTO customization_options (item_id, customization_name, choice_type_id) VALUES
(1, 'Bread Type', 1), -- For Avocado Toast
(5, 'Milk Type', 1); -- For Coffee

-- Insert Customization Choices
INSERT INTO customization_choices (customization_id, choice_name, additional_price) VALUES
(1, 'Whole Wheat', 0.00), -- Bread type option for Avocado Toast
(1, 'Sourdough', 0.50),  -- Bread type option for Avocado Toast
(2, 'Whole Milk', 0.00), -- Milk type option for Coffee
(2, 'Almond Milk', 0.50); -- Milk type option for Coffee

-- Insert Order Item Customizations
INSERT INTO order_item_customizations (order_item_id, customization_choice_id) VALUES
(1, 2), -- Sourdough bread for Avocado Toast
(2, 4); -- Almond Milk for Coffee

-- Insert Reviews
INSERT INTO reviews (user_id, item_id, rating, review_text, review_date) VALUES
(1, 1, 5, 'Delicious Avocado Toast! Will order again.', '2024-08-01'),
(2, 3, 4, 'Good sandwich but could use more flavor.', '2024-08-02');

-- Insert Roles
INSERT INTO roles (role_name) VALUES
('Admin'), ('Customer');

-- Assign Roles to Users
INSERT INTO user_roles (user_id, role_id) VALUES
(1, 2), -- John Doe is a Customer
(2, 2); -- Jane Smith is a Customer

-- Insert Audit Logs
INSERT INTO audit_logs (user_id, action_taken, table_name, record_id) VALUES
(1, 'Created Order', 'orders', 1),
(2, 'Updated Profile', 'user_profiles', 2);
