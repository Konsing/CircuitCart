# Base stage: common setup
FROM node:14-alpine AS base
WORKDIR /usr/src/app
COPY package.json package-lock.json* ./
RUN npm install
COPY . .

# Development stage: runs the dev server with hot reloading
FROM base AS development
EXPOSE 3000
CMD [ "npm", "start" ]

# Production stage: builds static assets and serves them via a static file server
FROM base AS production
RUN npm run build
# Install a lightweight static file server (using 'serve')
RUN npm install -g serve
EXPOSE 5000
CMD [ "serve", "-s", "build", "-l", "5000" ]
