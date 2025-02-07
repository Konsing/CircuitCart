// src/pages/FeaturedPage.js
import React, { useEffect, useState } from 'react';
import ProductList from '../components/ProductList';

const FeaturedPage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch featured products from the Django API
    fetch('/api/products/featured/')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Featured Products</h1>
      <ProductList products={products} />
    </div>
  );
};

export default FeaturedPage;
