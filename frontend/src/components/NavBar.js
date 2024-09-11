// src/components/NavBar.js
import React from "react";
import "./NavBar.css";

const NavBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="logo">
          <img src="images/logo-wide.png" alt="Corner Bakery Cafe" />
        </div>
        <ul className="navbar-links">
          <li>
            <a href="#menu">Menu</a>
          </li>
          <li>
            <a href="#locations">Locations</a>
          </li>
          <li>
            <a href="#order">Order Online</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default NavBar;
