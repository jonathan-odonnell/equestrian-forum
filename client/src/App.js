import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import './App.css';
import { Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';

function App() {
  return (
    <React.Fragment>
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/forum/" />
          <Route exact path="/forum/:slug/" />
          <Route component={Error} />
        </Switch>
    </React.Fragment>
  );
}

export default App;
