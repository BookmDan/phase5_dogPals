import { useState } from "react";
import {LoginForm} from "./Login";
import {SignupForm} from "./Register";
import {LoginLoading} from "./cards-lists-boxes/LoginLoading";

function Login({ onLogin }) {

  const [signupMode, setSignupMode] = useState(false)
  // const [isLoading, setIsLoading] = useState(false)

  // setIsLoading={setIsLoading} 
  return (
    <div>
      {isLoading? <LoginLoading />: ""}
    {signupMode? 
      <SignupForm signupMode={signupMode} setSignupMode={setSignupMode} onLogin={onLogin} /> : 
      <LoginForm 
        onLogin={onLogin} 
        setSignupMode={setSignupMode} 
        signupMode={signupMode}
        // setIsLoading={setIsLoading} 
      />}
    </div>
  )
}

export default Login