import React, { useState, useEffect } from "react";

function ForumList(){
  const [ forum, setForum ] = useState([])
  
  useEffect( () => {
    fetch("http://127.0.0.1:5555/forums")
    .then((r) => r.json())
    .then( data => setForum(data) ) }, []
  )

    const renderForumCards = forum.map( forum => 
      <div>
          <h2> {forum.title} </h2>
          <h3> {forum.description} </h3>
      </div>
    )

    return (
      <main > 
        <div className="forum-list">
          <h1 className="all-forum"> </h1>
            {renderForumCards}
        </div>
      </main>
    )

}

export default ForumList;