Automated CI/CD Pipeline Using GitHub Actions and Docker

Project Overview

This project demonstrates how to automate the Continuous Integration (CI) and Continuous Delivery (CD) process using GitHub Actions.

Whenever code is pushed to the GitHub repository, GitHub Actions automatically runs the workflow, performs application testing, builds a Docker image, and publishes the image to Docker Hub.

The project also uses Git Commit SHA for Docker image versioning.

Technologies Used

Python (Flask)

Git and GitHub

GitHub Actions

Docker

Docker Hub

Pytest

Project Architecture

Developer → Git Push → GitHub Repository → GitHub Actions → Automated Testing → Docker Image Build → Docker Hub

Project Workflow

1. Application Development

Developed a Python Flask application.

Created automated test cases for the application.

2. Git and GitHub

Managed application source code using Git.

Pushed code changes to the GitHub repository.

Used Git commits to track code changes.

3. GitHub Actions – CI/CD

Configured an automated workflow using GitHub Actions.

Triggered the workflow on push and pull requests to the main branch.

Automatically executed application tests.

Built a Docker image after successful testing.

4. Docker Image Publishing

Built the Docker image automatically through GitHub Actions.

Published the Docker image to Docker Hub.

Used Docker image tags for version identification.

5. Git Commit SHA

Learned how Git generates a unique SHA for every commit.

Used Commit SHA to identify specific code versions.

Studied the difference between latest and Commit SHA Docker image tags.

Key Learnings

Understanding CI/CD pipeline workflow.

Automating application testing.

Building Docker images using GitHub Actions.

Publishing Docker images to Docker Hub.

Understanding Git Commit SHA.

Managing Docker image versions using tags.

Project Outcome

Successfully implemented an automated CI/CD workflow using GitHub Actions to test the Flask application, build Docker images, and publish them to Docker Hub.

Conclusion

This project provided practical experience with CI/CD automation, GitHub Actions, Docker image building, automated testing, and Docker Hub integration.
