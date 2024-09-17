import React, { useEffect, useState } from "react";
import NavBar from "./components/NavBar";
import MenuCategory from "./components/MenuCategory";
import "./App.css";
import LocationList from "./components/LocationList";
import {
  fetchCategories,
  fetchMenuItems,
  fetchMenuItemsByLocation,
} from "./services/apiService";

const App = () => {
  const [categories, setCategories] = useState([]);
  const [menuItems, setMenuItems] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedLocationId, setSelectedLocationId] = useState(null);

  const handleSelectLocation = (locationId) => {
    setSelectedLocationId(locationId);
  };

  useEffect(() => {
    const loadCategories = async () => {
      const data = await fetchCategories();
      setCategories(data);
      setSelectedCategory(data[0].category_id); // Automatically select the first category as default
    };
    loadCategories();

    const loadMenuItems = async () => {
      let data;

      if (selectedLocationId) {
        // Fetch filtered menu items if locationId is provided
        data = await fetchMenuItemsByLocation(selectedLocationId);
      } else {
        // Fetch all menu items if no locationId is provided
        data = await fetchMenuItems();
      }

      setMenuItems(data);
    };

    loadMenuItems();
  }, [selectedLocationId]);

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
      <LocationList onSelectLocation={handleSelectLocation} />
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
