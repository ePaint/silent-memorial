import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './Posts.css';
import PostFeatured from './PostFeatured';
import PostRegular from './PostRegular';
import PostDetailed from './PostDetailed';
import Pagination from './Pagination';

function Posts() {
    const [postData, setPostData] = useState({});
    const [paginatorData, setPaginatorData] = useState({});

    const fetchPost = (post_id) => {
        const url = `http://localhost:8000/api/posts/${post_id}/`;
        console.log('post_id:', post_id, ', url:', url);
        axios.get(url).then(response => {
            console.log(response);
            setPostData({
                ...postData,
                post: response.data,
                showPost: true
            });
        });
    }

    const fetchPostList = (page) => {
        if (!page) page = 1;
        const url = `http://localhost:8000/api/posts/?page=${page}`;
        console.log('page:', page, ', url:', url);
        axios.get(url).then(response => {
            console.log(response);
            setPostData({
                ...postData,
                postList: response.data.results,
                showPost: false
            });
            setPaginatorData({
                ...paginatorData,
                current_page: response.data.current_page,
                total_pages: response.data.total_pages,
                page_prev: response.data.previous,
                page_next: response.data.next
            });
        });
    }

    useEffect(() => fetchPostList(), []);
    
    const getPost = () => {
        return <PostDetailed post={postData.post} fetchPost={fetchPost} />;
    }

    const getPostList = () => {
        const content = [];
        const regularPosts = [];
        postData.postList?.forEach((post, index) => {
            if (index) {
                regularPosts.push(<PostRegular post={post} index={index+1} key={post.post_id} fetchPost={fetchPost} />);
            } else {
                content.push(<PostFeatured post={post} index={index+1} key={post.post_id} fetchPost={fetchPost} />);
            }
        });

        content.push(<section className="posts">{regularPosts}</section>);

        content.push(<Pagination data={paginatorData} fetchPostList={fetchPostList} />);

        return content;
    }

    const getContent = () => {
        if (postData.showPost) {
            return getPost();
        } else {
            return getPostList();
        }
    }

    return (
        <div id="main">
            {getContent()}
        </div>
    )
}

export default Posts