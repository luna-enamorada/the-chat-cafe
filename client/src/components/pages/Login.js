import React, {useState} from "react";
import {Link} from "react-router-dom";
import { useHistory } from "react-router-dom";
import PropTypes from 'prop-types';

async function logininUser(credentials) {
    return fetch('http://127.0.0.1:5555/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
    .then(data => data.json())
}

function Login({setToken}) {
    const [email, setEmail] = useState("")
    const [_password, setPassword] = useState("")

    const handleSubmit = async e => {
        e.preventDefault()
        const token = await logininUser({
            email,
            _password
        });
        setToken(token);
    }

    return (
        <main className="login">
            <h1 className="loginTitle">Log into your account</h1>
            <form className="loginForm" onSubmit={handleSubmit}>
                <label htmlFor="email">Email Address</label>
                <input
                    type='text'
                    name='email'
                    id='email'
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor="password">Password</label>
                <input 
                    type="password"
                    name="password"
                    id='password'
                    required
                    value={_password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button className="loginBtn">SIGN IN</button>
                <p>
                    Don't have an account? <Link to='/register'>Create an account</Link>
                </p>
            </form>
        </main>
    )
}

Login.propTypes = {
    setToken: PropTypes.func.isRequired
}

export default Login;