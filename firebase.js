// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAgwo_kcpG2Izs6Tg2sIfje70pewRAOkUs",
  authDomain: "vuejs-ad0f2.firebaseapp.com",
  projectId: "vuejs-ad0f2",
  storageBucket: "vuejs-b0af.appspot.com",
  messagingSenderId: "1001390977387",
  appId: "1:1001190987387:web:53d3aAaf93C769f619f4de"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const db = getFirestore();
