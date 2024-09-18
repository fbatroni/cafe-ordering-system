-- Insert Additional Menu Items into the Menu Items Table with Corrected Image URLs
INSERT INTO menu_items (category_id, item_name, description, price, image_url) VALUES
-- Breakfast items
(1, 'Eggs Benedict', 'Poached eggs on English muffins with hollandaise sauce', 8.99, 'images/eggs_benedict.png'),
(1, 'French Toast', 'Thick slices of bread dipped in eggs and fried', 7.99, 'images/french_toast.png'),
(1, 'Omelette', 'Three-egg omelette with cheese, ham, and vegetables', 6.99, 'images/omelette.png'),
(1, 'Bagel with Cream Cheese', 'Toasted bagel with cream cheese', 3.50, 'images/bagel.png'),
(1, 'Waffles', 'Crispy Belgian waffles with syrup', 7.50, 'images/waffles.png'),
(1, 'Breakfast Burrito', 'Flour tortilla filled with eggs, cheese, and bacon', 6.50, 'images/breakfast_burrito.png'),
(1, 'Cinnamon Roll Pancakes', 'Pancakes with a cinnamon swirl and cream cheese glaze', 8.99, 'images/cinnamon_roll_pancakes.png'),
(1, 'Blueberry Muffins', 'Freshly baked blueberry muffins', 3.50, 'images/blueberry_muffins.png'),
(1, 'Breakfast Quesadilla', 'Eggs, cheese, and sausage in a grilled tortilla', 7.99, 'images/breakfast_quesadilla.png'),
(1, 'Fruit Parfait', 'Layers of yogurt, granola, and fresh fruit', 5.99, 'images/fruit_parfait.png'),
(1, 'Egg White Omelette', 'Omelette made with egg whites and vegetables', 6.99, 'images/egg_white_omelette.png'),
(1, 'Biscuits and Gravy', 'Buttermilk biscuits smothered in sausage gravy', 6.50, 'images/biscuits_and_gravy.png'),

-- Lunch items
(2, 'Chicken Caesar Salad', 'Grilled chicken on a bed of romaine with Caesar dressing', 9.99, 'images/chicken_caesar_salad.png'),
(2, 'BLT Sandwich', 'Bacon, lettuce, and tomato sandwich', 6.99, 'images/blt.png'),
(2, 'Grilled Cheese', 'Toasted bread with melted cheese', 5.99, 'images/grilled_cheese.png'),
(2, 'Veggie Burger', 'Plant-based burger patty with lettuce, tomato, and onions', 8.99, 'images/veggie_burger.png'),
(2, 'Chicken Wrap', 'Grilled chicken wrapped in a tortilla with veggies', 7.99, 'images/chicken_wrap.png'),
(2, 'Steak Sandwich', 'Sliced steak on a hoagie roll', 10.99, 'images/steak_sandwich.png'),

(2, 'Chicken Club Sandwich', 'Grilled chicken sandwich with bacon, lettuce, tomato, and mayo', 9.50, 'images/chicken_club_sandwich.png'),
(2, 'Tuna Salad Sandwich', 'Tuna salad with lettuce and tomato on whole wheat bread', 8.50, 'images/tuna_salad_sandwich.png'),
(2, 'Pulled Pork Sandwich', 'Pulled pork with BBQ sauce on a brioche bun', 9.99, 'images/pulled_pork_sandwich.png'),
(2, 'Caesar Wrap', 'Grilled chicken, romaine lettuce, and Caesar dressing in a tortilla', 7.99, 'images/caesar_wrap.png'),
(2, 'Philly Cheesesteak', 'Sliced beef with melted cheese on a hoagie roll', 10.99, 'images/philly_cheesesteak.png'),
(2, 'Turkey BLT Wrap', 'Turkey, bacon, lettuce, and tomato in a tortilla wrap', 8.99, 'images/turkey_blt_wrap.png'),

