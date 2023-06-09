import React, {useState} from "react";
import Nav from "./Nav";

function Home() {
    const [title, setTitle] = useState("")
    const [description, setDescription] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        newForum
        setTitle("")
        setDescription("")
    }

    const newForum = () => {
        fetch("http://127.0.0.1:5555/register", {
            method: "POST",
            body: JSON.stringify({
                title,
                description
            }),
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
        })
        .catch((err) => console.error(err));
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
                            name="title"
                            required
                            value={forum}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                        <label htmlFor="forum">Description</label>
                        <input 
                            type="text"
                            name="description"
                            required
                            value={forum}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    </div>
                    <button className="homeBtn">CREATE FORUM</button>
                </form>
            </main>
        </>
    )
}

export default Home;