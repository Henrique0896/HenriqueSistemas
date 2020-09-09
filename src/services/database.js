import firebase from 'firebase';


const firebaseConfig = {
  apiKey: "AIzaSyBfBcbqqP14648QcJe5p0pfKV0JDz_lH9I",
  authDomain: "upgracie.firebaseapp.com",
  databaseURL: "https://upgracie.firebaseio.com",
  projectId: "upgracie",
  storageBucket: "upgracie.appspot.com",
  messagingSenderId: "808086691507",
  appId: "1:808086691507:web:8c848b7e30ac82b4b01ac6"
};


const database = firebase.initializeApp(firebaseConfig);


export default database;