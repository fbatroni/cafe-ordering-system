// frontend/src/components/MenuItems.js
import React, { useState, useEffect } from "react";
import { fetchMenuItemsByLocation } from "../services/apiService";

const MenuItems = ({ locationId }) => {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    if (locationId) {
      const loadMenuItems = async () => {
        const data = await fetchMenuItemsByLocation(locationId);
        setMenuItems(data);
      };
      loadMenuItems();
    }
  }, [locationId]);

  return (
    <div>
      <h2>Menu Items</h2>
      {locationId ? (
        <ul>
          {menuItems.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>Please select a location to view menu items.</p>
      )}
    </div>
  );
};

export default MenuItems;
