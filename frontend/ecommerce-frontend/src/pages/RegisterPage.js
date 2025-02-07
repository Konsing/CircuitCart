// src/pages/RegisterPage.js
import React from 'react';

const RegisterPage = () => {
  return (
    <div>
      <h1>Register</h1>
      <form>
        <label>Name:</label>
        <input type="text" name="name" required />
        <br />
        <label>Email:</label>
        <input type="email" name="email" required />
        <br />
        <label>Password:</label>
        <input type="password" name="password" required />
        <br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegisterPage;
