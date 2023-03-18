function PostDetailed({ post={}, index=1, fetchPost=null } = {}) {
    return (
        <article className="post detailed">
            <header className="major">
                <span className="date">{post?.death_date}</span>
                <h2><a href="#">{post?.title}</a></h2>
                <a href="#" className="image main"><img src={require("../images/pic0" + index + "-alt.jpg")} alt="" /></a>
                <p className="content" dangerouslySetInnerHTML={{__html: post?.content}}></p>
            </header>
        </article>
    )
}

export default PostDetailed