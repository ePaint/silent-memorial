import axios from 'axios';
import React, { Component } from 'react';
import './App.css';
import CustomModal from './components/Modal';
import Intro from './components/Intro';
import Posts from './components/Posts';
import Footer from './components/Footer';
import Copyright from './components/Copyright';
import overlay from './images/overlay.png';
import bg from './images/bg.jpg';


function App() {
    const style = { backgroundImage: `url(${overlay}), linear-gradient(0deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)), url(${bg})` };

    return (
        <div id="wrapper" className="fade-in" style={style}>
            <Intro />
            <Posts />
            <Footer />
            <Copyright />
        </div>
    );
}

export default App;
