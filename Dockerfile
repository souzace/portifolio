# ── Stage: serve ─────────────────────────────────────────────────────────────
FROM nginx:1.27-alpine

# Remove default nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy all site content
# (files excluded via .dockerignore: *.py, *.md, Dockerfile, docker-compose.yml, k8s.yml, ideal/, .git)
COPY . /usr/share/nginx/html/

# Override nginx default config with ours (must come after COPY . to win)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Port 80 exposed for k8s Service / docker port mapping
EXPOSE 80

# Healthcheck — mirrors k8s liveness probe
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]
