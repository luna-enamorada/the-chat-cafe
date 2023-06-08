import { Link } from "react-router-dom";
import MemberList from "./pages/MemberList";
import HomePage from "./pages/HomePage";
import ForumList from "./pages/ForumList";

import React, {useState} from "react";
import {
  Nav,
  NavLink,
  Bars,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from './NavbarElements';


function Navbar({ selectedPage, setSelectedPage }) {

  return (
    <Nav className="item-menu">
      <Bars />
      <NavMenu>
          <NavLink to="/" > 
          <h1> The Chat Cafe </h1>
          </NavLink>

          <NavLink to="/users"
          > Members
          </NavLink>

          <NavLink to="/forums" >
          Forums
          </NavLink>

          <NavLink to="/posts" >
          All Posts
          </NavLink>
      </NavMenu>
    </Nav>
  );
}

export default Navbar;
