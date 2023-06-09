import { Link } from "react-router";
import React, { useState, useEffect } from "react";

function MemberList(){
  const [ members, setMembers ] = useState([])
  
  useEffect( () => {
    fetch("http://127.0.0.1:5555/users")
    .then((r) => r.json())
    .then( data => setMembers(data) ) }, []
  )
  
    const renderMemberCards = members.map( member => 
      <div>
          <h2> User: {member.username} </h2>
      </div>
    )

    return (
      <main > 
        <div className="member-list">
          <h1 className="all-members"> </h1>
            {renderMemberCards}
            
        </div>
      </main>
    )

}

export default MemberList;