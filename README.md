# Kubernetes-project

![](https://github.com/Nelly-98/Kubernetes-project/blob/main/projet-kubernetes.png)

##  déployer de manière sécurisée trois micro-services essentiels :

- Un service FastAPI pour l'application principale.
- Un service PostgreSQL comme base de données.
- PGAdmin pour l'administration des bases de données.

## Stratégie de Déploiement :

- Définition des objets Kubernetes pour optimiser le déploiement des micro-services.
- Création du Dockerfile pour le service FastAPI.
- Utilisation de StorageClass de Rancher pour un stockage partagé de 10 Gi.
- Configuration de trois réplicas de l'application, avec un HorizontalPodAutoscaler pour gérer la montée en charge entre 3 et 6 Pods, basée sur une utilisation CPU de 70%.

## Déploiement Multimodal :

Le déploiement a été réalisé à travers trois méthodes pour démontrer la flexibilité et la robustesse de Kubernetes :

- Fichiers YAML (dans le dossier yaml-standard) standards dans le Namespace standard.
- HELM (dans le dossier helm) dans le Namespace helm.
- Kustomize (dans le dossier kustomize) dans le Namespace kustomize.