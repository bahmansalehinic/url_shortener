def is_from_browser(user_agent):
    return user_agent.browser in [
        "camino",
        "chrome",
        "firefox",
        "galeon",
        "kmeleon",
        "konqueror",
        "links",
        "lynx",
        "msie",
        "msn",
        "netscape",
        "opera",
        "safari",
        "seamonkey",
        "webkit",
    ]