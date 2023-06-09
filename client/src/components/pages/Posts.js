import { useParams } from 'react-router-dom';
import React, { useState, useEffect } from "react";

import Comments from '../Comments';

function Posts() {
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/posts/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch post data');
        }
        return response.json();
      })
      .then((data) => {
        setPost(data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [id]);


  if (!post) {
    return <div>Loading posts...</div>;
  }

  return (
    <div className='posts'>
      <h1>{post.title}</h1>
      <h3>{post.content}</h3>
      <h2> Comments: </h2>
      {post.comments.map((comment) => (
            <div className='comments'> 
            <h3>{comment.content}</h3> 
            </div> ))}
        <Comments />
    </div>
  );
}

export default Posts;
