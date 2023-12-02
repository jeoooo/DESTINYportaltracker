# DESTINYsitetracker

Python script that automates uptime tracking of websites (SSL verified checks), and stores the status in a Pocketbase backend

- Data insertion to pocketbase via py http requests 
- TODO: implement using Python Pocketbase SDKs (early versions are not stable at the moment + minimal documentation)
- TODO: dockerize and deploy via GCP 
- TODO: update intervals (from 30 seconds to 15 or 30 mins)

# Prerequisites

- `Python 3.8`
- `certificates/cacert.pem` - IMPORTANT
- `API_KEY`

# Installation 

```
https://github.com/jeoooo/DESTINYportaltracker.git
cd DESTINYportaltracker
pip install
py main.py or python main.py
```

