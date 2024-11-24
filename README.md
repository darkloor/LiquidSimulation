This code simulates liquid temperatures in an enclosed space. Run by executing the main.py Python script.
============================================
HOW TO MODIFY THE SIMULATION TO YOUR LIKING
============================================
Everything is that is simulated is defined in the main.py script, and you can edit the objects (config, walls, etc...) to your liking.

Want a bigger surface area on the side that the sun rises? You can do that.
Want the container to be fully enclosed, so no solar heat gathers inside? You can set that, and simulate to see what happens.

Currently Supported Liquids: Water and Isopropnaol

**SUPER IMPORTANT**
Edit your config values to your liking (also set in the main.py script)
- location (desired lon/lat) (IMPACTS SUN POSITIONING, AND THE TEMPERATURE DATA USED)
- start_date (gives the time of year that the historical temperature data will be referenced)
- simulation_time (how long you the output graph to show in SECONDS, default 1 day)
- simulation_timestep (how data points do you want to collect. minutely? hourly?)
- etc...

**Dependencies**
meteostat
pytz
pvlib
pandas
numpy

In case you missed it, run by executing the main.py Python script.