// Pages/CartPage.js
import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/CartPage.css';

function CartPage() {
  return (
    <div className="cart-page">
      <Header />
      <div className="cart-content">
        <h2>Your Cart</h2>
        <p>No items in your cart yet.</p>
      </div>
      <Footer />
    </div>
  );
}

export default CartPage;
