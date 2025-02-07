// src/components/ProductCard.js
import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <div style={{ border: '1px solid #ddd', padding: '1rem', width: '220px' }}>
      <img 
        src={product.image} 
        alt={product.title} 
        style={{ width: '200px', height: 'auto' }} 
      />
      <h2 style={{ fontSize: '1.2rem' }}>{product.title}</h2>
      <p>{product.description}</p>
      <p><strong>${product.price}</strong></p>
      <button>Add to Cart</button>
    </div>
  );
};

export default ProductCard;
