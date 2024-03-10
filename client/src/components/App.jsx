import {Home} from "./Home";
import {Header} from "./Header";
import {Login} from "./authentication/Login";
import {Register} from "./authentication/Register";
import '../index.css'
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import { AuthProvider } from "../contexts/authContext";

function App() {

  // <Header />

    // <div>
    //   <h2>Race Events</h2>
    // </div>
  return (
    <Router>
      <Routes>
        <Route path="/home" element={<Home /> }/>
      </Routes>
    </Router>
  );
  
}
    // <AuthProvider>
    //   <div className="w-full h-screen flex flex-col">
    //     <Router>
    //       <Routes>
    //         <Route
    //           path="/"
    //           element={<Home /> }
    //         />
    //         {/* <Route path="/*" element={<Login />} />
    //         <Route path="/login" element={<Login />} />
    //         <Route path="/register" element={<Register />} />
    //         <Route path="/home" element={<Home />} /> */}
    //       </Routes>
    //     </Router>
    //   </div>
    // </AuthProvider>

export default App;
