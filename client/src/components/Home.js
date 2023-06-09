import React, {useState} from "react";
import Nav from "./Nav";

function Home() {
    const [forumTitle, setForumTitle] = useState("")

    const [ forumDescription, setForumDescription] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        setForumTitle("")
        setForumDescription("")
    }


    return (
        <>
            <Nav />
            <main className="home">
                <h2 className="homeTitle">Create a Forum</h2>
                <form className="homeForm" onSubmit={handleSubmit}>
                    <div className="home__container">
                    <label htmlFor="forum">Title</label>
                    <input 
                            type="text"
                            name="thread"
                            required
                            value={forumTitle}
                            onChange={(e) => setForumTitle(e.target.value)}
                        />
                    <label htmlFor="forum">Description</label>
                        <input 
                            type="text"
                            name="thread"
                            required
                            value={forumDescription}
                            onChange={(e) => setForumDescription(e.target.value)}
                        />
                    </div>
                    <button className="homeBtn">CREATE FORUM</button>
                </form>
            </main>
        </>
    )
}

export default Home;