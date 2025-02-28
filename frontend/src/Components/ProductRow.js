// Components/ProductRow.js
import React from 'react';
import ProductCard from './ProductCard';
import './ProductRow.css';

function ProductRow({ title, products }) {
  return (
    <div className="product-row">
      <div className="row-header">
        <h2 className="row-title">{title}</h2>
      </div>
      <div className="row-products">
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default ProductRow;
