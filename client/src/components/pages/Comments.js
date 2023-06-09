import React, {useState} from "react";

function Comments() {
    const [comment, setComment] = useState("")

    const handleSubmitComment = (e) => {
        e.preventDefault()
        console.log({comment})
        setComment("")
    }

    return (
        <main className="replies">
            <form className="modal__content" onSubmit={handleSubmitComment}>
                <label htmlFor="comment">Comment on the post!</label>
                <textarea 
                    rows={5}
                    value={comment}
                    onChange={(e) => setComment(e.target.value)}
                    type='text'
                    name="comment"
                    className="modalInput"
                />

                <button className="modalBtn">SEND</button>
            </form>
        </main>
    )
}

export default Comments;