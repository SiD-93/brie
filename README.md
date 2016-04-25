# Brie - an automaton for the chronically lazy and the ever forgetful.

Presently in beta, this scraper pulls data from websites as per user preference.
Episodes of 720p are queued by default and settings for quality are on the way.


## Dependencies
* requests - A Pythonic library for HTTP/1.1 requests.
* BeautifulSoup - Python library for scraping.
* json - Config file support.
* os - Read/write from/to directories.
* Possibly many more...

# v0.9.1
* Pulls data from one website (highly breakable).
* Prints data to STDOUT, in no formatted way (working on reducing this).
* JSON supported for config files.

# v0.9.3
* Much better config file format.
* Flexible reading from and writing to config file.
* Using default `.config` directory for config file storage.

#TODO
- [x] Quality selector.
- [ ] Daemonize or run with cron.
- [ ] Add scraper and downloader.
- [ ] UI or go OG with only CLI?
