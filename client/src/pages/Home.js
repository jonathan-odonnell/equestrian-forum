import React from "react";
import { Link } from "react-router-dom";
import Hero from "../components/Hero";
import Banner from "../components/Banner";

const Home = () => {
  return (
    <React.Fragment>
      <Hero>
        <Banner
          title="Equestrian Forum"
        >
          <Link to="/forum/" className="btn-primary">
            Find Out More
          </Link>
        </Banner>
      </Hero>
    </React.Fragment>
  );
};

export default Home