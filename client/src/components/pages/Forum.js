import { useParams } from 'react-router-dom';
import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom/cjs/react-router-dom.min';


function Forum() {
  const { id } = useParams();
  const [forum, setForum] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/forums/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch forum data');
        }
        return response.json();
      })
      .then((data) => {
        setForum(data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [id]);



  if (!forum) {
    return <div>Loading forum...</div>;
  }

  return (
    <div className='forums'>
      <h1>{forum.title}</h1>
      <h3>{forum.description}</h3>
      <div>
        {forum.posts.map((post) => (
          <Link to={`/forums/${forum.id}/posts/${post.id}`} key={post.id}>
            <h3>{post.title}</h3>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Forum;
