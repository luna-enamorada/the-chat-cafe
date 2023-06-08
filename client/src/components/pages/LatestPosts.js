import { Link } from "react-router";
import React, { useState, useEffect } from "react";

function LatestPosts(){
  const [ post, setPosts ] = useState([])
  
  useEffect( () => {
    fetch("http://127.0.0.1:5555/posts")
    .then((r) => r.json())
    .then( data => setPosts(data) ) }, []
  )
  
    const renderPosts = post.map( post => 
      <div>
        <h2> {post.title} </h2>
        <h3> {post.content} </h3>
      </div>
    )

    return (
      <main > 
        <div className="member-list">
          <h1 className="all-posts"> </h1>
            {renderPosts}
        </div>
      </main>
    )

}

export default LatestPosts;