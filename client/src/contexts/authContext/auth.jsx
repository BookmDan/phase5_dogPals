import { auth, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "../../firebase/firebase";


export const createUserWithEmailAndPassword = async (email, password) => {
  return createUserWithEmailAndPassword(auth,email,password)
}

export const doSignInWithEmailAndPassword = (email, password) => {
  return signInWithEmailAndPassword(auth,email,password)
}

export const doSignInWithGoogle = async () => {
  const provider = new GoogleAuthProvider()
  const result = await signInWithPopup(auth, provider)
  // result.user save user info in firestore
  return result
}

export const doSignOut = () => {
  return auth.signOut()
}

// export const doPasswordReset = (email) => {
//   return sendPasswordResetEmail(auth,email)
// }

// export const doPassWordChange = (password) => {
//   return updatedPassword(auth.currentUser, password)
// }

// export const doSendEmailVerification = () => {
//   return sendEmailVerification(auth.currentUser, {
//     url: `${window.location.origin}/home`,
//   })
// }