# Otémé

Ce petit programme – ou service – naît d'un problème simple : aucun client météo ne donne accès aux prévisions passées ! Or personnellement, pour savoir comment je m'habille le matin, je pointe mon nez dehors et je décide des choix d'aujourd'hui par rapport aux choix de la veille, sachant les changements météo entre hier et demain.

Parce qu'on est jamais mieux servi que par soi-même, voilà un petit progamme qui permet de
1. récupérer les prévisions météos du jour et de les sauvegarder dans un fichier `.json`
2. calculer les différences avec les prévisions passées dans un autre fichier `.json`.

Ce programme est executé toutes les heures grâce à une Github Action. La localisation de la météo est à Paris, mais elle peut être changée facilement dans le programme.
