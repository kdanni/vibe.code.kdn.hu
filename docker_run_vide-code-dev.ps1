docker build -t vibe-code-dev .
docker run --rm -it -v "${PWD}:/app" vibe-code-dev