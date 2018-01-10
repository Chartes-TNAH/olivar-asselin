# olivar-asselin
Corpus d'échanges épistolaires d'Olivar Asselin




Référent : @ponteineptique

- Difficulté : 5/10
- Répétitivité : 7/10
- Schéma à utiliser : Lire plus bas
- Minimum à convertir : les correspondances.

## Notes du référent

À partir de [des sources d'Asselin](https://fr.wikisource.org/wiki/Auteur:Olivar_Asselin) , il faudra capitainiser les documents c'est à dire:

- avoir choisi un schéma cohérent d'encodage TEI de l'ensemble des textes
  - la réalisation d'un schéma tangible (encodé dans un RelaxNG par exemple) est un plus
- décider des identifiants des textes
- encoder les métadonnées des documents (teiHeader) et dans les fichiers `__cts__.xml`
  - Y compris l'ensemble des métadonnées DC pour les oeuvres via cpt:structured-metadata
- adapter le code TEI pour qu'il soit compatible avec les guidelines CapiTainS
- Ajouter le fichier pour faire tourner HookTest sur Travis


