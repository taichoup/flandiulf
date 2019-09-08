### Project structure

- `astrocrawl.py`, when run, creates individual JSON files, as well as an aggregate JSON file that can be used by the front-end to display the results
- In `astrocrawl/spiders/` you will find the individual scrapers that are used to get the data on the webpages. Each source website has its own "spider"
- `index.html` is the front-end, and retrieves the JSON files for displaying through jQuery-style Ajax requests

### Testing

The folder `out_tests` contains a set of JSON files that can be used for tests without needing to run the spiders.


### Dependency management
- `pip install -r requirements.txt`