import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import database from '../../services/database';
import Material from './Material';


const Login = () => {


  const history = useHistory();
  useEffect( () => {
   if(localStorage.getItem('uiduser')){
      history.push('/');
    };
  }, [])
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  

  const clearErrors = () => {
    setEmailError('');
    setPasswordError('');
  }

  async function handleLogin(e) {
    e.preventDefault();
    clearErrors();
    try {
      const response = await database.auth()
        .signInWithEmailAndPassword(email, password);
        history.push('/');
        localStorage.setItem( 'uiduser', response.user.uid );
        /*localStorage.setItem('name', response.user.name);*/
    } catch (e) {
        switch (e.code) {
          case "auth/invalid-email":
            setEmailError('Digite um e-mail válido!');
            break;
          case "auth/user-disabled":
          case "auth/user-not-found":
          case "auth/wrong-password":
            setPasswordError('E-mail e/ou senha inválidos!');
            break;
      }
    }
  }

  return (
      <Material 
        handleLogin ={ handleLogin }
        email ={ email }
        setEmail ={ setEmail }
        emailError ={ emailError }
        password ={ password }
        setPassword ={ setPassword }
        passwordError ={ passwordError }
     />
   
  )
}

export default Login;
