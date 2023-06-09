import React, {useState} from "react";
import {Link} from "react-router-dom";

function Register() {
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [_password, setPassword] = useState("")
    const [avatar, setAvatar] = useState("")
    const [bio, setBio] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        signUp()
        setEmail("")
        setUsername("")
        setPassword("")
        setAvatar("")
        setBio("")
    }

    const signUp = () => {
        fetch("http://127.0.0.1:5555/register", {
            method: "POST",
            body: JSON.stringify({
                email,
                _password,
                username,
                avatar,
                bio
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
        <main className="register">
            <h1 className="registerTitle">Create an account</h1>
            <form className="registerForm" onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input 
                    type="text"
                    name="username"
                    id="username"
                    required
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <label htmlFor="email">Email Address</label>
                <input 
                    type="text"
                    name="email"
                    id="email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor="password">Password</label>
                <input 
                    type="password"
                    name="password"
                    id="password"
                    required
                    value={_password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <label htmlFor="avatar">Avatar</label>
                <input
                    type="avatar"
                    name="avatar"
                    id="avatar"
                    value={avatar}
                    onChange={(e) => setAvatar(e.target.value)}
                />
                <label htmlFor="bio">Bio</label>
                <input 
                    type="bio"
                    name="bio"
                    id="bio"
                    value={bio}
                    onChange={(e) => setBio(e.target.value)}
                />
                <button className="registerBtn">REGISTER</button>
                <p>
                    Have an account? <Link to='/login'>Sign in</Link>
                </p>
            </form>
        </main>
    )
}

export default Register;