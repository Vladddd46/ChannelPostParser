<h3>Introduction</h3>
<p>The purpose of this project is to fetch posts from social media services/messangers/etc. like Telegram, Whatsup, Twitter and so on.</p>
<p>The posts are retrieved from selected in 'config.py' service and also processed by selected function in 'config.py'. The format of retrieved posts is JSON.</p>
<p>The projects is designed so you could easily extend it with new services. Moreover you could redefine function for further processing of fetched posts.<br>For more info ./docs</p>

<h3>Supported services</h3>
<ul>
  <li>Telegram</li>
</ul>

<h3>Quick Start</h3>
<ul>
  <li>python version >= 3.8.18</li>
  <li>pip install -r requirements.txt</li>
  <li>python main.py</li>
</ul>


<h3>Project structure</h3>
<ul>
  <li>docs - project`s documentation.</li>
  <li>examples - files with example code. use run_examples.py to run them.</li>
  <li>src - source code</li>
  <ul>
    <li>adaptors - adopts external objects into entities.</li>
    <li>data_processors - defines how data be processed after being fetched.</li>
    <li>entities - project`s entities like channel, post, user, etc.</li>
    <li>entrypoints - entrypoints to services like ftp server, posts fetcher, etc.</li>
    <li>fetchers - classes responsible for fetching data from services.</li>
    <li>utils - helper functions.</li>
  </ul>
  <li>tmp - contains files like *.session, creats.py, logs, retrieved data.</li>
  <ul>
    <li>logs - logs are stored here.</li>
    <li>retrieved_data - fetched posts will be stored here. (in case config.py has proper configuration)</li>
    <li>creds.py - credentials for the project.</li>
  </ul>
</ul>
