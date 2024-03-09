// components/PassList.js
import React from 'react';

function PassList({ passes }) {
  return (
    <div>
      <h2>Passes</h2>
      <ul>
        {passes.map((pass, index) => (
          <li key={index}>{pass.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default PassList;
