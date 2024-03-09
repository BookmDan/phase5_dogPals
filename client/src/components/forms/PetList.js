// components/PetList.js
import React from 'react';

function PetList({ pets }) {
  return (
    <div>
      <h2>Pets</h2>
      <ul>
        {pets.map((pet, index) => (
          <li key={index}>{pet.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default PetList;
