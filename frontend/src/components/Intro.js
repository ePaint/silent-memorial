function Intro({ fetchPosts=null } = {}) {
    return (
        <>
            <div id="intro">
                <h1>Silent<br />
                Memorial</h1>
                <p>A place to remember our loved ones.</p>
                <ul className="actions">
                <li><a href="#header" className="button icon solid solo fa-arrow-down scrolly">Continue</a></li>
                </ul>
            </div>

            <header id="header">
                <a href="index.html" className="logo">Silent Memorial</a>
            </header>

            <nav id="nav">
                <ul className="links">
                    <li className="active"><a href="#main" onClick={() => fetchPosts()}>Latest Memorials</a></li>
                    <li><a href="generic.html">Search Memorials</a></li>
                    <li className="signup"><a href="elements.html">Sign Up</a></li>
                </ul>
                
                <ul className="icons">
                    <li><a href="#" className="icon brands fa-twitter"><span className="label">Twitter</span></a></li>
                    <li><a href="#" className="icon brands fa-facebook-f"><span className="label">Facebook</span></a></li>
                    <li><a href="#" className="icon brands fa-instagram"><span className="label">Instagram</span></a></li>
                    <li><a href="#" className="icon brands fa-github"><span className="label">GitHub</span></a></li>
                </ul>
            </nav>
        </>
    );
}

export default Intro