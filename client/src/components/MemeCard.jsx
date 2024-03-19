function MemeCard({ meme }) {

    return (
        <div className="card">

            <img src={meme.img_url} alt={meme.caption} />

            <p>{meme.caption}</p>

            <button>{meme.likes} Likes</button>

            <button>DELETE</button>

        </div>
    )

}

export default MemeCard