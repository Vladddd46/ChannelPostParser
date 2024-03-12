<h3>Introduction</h3>
<p>The purpose of this project is to fetch posts from social media services/messangers/etc.</p>
<p>The posts are retrieved from services and processed depending on selected function.</p>
<p>The projects is designed so you could easily extend it with new services.<br>For more info ./docs</p>

<h3>Supported services</h3>
<ul>
  <li>Telegram</li>
</ul>

<h3>Project structure</h3>
<ul>
  <li>adaptors - used for convert external module types into project entities.</li>
  <li>data_processors - functions, that define how to process data after being fetched.</li>
  <li>docs - documentation.</li>
  <li>entities - classes, that represent project entities.</li>
  <li>entrypoints - api for specific functionalities like postFetcher, exaternal dbs, etc.</li>
  <li>examples - example files. use run_examples.py to run them.</li>
  <li>fetchers - classes, that is responsible for fetching data from services.</li>
  <li>retrieved_data - where fetched data is stored.</li>
  <li>tmp - contains files like *.session, creats.py, etc.</li>
</ul>
