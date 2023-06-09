import React, {useState} from 'react'
import {useHistory} from 'react-router-dom'

const initialState = {
    name: ' ',
    email: ' '
}

function Authentication({updateUser}) {
    const [signUp, setSignUp] = useState(false)
    const history = useHistory()

    const [formState, setFormState] = useState(initialState)

    const [formErrors, setFormErrors] = useState(null)

    const renderFormErrors = () => {
        return formErrors.map(error => <>{error}</>)
    }

    const changeFormState = (event) => {
        const {name, value} = event.target
        const updateFormState = {...formState, [name]: value}
        setFormState(updateFormState)
    }

    const handleClick = () => setSignUp((signUp) => !signUp)

    const userLoginOrCreation = (event) => {
        event.preventDefault()
        
        const postRequest = {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
                'accept': 'application/json'
            },
            body: JSON.stringify(formState)
        }
        
    }
}