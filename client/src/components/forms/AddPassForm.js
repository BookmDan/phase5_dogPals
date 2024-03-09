import { useState } from 'react';

function AddPassForm({ onAddPass }) {
  const [passName, setPassName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!passName.trim()) return;
    const newPass = { name: passName };
    onAddPass(newPass);
    setPassName('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter pass name"
        value={passName}
        onChange={(e) => setPassName(e.target.value)}
      />
      <button type="submit">Add Pass</button>
    </form>
  );
}

export default AddPassForm;
