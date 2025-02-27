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

# Production stage: builds static assets and serves them using a lightweight static file server
FROM base AS production
# Accept build-time argument for the API URL
ARG REACT_APP_API_URL
# Set it in the environment so that Create React App can use it during build
ENV REACT_APP_API_URL=${REACT_APP_API_URL}
RUN npm run build
# Use "serve" package to serve static files
RUN npm install -g serve
EXPOSE 3000
CMD [ "serve", "-s", "build", "-l", "3000" ]
