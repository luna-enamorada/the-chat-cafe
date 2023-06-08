import React, { useEffect, useState } from "react";
import User from "./User";

function HomePage() {

  const [user, setUser] = useState(null)


  
  return (
    <div>
      <h2> uhh meow? </h2>
      {/* <h2> {user.username} </h2> */}
    </div>
  )
}

export default HomePage;