Deployment
==========

This project is deployed using Docker and Render, and automated through a GitHub Actions CI/CD pipeline.

CI/CD Pipeline Overview
------------------------

The deployment process is fully automated and consists of three main stages:

1. **Linting, Testing & Coverage**
   - Runs linting using `flake8`.
   - Executes tests using `pytest`.
   - Checks that coverage is at least 80%.

2. **Docker Image Build & Push**
   - Builds a Docker image tagged with `latest` and the commit SHA.
   - Pushes the image to Docker Hub.
   - Only triggered on the `master` branch when tests pass.

3. **Deployment to Render**
   - Triggers a deployment via Render's Deploy Hook.
   - The deployed Render service pulls the latest Docker image from Docker Hub.

Deployment Prerequisites
-------------------------

Ensure the following are configured in your GitHub repository:

- **Secrets** in GitHub (`Settings > Secrets > Actions`):
  - `DOCKER_USERNAME`: Your Docker Hub username
  - `DOCKER_PASSWORD`: Your Docker Hub password or token
  - `RENDER_DEPLOY_HOOK`: Your Render Deploy Hook URL (found in the service settings)
  - `RENDER_API_KEY`: Your Render API key (if applicable)

Docker Hub repository must be:
- Public or properly authenticated
- Tagged as `latest` and commit SHA

Render service must be:
- Configured to use the correct Docker image URL (e.g. `docker.io/username/image:latest`)
- Set to redeploy on hook trigger

Manual Deployment
------------------

To manually trigger a deployment:

1. Push your changes to the `master` branch.
2. GitHub Actions will build and push the Docker image.
3. The pipeline will trigger a new deployment on Render using the hook.

You can also trigger manually from GitHub under `Actions > CI/CD Pipeline > Run workflow`.

Check logs for each step in GitHub Actions or Render's dashboard.

