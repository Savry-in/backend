# Savry Backend &middot; ![Status](https://img.shields.io/badge/Status-Under%20Development-orange)

> **A Django-powered backend for the Savry Kitchen Inventory Manager**, providing secure data storage, user authentication, real-time notifications, and seamless integrations with external services like barcode scanning and CockroachDB.

## Overview

The **Savry Backend** is the core engine that handles all server-side logic for the Savry platform. It offers RESTful APIs (or GraphQL, if you choose) for our React (web) and Flutter (mobile) clients, ensuring a unified experience and consistent data management across all devices.

## Features (Planned)

- **User Management**  
  Register, login, and profile updates. Supports custom user models, households/family sharing, and role-based permissions if needed.

- **Inventory Management**  
  Create, update, and delete kitchen items, track quantities, and monitor expiry dates.

- **Notifications**  
  Automated alerts for low-stock or expiring items. Configurable to send in-app or email notifications.

- **Barcode Scanning Integration**  
  Hooks to external APIs for scanning and retrieving product data. Items can be added to inventory by scanning barcodes.

- **CockroachDB Integration**  
  Scalable, fault-tolerant database setup, ensuring consistent performance and reliability.

## Tech Stack

- **Language:** Python (3.9+ or 3.10+ recommended)
- **Framework:** Django (with Django REST Framework if building a RESTful API)
- **Database:** CockroachDB (wire-compatible with PostgreSQL)
- **Authentication:** Django’s built-in auth or JWT-based, depending on your design
- **Deployment:** GitHub Actions for CI/CD, containerization optional (Docker)
- **Hosting (Future):** Possibly AWS, Heroku, or any other cloud provider

## Development Status

This project is in the **early stages of development**. Key modules (user management, inventory logic, notifications) are being designed and implemented. Expect frequent updates and possible breaking changes until we reach a stable release.

