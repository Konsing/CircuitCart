// src/pages/CombosPage.js
import React, { useEffect, useState } from 'react';
import ProductList from '../components/ProductList';

const CombosPage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch combo products from the Django API
    fetch('/api/products/combos/')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Combo Deals</h1>
      <ProductList products={products} />
    </div>
  );
};

export default CombosPage;