-- Sides
(3, 'French Fries', 'Crispy golden French fries', 2.99, 'images/french_fries.png'),
(3, 'Sweet Potato Fries', 'Fried sweet potato sticks', 3.50, 'images/sweet_potato_fries.png'),
(3, 'Onion Rings', 'Battered and fried onion rings', 3.99, 'images/onion_rings.png'),
(3, 'Coleslaw', 'Cabbage and carrot salad in a creamy dressing', 2.50, 'images/coleslaw.png'),
(3, 'Side Salad', 'Small salad with mixed greens and dressing', 3.99, 'images/side_salad.png'),
(3, 'Mashed Potatoes', 'Creamy mashed potatoes with gravy', 3.99, 'images/mashed_potatoes.png'),
(3, 'Potato Salad', 'Classic potato salad with mayonnaise and mustard', 2.99, 'images/potato_salad.png'),
(3, 'Mac and Cheese', 'Creamy macaroni and cheese', 3.50, 'images/mac_and_cheese.png'),
(3, 'Garlic Bread', 'Toasted bread with garlic butter', 2.50, 'images/garlic_bread.png'),
(3, 'Mozzarella Sticks', 'Fried mozzarella sticks served with marinara sauce', 4.99, 'images/mozzarella_sticks.png'),
(3, 'House Chips', 'Crispy house-made potato chips', 2.99, 'images/house_chips.png'),
(3, 'Fruit Cup', 'Fresh seasonal fruit', 3.99, 'images/fruit_cup.png'),


-- Beverages
(4, 'Iced Tea', 'Chilled black tea with ice', 2.50, 'images/iced_tea.png'),
(4, 'Lemonade', 'Freshly squeezed lemonade', 3.00, 'images/lemonade.png'),
(4, 'Soda', 'Carbonated soft drink', 1.99, 'images/soda.png'),
(4, 'Hot Chocolate', 'Rich chocolate drink topped with whipped cream', 2.99, 'images/hot_chocolate.png'),
(4, 'Smoothie', 'Blended fruit drink', 4.99, 'images/smoothie.png'),
(4, 'Espresso', 'Strong black coffee', 2.99, 'images/espresso.png'),
(4, 'Iced Coffee', 'Chilled coffee served over ice', 3.50, 'images/iced_coffee.png'),
(4, 'Herbal Tea', 'Caffeine-free tea made with herbs', 2.99, 'images/herbal_tea.png'),
(4, 'Mocha Latte', 'Espresso with steamed milk and chocolate', 4.50, 'images/mocha_latte.png'),
(4, 'Chai Latte', 'Spiced tea mixed with steamed milk', 4.00, 'images/chai_latte.png'),
(4, 'Milkshake', 'Thick and creamy milkshake in vanilla, chocolate, or strawberry', 5.50, 'images/milkshake.png'),
(4, 'Sparkling Water', 'Carbonated water with a hint of lemon', 2.50, 'images/sparkling_water.png');


-- Insert Inventory for Additional Menu Items
INSERT INTO inventory (item_id, quantity_available, reorder_level) VALUES
(6, 40, 10),  -- Eggs Benedict
(7, 35, 10),  -- French Toast
(8, 30, 10),  -- Omelette
(9, 50, 10),  -- Bagel with Cream Cheese
(10, 40, 10), -- Waffles
(11, 45, 10), -- Breakfast Burrito
(12, 30, 10), -- Chicken Caesar Salad
(13, 40, 10), -- BLT Sandwich
(14, 35, 10), -- Grilled Cheese
(15, 25, 10), -- Veggie Burger
(16, 40, 10), -- Chicken Wrap
(17, 30, 10), -- Steak Sandwich
(18, 100, 20), -- French Fries
(19, 80, 20),  -- Sweet Potato Fries
(20, 90, 20),  -- Onion Rings
(21, 50, 10),  -- Coleslaw
(22, 50, 10),  -- Side Salad
(23, 40, 10),  -- Mashed Potatoes
(24, 100, 20), -- Iced Tea
(25, 80, 20),  -- Lemonade
(26, 120, 30), -- Soda
(27, 50, 10),  -- Hot Chocolate
(28, 60, 15),  -- Smoothie
(29, 70, 20);  -- Espresso


