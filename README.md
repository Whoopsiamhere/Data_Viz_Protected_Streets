# NYC Protected Streets

An interactive student project by Yannan (Mike) Zhu. Guess what “protected” means, explore NYC street segments, and compare when protection ends across boroughs.

## Publish on GitHub Pages

1. Unzip this project. Upload all files and folders inside it to the root of your GitHub repository. Keep the data, photos and vendor folders intact.
2. In GitHub, open Settings → Pages. Choose Deploy from a branch, then main and / (root). Save.
3. GitHub will show your website URL when publication finishes.

No API key, npm install or build step is required. Upload the extracted files, not the ZIP itself.

## Run locally

From the folder containing index.html, run:

    python3 -m http.server 8000

Open http://localhost:8000. Double-clicking index.html may prevent the browser from loading the data.

## Edit

- index.html: page text and structure
- style.css: black-and-white appearance and mobile layout
- learn.js: opening question and explanation
- app.js: Canvas map, D3 chart, search, filters and street details
- core.js: date windows, filtering and map projection
- prepare_data.py: data preparation
- data/: source snapshot, cleaned CSV, map data and cleaning audit
- photos/: real street photo and attribution
- vendor/: bundled D3 library

The map and bar chart are rendered in JavaScript. Python is used to prepare the data. The photograph is a real photograph, not an AI-generated image.

## Data and limitations

The site preserves the September 23, 2026 snapshot used in the class project, containing 24,404 active records. The time slider counts forward from that snapshot date, not the date of a visitor's browser. Counts are dataset records, not unique street names or total road mileage. The chart shows each borough's share ending within the chosen window; its count toggle changes the measure. Selecting a bar filters the map; selecting a street highlights its borough.

Protected streets are newly resurfaced or reconstructed streets with restrictions on excavation, normally for five years. The designation is not a crime or traffic-safety rating. Exceptions may apply. The site is an educational snapshot, not a permit or construction decision tool. Original source and definition links are in the page footer. NYC DOT warns that the source may contain errors or omissions.

## Street photos

Click any street for an Open Street View link. This opens Google Maps at the segment midpoint, requesting the nearest available panorama. Coverage and image dates vary; a panorama is not guaranteed for every segment. The website does not embed or scrape Google imagery.

Use “See Astor Place photo” to see an actual Astor Place photograph directly on the page. It was taken in 2019, before the dataset snapshot. Credit: Jim.henderson, CC BY-SA 4.0. See photos/README.md. Keep attribution and licensing when redistributing the image.

The opening is a three-step flow: guess, read the explanation, and enter the map. A skip link and a return-to-explanation button are available. Street View runs on Google’s website; its loading or black-screen behavior is outside this static site’s control. Use the Google Maps link if the panorama does not load.


## October 28 update

The map and borough chart now sit together. Repeated counters, the street list, quick time presets and the only-soon checkbox were removed. A single month slider updates both views. Snapshot and protection dates are available in expandable notes. Street details and the Astor Place photo appear in the side panel. Searching reveals a compact segment selector (first 100 matches), also usable with a keyboard. Clicking an already selected borough in the chart returns to all boroughs.

## Update an existing GitHub Pages site

Keep your existing repository and Pages settings. Upload index.html, style.css, app.js, learn.js and README.md from this package to the repository root, replacing the files with the same names. The data, photos, vendor, core.js and favicon.svg have not changed. Commit all four application files together to avoid mixing versions. GitHub Pages will rebuild at the same URL. If the old version remains visible after deployment, use Ctrl+Shift+R.
