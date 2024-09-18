// src/components/MenuItem.js
import React from "react";
import "./MenuItem.css";

const MenuItem = ({ item }) => {
  console.log("item:: ", item);
  return (
    <div className="menu-item">
      <img src={item.image_url} alt={item.name} className="menu-item-image" />
      <div className="menu-item-details">
        <h3>{item.name}</h3>
        <p>{item.description}</p>
        <p className="price">${item.price}</p>
        <button className="order-btn">Order Now</button>
        &nbsp;({item.location_name.replace("Corner Bakery Cafe - ", "")})
      </div>
    </div>
  );
};

export default MenuItem;
