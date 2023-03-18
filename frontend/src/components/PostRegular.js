function PostRegular({ post={}, index=1, fetchPost=null } = {}) {
    return (
        <article>
            <header>
                <span className="date">{post?.death_date}</span>
                <h2><a href="#">{post?.title}</a></h2>
            </header>
            <a href="#" className="image fit"><img src={require("../images/pic0" + index + "-alt.jpg")} alt="" /></a>
            <p className="preview-content" dangerouslySetInnerHTML={{__html: post?.short_content}}></p>
            <ul className="actions special">
                <li><a href="#main" onClick={() => fetchPost(post.post_id)} className="button">Full Story</a></li>
            </ul>
        </article>
    )
}

export default PostRegular