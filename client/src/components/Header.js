import React from "react";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import MemberList from "./pages/MemberList";
import HomePage from "./pages/HomePage";
import ForumList from "./pages/ForumList";
import LatestPosts from "./pages/LatestPosts";
import Register from "./pages/Register";
import Login from "./pages/Login";
import useToken from "./useToken";

function Header() {

  const {token, setToken} = useToken()

  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <Switch>
      <Route exact path ='/' component = {HomePage}/>
      <Route path ='/users' exact component={MemberList} />
      <Route path ='/forums' exact component={ForumList} />

      <Route path ='/posts' exact component={LatestPosts} />
      <Route path ='/register' exact component={Register} />
      <Route path='/login' exact component={Login} />

    </Switch>
  );
}


export default Header;
