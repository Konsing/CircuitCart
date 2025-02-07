// src/pages/HomePage.js
import React, { useEffect, useState } from 'react';
import ProductList from '../components/ProductList';

const HomePage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch all products from the Django API
    fetch('/api/products/')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Welcome to our Computer Components Store!</h1>
      <ProductList products={products} />
    </div>
  );
};

export default HomePage;
