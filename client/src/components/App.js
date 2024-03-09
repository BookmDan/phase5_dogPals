import { useState } from 'react'
import Home from "./Home";
import Header from "./Header";
import Login from "./components/auth/login";
import Register from "./components/auth/register";
import './App.css'
import { useRoutes } from 'react-router-dom';
import { AuthProvider } from "./contexts/authContext";

function App() {
  const routesArray = [
    {
      path: "*",
      element: <Login />,
    },
    {
      path: "/login",
      element: <Login />,
    },
    {
      path: "/register",
      element: <Register />,
    },
    {
      path: "/home",
      element: <Home />,
    },
  ];

  let routesElement = useRoutes(routesArray);
  
  return (
    <AuthProvider>
      <Header />
      <div className="w-full h-screen flex flex-col">{routesElement}</div>
    </AuthProvider>
  )
}

export default App
