import './App.css';
import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import {Link} from 'react-router-dom';
import Header from "./components/Header";
import Navbar from './components/NavBar';
import { Switch } from 'react-router-dom/cjs/react-router-dom.min';

function App() {

  return (
    <div className="App">
        <Router>
          <Navbar />
          <Header />
        </Router>
    </div>
  )
}

export default App;
