// frontend/src/components/LocationList.js
import React, { useState, useEffect } from "react";
import { fetchLocations } from "../services/apiService";

const LocationList = ({ onSelectLocation }) => {
  const [locations, setLocations] = useState([]);
  const [selectedLocation, setSelectedLocation] = useState(1);

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
        {locations.map((location) => (
          <button
            key={location.location_id}
            className={`category-button ${
              selectedLocation === location.location_id ? "active" : ""
            }`}
            onClick={() => setSelectedLocation(location.location_id)}
          >
            {location.location_name}
          </button>
        ))}
      </div>
    </div>
  );
};

export default LocationList;