-- Insert Inventory for Additional Menu Items
INSERT INTO inventory (item_id, quantity_available, reorder_level) VALUES
(6, 40, 10),  -- Eggs Benedict
(7, 35, 10),  -- French Toast
(8, 30, 10),  -- Omelette
(9, 50, 10),  -- Bagel with Cream Cheese
(10, 40, 10), -- Waffles
(11, 45, 10), -- Breakfast Burrito
(12, 30, 10), -- Chicken Caesar Salad
(13, 40, 10), -- BLT Sandwich
(14, 35, 10), -- Grilled Cheese
(15, 25, 10), -- Veggie Burger
(16, 40, 10), -- Chicken Wrap
(17, 30, 10), -- Steak Sandwich
(18, 100, 20), -- French Fries
(19, 80, 20),  -- Sweet Potato Fries
(20, 90, 20),  -- Onion Rings
(21, 50, 10),  -- Coleslaw
(22, 50, 10),  -- Side Salad
(23, 40, 10),  -- Mashed Potatoes
(24, 100, 20), -- Iced Tea
(25, 80, 20),  -- Lemonade
(26, 120, 30), -- Soda
(27, 50, 10),  -- Hot Chocolate
(28, 60, 15),  -- Smoothie
(29, 70, 20);  -- Espresso


-- Associate Additional Menu Items with Both Locations in the location_menu_items table
INSERT INTO location_menu_items (location_id, item_id, is_available) VALUES
-- Park Crossing Location (Location 1)
(1, 6, TRUE),  -- Eggs Benedict
(1, 7, TRUE),  -- French Toast
(1, 8, TRUE),  -- Omelette
(1, 9, TRUE),  -- Bagel with Cream Cheese
(1, 10, TRUE), -- Waffles
(1, 11, TRUE), -- Breakfast Burrito
(1, 30, TRUE),  -- Chicken Club Sandwich
(1, 31, TRUE),  -- Tuna Salad Sandwich
(1, 32, TRUE),  -- Pulled Pork Sandwich
(1, 33, TRUE),  -- Caesar Wrap
(1, 34, TRUE),  -- Philly Cheesesteak
(1, 35, TRUE),  -- Turkey BLT Wrap
(1, 42, TRUE),  -- Iced Coffee
(1, 43, TRUE),  -- Herbal Tea
(1, 44, TRUE),  -- Mocha Latte
(1, 45, TRUE),  -- Chai Latte
(1, 46, TRUE),  -- Milkshake
(1, 47, TRUE),  -- Sparkling Water

-- Uptown Location (Location 2)
(2, 12, TRUE), -- Chicken Caesar Salad
(2, 13, TRUE), -- BLT Sandwich
(2, 14, TRUE), -- Grilled Cheese
(2, 15, TRUE), -- Veggie Burger
(2, 16, TRUE), -- Chicken Wrap
(2, 17, TRUE), -- Steak Sandwich
(2, 36, TRUE),  -- Cinnamon Roll Pancakes
(2, 37, TRUE),  -- Blueberry Muffins
(2, 38, TRUE),  -- Breakfast Quesadilla
(2, 39, TRUE),  -- Fruit Parfait
(2, 40, TRUE),  -- Egg White Omelette
(2, 41, TRUE),  -- Biscuits and Gravy
(2, 48, TRUE),  -- Potato Salad
(2, 49, TRUE),  -- Mac and Cheese
(2, 50, TRUE),  -- Garlic Bread
(2, 51, TRUE),  -- Mozzarella Sticks
(2, 52, TRUE),  -- House Chips
(2, 53, TRUE),  -- Fruit Cup

-- Common items at both locations
(1, 18, TRUE), (2, 18, TRUE),  -- French Fries
(1, 19, TRUE), (2, 19, TRUE),  -- Sweet Potato Fries
(1, 20, TRUE), (2, 20, TRUE),  -- Onion Rings
(1, 21, TRUE), (2, 21, TRUE),  -- Coleslaw
(1, 22, TRUE), (2, 22, TRUE),  -- Side Salad
(1, 23, TRUE), (2, 23, TRUE),  -- Mashed Potatoes
(1, 24, TRUE), (2, 24, TRUE),  -- Iced Tea
(1, 25, TRUE), (2, 25, TRUE),  -- Lemonade
(1, 26, TRUE), (2, 26, TRUE),  -- Soda
(1, 27, TRUE), (2, 27, TRUE),  -- Hot Chocolate
(1, 28, TRUE), (2, 28, TRUE),  -- Smoothie
(1, 29, TRUE), (2, 29, TRUE);  -- Espresso


