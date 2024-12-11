import React, { useState, useEffect } from 'react';

export const Navigation = () => {
  const Links = [
    { name: "HOME", link: "/" },
    { name: "SERVICE", link: "/service" },
    { name: "ABOUT", link: "/about" },
    { name: "BLOG'S", link: "/blogs" },
    { name: "CONTACT", link: "/contact" },
  ];

  const [open, setOpen] = useState(false);
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    // Check user authentication
    if (localStorage.getItem("access_token")) {
      setIsAuth(true);
    } else {
      setIsAuth(false);
    }
  }, []);

  // Inline CSS
  const styles = {
    navContainer: {
      boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
      position: "fixed",
      top: 0,
      left: 0,
      width: "100%",
      backgroundColor: "#fff",
      zIndex: 1000,
    },
    navBar: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "10px 20px",
    },
    brand: {
      fontWeight: "bold",
      fontSize: "24px",
      display: "flex",
      alignItems: "center",
      color: "#4B5563",
      textDecoration: "none",
    },
    icon: {
      fontSize: "30px",
      color: "#4F46E5",
      marginRight: "10px",
    },
    menuIcon: {
      fontSize: "30px",
      cursor: "pointer",
      display: "block",
    },
    linksContainer: (isOpen) => ({
      display: isOpen ? "block" : "none",
      position: "absolute",
      top: "60px",
      left: 0,
      width: "100%",
      backgroundColor: "#fff",
      textAlign: "center",
      padding: "10px 0",
      boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
    }),
    link: {
      textDecoration: "none",
      color: "#4B5563",
      margin: "10px",
      fontSize: "18px",
      transition: "color 0.3s",
    },
    linkHover: {
      color: "#9CA3AF",
    },
    desktopLinks: {
      display: "flex",
      alignItems: "center",
    },
    button: {
      backgroundColor: "#4F46E5",
      color: "#fff",
      padding: "10px 20px",
      borderRadius: "5px",
      border: "none",
      cursor: "pointer",
      fontSize: "16px",
      marginLeft: "10px",
    },
    homepage: {
      marginTop: "80px", // Adds space below the fixed navbar
      padding: "20px",
      fontFamily: "Arial, sans-serif",
    },
  };

  return (
    <div>
      {/* Navbar */}
      <div style={styles.navContainer}>
        <div style={styles.navBar}>
          <a href="/" style={styles.brand}>
            <span style={styles.icon}>
              <ion-icon name="logo-ionic"></ion-icon>
            </span>
            FAAN ACADEMY LOGO
          </a>
          <div onClick={() => setOpen(!open)} style={styles.menuIcon}>
            <ion-icon name={open ? "close" : "menu"}></ion-icon>
          </div>
          <ul style={{ ...styles.desktopLinks, display: "flex" }}>
            {Links.map((link) => (
              <li key={link.name} style={{ listStyle: "none" }}>
                <a
                  href={link.link}
                  style={styles.link}
                  onMouseOver={(e) =>
                    (e.target.style.color = styles.linkHover.color)
                  }
                  onMouseOut={(e) => (e.target.style.color = styles.link.color)}
                >
                  {link.name}
                </a>
              </li>
            ))}
            {isAuth ? (
              <>
                <li style={{ listStyle: "none" }}>
                  <a
                    href="/"
                    style={styles.link}
                    onMouseOver={(e) =>
                      (e.target.style.color = styles.linkHover.color)
                    }
                    onMouseOut={(e) =>
                      (e.target.style.color = styles.link.color)
                    }
                  >
                  
                  </a>
                </li>
                <li style={{ listStyle: "none" }}>
                  <a
                    href="/logout"
                    style={styles.link}
                    onMouseOver={(e) =>
                      (e.target.style.color = styles.linkHover.color)
                    }
                    onMouseOut={(e) =>
                      (e.target.style.color = styles.link.color)
                    }
                  >
                    LOGOUT
                  </a>
                </li>
              </>
            ) : (
              <li style={{ listStyle: "none" }}>
                <a
                  href="/login"
                  style={styles.link}
                  onMouseOver={(e) =>
                    (e.target.style.color = styles.linkHover.color)
                  }
                  onMouseOut={(e) => (e.target.style.color = styles.link.color)}
                >
                  Login
                </a>
              </li>
            )}
          </ul>
        </div>
      </div>

      {/* Homepage Content */}
      <div style={styles.homepage}>
        {/* <h1>Welcome to Designer</h1>
        <p>
          This is the homepage content. Feel free to customize it with your
          details. The navigation bar is fixed at the top, and the content is
          adjusted to remain visible.
        </p> */}
      </div>
    </div>
  );
};

export default Navigation;
