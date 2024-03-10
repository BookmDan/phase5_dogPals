import { firebase } from '../firebase/firebase';
// import PassList from './forms/PassList';
// import AddPassForm from './forms/AddPassForm';
// import PetList from './forms/PetList';
import { useState, useEffect } from 'react'
import { useAuth } from '../contexts/authContext'

function Home() {
  const [passes, setPasses] = useState([]);
  const [pets, setPets] = useState([]);
  const { currentUser } = useAuth()

  // useEffect(() => {
    // const fetchPasses = async () => {
    //   // Fetch passes from Firebase or your backend
    //   const passesSnapshot = await firebase.passes().get();
    //   const passesData = passesSnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    //   setPasses(passesData);
    // };
    // const fetchPets = async () => {
    //   // Fetch pets from Firebase or your backend
    //   const petsSnapshot = await firebase.pets().get();
    //   const petsData = petsSnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    //   setPets(petsData);
    // };

    // fetchPasses();
    // fetchPets();
  // }, []);

  // const handleAddPass = (newPass) => {
  //   // Add pass to Firebase or your backend
  //   firebase.passes().add(newPass);
  //   setPasses([...passes, newPass]);
  // };

      // <div className='text-2xl font-bold pt-14'>Hello       {currentUser.displayName ? currentUser.displayName : currentUser.email}, you are now logged in.
      // </div>
      // <div className="App">
      //   <h1>My Pet Wallet</h1>
      //   <AddPassForm onAddPass={handleAddPass} />
      //   <PassList passes={passes} />
      //   <PetList pets={pets} />
      // </div>
  return (
    <>
      <div>
        <h2>Race Events</h2>
      </div>
    </>
  )
}

export default Home;
