function Intro() {
    return (
        <>
            <div id="intro">
                <h1>This is<br />
                Massively</h1>
                <p>A free, fully responsive HTML5 + CSS3 site template designed by <a href="https://twitter.com/ajlkn">@ajlkn</a> for <a href="https://html5up.net">HTML5 UP</a><br />
                and released for free under the <a href="https://html5up.net/license">Creative Commons license</a>.</p>
                <ul className="actions">
                <li><a href="#header" className="button icon solid solo fa-arrow-down scrolly">Continue</a></li>
                </ul>
            </div>

            <header id="header">
                <a href="index.html" className="logo">Massively</a>
            </header>

            <nav id="nav">
            <ul className="links">
                <li className="active"><a href="index.html">This is Massively</a></li>
                <li><a href="generic.html">Generic Page</a></li>
                <li><a href="elements.html">Elements Reference</a></li>
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