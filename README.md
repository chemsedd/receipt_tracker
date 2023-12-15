# Receipt Tracker Project

This repository contains a Django project that includes basic functionality for managing receipts.

## Getting Started

### Installation

#### Clone the repository:

```bash
git clone https://github.com/chemsedd/receipt_tracker.git
cd receipt_tracker
```

#### Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
# or
.\venv\Scripts\activate       # On Windows
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

### Database setup

#### Apply initial migrations:

```bash
python manage.py migrate
```

#### Load sample data using fixtures:

```bash
python manage.py generate_fixtures
```
### Usage

#### Run the app

```bash
python manage.py runserver
```

Visit http://localhost:8000/login in your browser to access the application and login.