// Components/FeaturedCarousel.js
import React, { useState, useEffect } from 'react';
import './FeaturedCarousel.css';

const featuredProducts = [
  {
    id: 1,
    name: "Gaming PC",
    image: "/images/product1.png",
    description: "High performance gaming PC for the ultimate gaming experience."
  },
  {
    id: 2,
    name: "Ultra HD Monitor",
    image: "/images/product2.png",
    description: "Stunning visuals with our ultra HD monitors."
  },
  {
    id: 3,
    name: "RGB Mechanical Keyboard",
    image: "/images/product3.png",
    description: "Enhance your gaming setup with our RGB mechanical keyboards."
  },
];

function FeaturedCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex(prev => (prev + 1) % featuredProducts.length);
    }, 5000); // Change slide every 5 seconds

    return () => clearInterval(timer);
  }, []);

  const { name, image, description } = featuredProducts[currentIndex];

  return (
    <div className="carousel">
      <img src={image} alt={name} className="carousel-image" />
      <div className="carousel-caption">
        <h2>{name}</h2>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default FeaturedCarousel;
