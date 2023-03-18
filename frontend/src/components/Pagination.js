import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './Pagination.css';

function Pagination({ data, fetchPostList }) {
    const maxPagesQuickAccess = 3;

    const getPage = ({ page=1, decorate=false, activePage=null, baseClass='page', label=null } = {}) => {
        let className = baseClass;

        if (decorate) {
            if (page === activePage) className += ' active';
            if (Math.abs(page - activePage) > 1) className += ' tail';
        }

        if (!label) label = page;

        return (<a  href="#main"
                    onClick={() => fetchPostList(page)} key={'page-' + page}
                    className={className}>
                    {label}
                </a>);
    }

    const getDivisor = () => {
        return (<span className="extra">&hellip;</span>);
    }

    const getPrev = () => {
        if (data.page_prev) return (getPage({ page: data.current_page - 1, baseClass: 'previous', label: 'Prev' }));
    }

    const getNext = () => {
        if (data.page_next) return (getPage({ page: data.current_page + 1, baseClass: 'next', label: 'Next' }));
    }

    const getPages = () => {
        const output = [];
        const startPage = Math.max(1, data.current_page - maxPagesQuickAccess + 1);
        const endPage = Math.min(data.total_pages, data.current_page + maxPagesQuickAccess - 1);

        if (startPage > 3) {
            output.push(getPage({ page: 1 }));
            output.push(getDivisor());
        } else if (startPage > 2) {
            output.push(getPage({ page: 1 }));
            output.push(getPage({ page: 2 }));
        } else if (startPage > 1) {
            output.push(getPage({ page: 1 }));
        }

        for (let i = startPage; i <= endPage; i++) {
            output.push(getPage({ page: i, decorate: true, activePage: data.current_page }));
        }

        if (data.total_pages - data.current_page > 4) {
            output.push(getDivisor());
            output.push(getPage({ page: data.total_pages }));
        } else if (data.total_pages - data.current_page > 3) {
            output.push(getPage({ page: data.total_pages - 1 }));
            output.push(getPage({ page: data.total_pages }));
        } else if (data.total_pages - data.current_page > 2) {
            output.push(getPage({ page: data.total_pages }));
        }

        return output;
    }

    return (
        <footer>
            <div className="pagination">
                {getPrev()}
                {getPages()}
                {getNext()}
            </div>
        </footer>
    )
}

export default Pagination