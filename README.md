# we-todoapp — Development startup

Quick instructions to start the app in development. This repository contains two services:

- `frontend` (Vue + Vite) — dev server runs inside container on container port `3000`.
- `backend` (FastAPI) — runs on container port `8000`.

## Prerequisites

- Docker (and docker-compose if you prefer)
- (Optional) VS Code devcontainer — this repo includes `.devcontainer/devcontainer.json` for port forwarding.

## Recommended: Start with docker-compose (development)

This approach mounts your working copy into the containers so file changes are reflected instantly.

From repository root:

```bash
# build and start both services (foreground)
docker-compose up --build

# or run in background
docker-compose up -d --build

# follow logs
docker-compose logs -f frontend
docker-compose logs -f backend

# stop and remove
docker-compose down
```

Notes:
- Frontend is published on the host at `http://localhost:3001` (host:container mapping `3001:3000`). Change the mapping in `docker-compose.yml` if you prefer `3000`.
- Backend is published at `http://localhost:8000`.
- The compose file uses bind mounts (`./frontend:/app` and `./backend:/app`) and anonymous volumes for `node_modules` / `__pycache__` to avoid conflicts.

## Alternative: Run containers directly (no compose)

If you prefer not to use `docker-compose`, run each service manually. Important: make sure to mount the correct host directory into the container — mounting the wrong directory (e.g. mounting `./backend` into the frontend container) will hide `package.json` and break startup.

Build images first (from repo root):

```bash
docker build -t frontend ./frontend
docker build -t backend ./backend
```

Run backend (host port 8000):

```bash
# mount host backend source into /app so edits are reflected
docker run -d \
  -v /workspaces/we-todoapp/backend:/app \
  -p 8000:8000 \
  --name backend_container \
  backend
```

Run frontend (host port 3001 -> container 3000):

```bash
docker run -d \
  -v /workspaces/we-todoapp/frontend:/app \
  -p 3001:3000 \
  --name frontend_container \
  frontend
```

If you want to use `3000` on the host instead, change `-p 3000:3000` and visit `http://localhost:3000`.

## Common troubleshooting

- `npm error enoent Could not read package.json`: you mounted the wrong host directory into the frontend container. Remove the container (`docker rm -f frontend_container`), then re-run with `-v /workspaces/we-todoapp/frontend:/app`.
- `Error: Could not import module "main"` / `uvicorn: executable file not found`: ensure the backend image was built with `requirements.txt` present during build, or install requirements inside the container. Using `docker-compose up --build` will rebuild correctly.
- CORS errors: the backend has CORS middleware. If your browser accesses the frontend at `http://localhost:3001`, make sure that origin is allowed in `backend/main.py`'s `allow_origins` list.
- Port mismatch (devserver accessible at `3001` but docker shows `3000`): check host processes (`ps aux | grep vite`) and devcontainer port forwarding. The repo `.devcontainer/devcontainer.json` may forward ports to different host ports.

## Helpful commands

```bash
# remove existing containers
docker rm -f frontend_container backend_container || true

# view running containers
docker ps

# view logs
docker logs -f frontend_container
docker logs -f backend_container
```

If you'd like, I can also add a `make` target or npm scripts to simplify these commands.
