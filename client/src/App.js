import './App.css';
import React from "react";
import {BrowserRouter as Switch, Route, Router} from "react-router-dom";
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";
import Comments from "./components/Comments";

function App() {
  return (
    <div className='App'>
        <Router>
          <Register />
          <Login />
          <Home />
          <Comments />
        </Router>
    </div>
  )
}

export default App;
