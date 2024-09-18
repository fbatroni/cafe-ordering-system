// frontend/src/components/LocationList.js
import React, { useState, useEffect } from "react";
import { fetchLocations } from "../services/apiService";

const LocationList = ({ selectedLocationId, onSelectLocation }) => {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    const loadLocations = async () => {
      const data = await fetchLocations();
      setLocations(data);
    };
    loadLocations();
  }, []);

  return (
    <div>
      <div className="locations-nav">
        <button
          className={`category-button ${
            selectedLocationId === null ? "active" : ""
          }`}
          onClick={() => onSelectLocation(null)}
        >
          All
        </button>
        {locations.map((location) => (
          <button
            key={location.location_id}
            className={`category-button ${
              selectedLocationId === location.location_id ? "active" : ""
            }`}
            onClick={() => onSelectLocation(location.location_id)}
          >
            {location.location_name}
          </button>
        ))}
      </div>
    </div>
  );
};

export default LocationList;
