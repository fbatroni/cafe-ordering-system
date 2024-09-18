-- Update image_url in menu_items table
UPDATE menu_items
SET image_url = REPLACE(image_url, 'https://example.com/images/', 'images/')
WHERE image_url LIKE 'https://example.com/images/%';

-- Update profile_picture_url in user_profiles table
UPDATE user_profiles
SET profile_picture_url = REPLACE(profile_picture_url, 'https://example.com/images/', 'images/')
WHERE profile_picture_url LIKE 'https://example.com/images/%';
