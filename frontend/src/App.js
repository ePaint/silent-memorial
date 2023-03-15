import axios from 'axios';
import React, { Component } from 'react';
import './App.css';
import CustomModal from './components/Modal';
import Intro from './components/Intro';
import Posts from './components/Posts';
import Footer from './components/Footer';
import Copyright from './components/Copyright';


function App(){

  return (
    <div id="wrapper" className="fade-in">
      <Intro />
      <Posts />
      <Footer />
      <Copyright />
    </div>
  );
}

export default App;
