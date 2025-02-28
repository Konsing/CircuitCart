// Pages/ProductsPage.js
import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/ProductsPage.css';

function ProductsPage() {
  return (
    <div className="products-page">
      <Header />
      <div className="products-content">
        <h2>Our Products</h2>
        <p>Browse our collection – more products coming soon!</p>
      </div>
      <Footer />
    </div>
  );
}

export default ProductsPage;
