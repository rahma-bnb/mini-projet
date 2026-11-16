# Application Flask conteneurisée

Petite application web Flask qui répond avec un message d'accueil configurable.

## Image Docker Hub

`rahmabnb/app` : versions `1.0.0`, `1.0.1` et alias `1.0` (dernière 1.0.x).

## Lancer l'application (depuis l'image publiée)

    docker run -d --name app -p 5001:5000 -e MESSAGE="Salut" --memory 256m --cpus 0.5 rahmabnb/app:1.0.1

Puis tester :

    curl http://localhost:5001

## Variables d'environnement

| Variable | Rôle | Valeur par défaut |
|---|---|---|
| MESSAGE | Message affiché par l'application | Bonjour depuis un conteneur Docker, v1.0.1 ! |

## Construire l'image soi-même

    git clone <url_du_depot>
    cd mini-projet
    docker build -t rahmabnb/app:1.0.1 .

## Arrêter et supprimer

    docker rm -f app
