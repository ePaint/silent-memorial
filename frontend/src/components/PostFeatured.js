function PostFeatured({ post={}, index=1, fetchPost=null } = {}) {
    return (
        <article className="post featured">
            <header className="major">
                <span className="date">{post?.death_date}</span>
                <h2><a href="#">{post?.title}</a></h2>
                <p className="preview-content" dangerouslySetInnerHTML={{__html: post?.featured_content}}></p>
            </header>
            
            <a href="#" className="image main"><img src={require("../images/pic0" + index + "-alt.jpg")} alt="" /></a>
            <ul className="actions special">
                <li><a href="#main" onClick={() => fetchPost(post.post_id)} className="button large">Full Story</a></li>
            </ul>
        </article>
    )
}

export default PostFeatured