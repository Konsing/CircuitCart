// Components/ProductCard.js
import React from 'react';
import './ProductCard.css';

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img 
        src={product.image} 
        alt={product.name} 
        className="product-image" 
      />
      <div className="product-info">
        <h3 className="product-name">{product.name}</h3>
      </div>
    </div>
  );
}

export default ProductCard;
