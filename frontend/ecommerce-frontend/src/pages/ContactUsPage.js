// src/pages/ContactUsPage.js
import React from 'react';

const ContactUsPage = () => {
  return (
    <div>
      <h1>Contact Us</h1>
      <form>
        <label>Name:</label>
        <input type="text" name="name" required />
        <br />
        <label>Email:</label>
        <input type="email" name="email" required />
        <br />
        <label>Message:</label>
        <textarea name="message" required></textarea>
        <br />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ContactUsPage;
