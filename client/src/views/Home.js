import React from 'react';
// import sections
import Hero from '../components/sections/Hero';
import Cta from '../components/sections/Cta';

const Home = () => {

  return (
    <>
      <Hero className="illustration-section-01" />
      <Cta split />
    </>
  );
}

export default Home;