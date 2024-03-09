import { onAuthStateChanged } from 'firebase/auth'
import { useState, useEffect, useContext } from "react"
import { auth } from '../../firebase/firebase'
import { onAuthStateChanged } from 'firebase/auth'


const AuthContext = React.createContext()

export function useAuth() { 
  return useContext(AuthContext)
 } 

function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null)
  const [userLoggedIn, setUserLoggedIn] = useState(false)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const unsubsubscribe = onAuthStateChanged(auth, initalizedUser)
    return unsubsubscribe
  }, []);

  async function initializeUser(user) {
    if (user) {
      setCurrentUser({ ...user })
      setUserLoggedIn(true)
    } else {
      setCurrentUser(null)
      setUserLoggedIn(false)
    }
    setLoading(false)
  }

  const value = {
    currentUser, 
    userLoggedIn,
    loading
  }

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  )
}

export default AuthProvider