import { Link } from "react-router-dom";
import MemberList from "./pages/MemberList";
import Home from "./Home";
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
import { Switch } from "react-router-dom/cjs/react-router-dom.min";


function Navbar({ selectedPage, setSelectedPage }) {

    return (
    <Switch>
        <Nav className="item-menu">
        <NavMenu>

            <NavLink to="/" > 
            <h1> The Chat Cafe </h1>
            </NavLink>

            <NavLink to="/register" >
            Register
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

            <NavBtn>
            <NavBtnLink to='/login'>Log In</NavBtnLink>
            </NavBtn>

        </NavMenu>
        </Nav>
    </Switch>
    );
}

export default Navbar;