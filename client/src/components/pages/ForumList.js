import { useParams, useHistory } from 'react-router-dom';
import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

function ForumList() {

  const [forumList, setForumList] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/forums")
      .then((response) => response.json())
      .then((data) => setForumList(data))
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const renderForumPages = forumList.map( forums => (
    <div key={forums.id}>
      <Link to={`/forums/${forums.id}`}>
        <h1>{forums.title}</h1>
      </Link>
      <h3> {forums.description} </h3>
    </div>
  ))

  return (
    <div className='forums'>
      {renderForumPages}
    </div>
  )
  }

export default ForumList;
