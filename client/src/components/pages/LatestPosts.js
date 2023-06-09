import { Link } from 'react-router-dom/cjs/react-router-dom.min';
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
      <Link to={`/forums/${post.id}`}>
        <h1>{post.title}</h1>
      </Link>
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