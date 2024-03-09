import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyAVSv1zjxwcC7e3_R_ccfg0pp8X9CBBcB4",
  authDomain: "dogpals-be115.firebaseapp.com",
  projectId: "dogpals-be115",
  storageBucket: "dogpals-be115.appspot.com",
  messagingSenderId: "278448206513",
  appId: "1:278448206513:web:c57a9291ee6d93b856e890",
  measurementId: "G-TZ38PP9R00"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// export default firebaseConfig;