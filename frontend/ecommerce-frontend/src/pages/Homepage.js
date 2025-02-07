import React, { useEffect, useState } from 'react';
import ProductList from '../components/ProductList';

const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/products/')
      .then(response => {
        // ✅ Check if response is valid JSON
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        // ✅ Ensure that the response is actually JSON
        if (!Array.isArray(data)) {
          throw new Error('Invalid JSON response from backend');
        }
        setProducts(data);
      })
      .catch(err => {
        console.error("Error fetching products:", err);
        setError("Failed to load products. Make sure the backend is running.");
      });
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <h1>Welcome to CircuitCart!</h1>
      <ProductList products={products} />
    </div>
  );
};

export default HomePage;
