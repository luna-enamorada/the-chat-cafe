import React from "react";
import { useParams } from "react-router-dom";

function User({member}){
    const { username, avatar, bio } = member;

    return (
      <div>
          <h2> User: {username} </h2>
      </div>
    )
}

export default User;