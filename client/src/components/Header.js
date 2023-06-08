import React, {useState} from "react";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import MemberList from "./pages/MemberList";
import HomePage from "./pages/HomePage";
import ForumList from "./pages/ForumList";
import LatestPosts from "./pages/LatestPosts";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";


import NavBar from "./NavBar";

function Header() {


  return (
    <Switch>
      <Route exact path ='/' component = {HomePage}/>
      <Route path ='/users' exact component={MemberList} />
      <Route path ='/forums' exact component={ForumList} />

      <Route path ='/posts' exact component={LatestPosts} />
      <Route path ='/register' exact component={null} />

    </Switch>
  );
}


export default Header;
