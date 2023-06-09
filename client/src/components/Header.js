import React from "react";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import MemberList from "./pages/MemberList";
import HomePage from "./pages/HomePage";
import ForumList from "./pages/ForumList";
import LatestPosts from "./pages/LatestPosts";
import Register from "./pages/Register";
import Login from "./pages/Login";
import useToken from "./useToken";
import Forum from "./pages/Forum"
import Posts from "./pages/Posts"

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
