import React, { Component } from "react";
import { Link } from "react-router-dom";
import { FaBars } from "react-icons/fa";

export default class Navbar extends Component {
  state = {
    isOpen: false
  };
  handleToggle = () => {
    this.setState({ isOpen: !this.state.isOpen });
    console.log(this.state.isOpen)
  };
  render() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">Equestrian Forum</Link>
                <button className="navbar-toggler" type="button" onClick={this.handleToggle}>
                    <FaBars className="nav-icon" />
                </button>
                <div className={this.state.isOpen ? "collapse navbar-collapse show" : "collapse navbar-collapse"}
                id="navbarNav">
                <ul className="navbar-nav ms-auto show">
                    <li className="nav-item">
                        <Link className="nav-link">Home</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link">Forum</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link">Register/Sign In</Link>
                    </li>
                </ul>
                </div>
            </div>
        </nav>
    );
  }
}