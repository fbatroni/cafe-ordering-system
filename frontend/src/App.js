import React, { useEffect, useState } from "react";
import NavBar from "./components/NavBar";
import MenuCategory from "./components/MenuCategory";
import "./App.css";

const App = () => {
  const [categories, setCategories] = useState([]);
  const [menuItems, setMenuItems] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  useEffect(() => {
    // Fetch categories
    fetch("http://localhost:8000/v1/categories")
      .then((response) => response.json())
      .then((data) => {
        setCategories(data);
        setSelectedCategory(data[0].category_id); // Automatically select the first category as default
      });

    // Fetch menu items
    fetch("http://localhost:8000/v1/menu-items")
      .then((response) => response.json())
      .then((data) => {
        const updatedMenuItems = data.map((item) => {
          return {
            ...item,
            image_url: item.image_url.replace("https://example.com/", ""), // Replace the base URL
          };
        });
        setMenuItems(updatedMenuItems); // Set the updated menu items
      });
  }, []);

  const handleCategoryClick = (categoryId) => {
    setSelectedCategory(categoryId); // Update the selected category
  };

  const filteredMenuItems = menuItems.filter(
    (item) => item.category_id === selectedCategory
  );

  return (
    <div className="App">
      <NavBar />
      <div className="categories-nav">
        {categories.map((category) => (
          <button
            key={category.category_id}
            className={`category-button ${
              selectedCategory === category.category_id ? "active" : ""
            }`}
            onClick={() => handleCategoryClick(category.category_id)}
          >
            {category.category_name}
          </button>
        ))}
      </div>

      <div className="menu-container">
        {filteredMenuItems.length > 0 ? (
          <MenuCategory
            categoryName={
              categories.find((cat) => cat.category_id === selectedCategory)
                ?.name
            }
            items={filteredMenuItems}
          />
        ) : (
          <p>No menu items found for this category.</p>
        )}
      </div>
    </div>
  );
};

export default App;
