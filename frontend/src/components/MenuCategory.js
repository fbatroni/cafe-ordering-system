// src/components/MenuCategory.js
import React from "react";
import MenuItem from "./MenuItem";
import "./MenuCategory.css";

const MenuCategory = ({ categoryName, items }) => {
  return (
    <section className="menu-category">
      <h2 className="category-name">{categoryName}</h2>
      <div className="menu-items">
        {items.map((item) => (
          <MenuItem key={item.id} item={item} />
        ))}
      </div>
    </section>
  );
};

export default MenuCategory;
