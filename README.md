# 🎬 Movies Backend API

Un projet backend de gestion de films développé pour mon portfolio. Cette API permet de gérer une base de données de films avec des fonctionnalités CRUD (Create, Read, Update, Delete), d'authentification des utilisateurs et de recherche.

## 🚀 Fonctionnalités

- 🔐 Authentification et autorisation (JWT ou autre)
- 🎥 CRUD complet sur les films (titre, réalisateur, année, genre, description, etc.)
- 🔍 Recherche et filtrage des films par titre, genre, année
- 📦 API RESTful documentée
- 🧪 Tests unitaires et d’intégration
- 📈 Statistiques simples (ex: nombre de films par genre)

## 🛠️ Technologies utilisées

- **Langage** : Python / Node.js / [ton langage ici]
- **Framework** : FastAPI / Express.js / Django REST Framework / [ton framework ici]
- **Base de données** : PostgreSQL / MongoDB / SQLite
- **ORM / ODM** : SQLAlchemy / Mongoose / Prisma
- **Authentification** : JWT / OAuth2
- **Tests** : Pytest / Jest / [autre outil de test]
- **Documentation** : Swagger / Redoc

## 📦 Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/ton-utilisateur/movies-backend.git
   cd movies-backend

### Crée un environnement virtuel (si Python) :
- python -m venv env
source env/bin/activate  # ou env\Scripts\activate sur Windows

### Installe les dépendances :
- pip install -r requirements.txt  # ou npm install
### Lance le serveur :
- uvicorn main:app --reload  # ou npm run dev
📄 Documentation de l'API

### Accès automatique via Swagger à l'adresse :


- http://localhost:8000/docs

### 🧪 Lancer les tests

- pytest  # ou npm test
### ✍️ Auteur
- Josias [NTEME]

[(https://www.linkedin.com/in/josias-nteme-95757721a/)]

Contact : [josias76nteme@gmail.com]

### 📁 Structure du projet (exemple)

movies-backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   └── main.py
│
├── tests/
├── requirements.txt
├── .env
└── README.md
📝 Licence

