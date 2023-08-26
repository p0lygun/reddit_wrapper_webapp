# reddit_wrapper_webapp
A project for an internship, the app is split into two parts, the backend and the frontend.
The backend is a **FastAPI** app that uses the Reddit API to get the top 10 posts from a subreddit and the frontend is a **Plain HTML webpage that uses TailwindCSS** that displays the posts.

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/p0lygun/reddit_wrapper_webapp/main.svg)](https://results.pre-commit.ci/latest/github/p0lygun/reddit_wrapper_webapp/main)


## How to run
- ### locally
  - Make sure you have docker installed.
  - Clone the repo
  - run `docker-compose up --build`
  - The app should be running on `0.0.0.0:8080`
- ### Production
  - Already deployed on a VPS, you can access it [here](https://probe-reddit.vibhakar.dev/)

## Tech Stack
  - ### Backend
    - FastAPI
    - Docker
  - ### Frontend
    - TailwindCSS
    - JS
    - HTML
