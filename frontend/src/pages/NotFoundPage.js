// Pages/NotFoundPage.js
import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import '../Styles/NotFoundPage.css';

function NotFoundPage() {
  return (
    <div className="not-found-page">
      <Header />
      <div className="not-found-content">
        <h2>404 - Page Not Found</h2>
        <p>The page you are looking for does not exist.</p>
      </div>
      <Footer />
    </div>
  );
}

export default NotFoundPage;
