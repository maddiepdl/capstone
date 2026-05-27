# Surf Product Catalog — Capstone Project

A full-stack product management system with an AI assistant. Users can manage a surf gear inventory through a web UI while an n8n AI bot answers natural language questions about the catalog in real time.

**Live site:** https://capstone-maddie.pathway4.click

---

## Tech Stack

| Layer | Technology |
|---|---|
| Database | PostgreSQL |
| Backend | Python, Flask, psycopg2 |
| Frontend | React 18, Vite |
| AI Automation | n8n, AWS Bedrock |
| Deployment | AWS EC2 |

---

## Features

- Add, view, and edit surf products (name, price, quantity) via a clean dashboard UI
- AI chat assistant embedded in the app — ask questions like *"How many wetsuits do we have in stock?"* and get a live answer pulled directly from the database
- Hawaii / surf theme with frosted glass cards and ocean background
- Fully deployed on AWS with a custom subdomain

---

## Project Structure

```
capstone/
├── app.py            # Flask server — API routes + serves the React build
├── database.py       # PostgreSQL connection and table setup
├── requirements.txt  # Python dependencies
├── .env              # DB credentials (not committed)
└── dist/             # React production build (served by Flask)
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/get_products` | Fetch all products |
| POST | `/add_product` | Add a new product |
| PUT | `/update_product/<id>` | Update a product by ID |

---

## Database Schema

**Table: `product`**

| Column | Type | Description |
|---|---|---|
| id | SERIAL | Auto-assigned unique ID |
| name | VARCHAR(100) | Product name |
| price | DECIMAL | Price |
| quantity | INTEGER | Units in stock |

---

## n8n AI Workflow

The n8n workflow connects directly to the PostgreSQL database via a Postgres tool attached to an AI Agent node (AWS Bedrock). When a user sends a message through the embedded chat widget, the agent queries the `product` table live and responds conversationally.

Chat widget webhook:
`https://automations.pathway4.click/webhook/9ea2760f-9cc9-443d-91c0-676e65236b87/chat`

---

## Running Locally

### Backend

```bash
pip install -r requirements.txt
# Add your PostgreSQL credentials to a .env file
python app.py
```

### Frontend (development)

```bash
cd frontend_cap
npm install
npm run dev
```

### Frontend (production build)

```bash
npm run build
# Copy dist/ output into the Flask project root
```

---

## Deployment

The React app is compiled with `npm run build` and served as static files directly by Flask on an AWS EC2 instance. The app is accessible at:

**https://capstone-maddie.pathway4.click**
