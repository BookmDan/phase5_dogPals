import { onAuthStateChanged } from 'firebase/auth'
import React,{ useState, useEffect, useContext } from "react"
import { auth } from '../../firebase/firebase'


const AuthContext = React.createContext()

export function useAuth() { 
  return useContext(AuthContext)
 } 

function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null)
  const [userLoggedIn, setUserLoggedIn] = useState(false)
  const [isEmailUser, setIsEmailUser] = useState(false);
  const [isGoogleUser, setIsGoogleUser] = useState(false);
  // const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsubsubscribe = onAuthStateChanged(auth, initializeUser)
    return unsubsubscribe
  }, []);

  async function initializeUser(user) {
    if (user) {
      setCurrentUser({ ...user })
      const isEmail = user.providerData.some(
        (provider) => provider.providerId === "password"
      );
      setIsEmailUser(isEmail);
      setUserLoggedIn(true)
    } else {
      setCurrentUser(null)
      setUserLoggedIn(false)
    }
    // setLoading(false)
  }

  const value = {
    userLoggedIn,
    isEmailUser,
    isGoogleUser,
    currentUser,
    setCurrentUser
  }

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  )
}

export default AuthProvider