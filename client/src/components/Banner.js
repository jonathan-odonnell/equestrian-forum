import React from "react";
const Banner = ({ children, title }) => {
  return (
    <div className="banner">
      <h1 className="display-2">{title}</h1>
      {children}
    </div>
  );
};

export default Banner;