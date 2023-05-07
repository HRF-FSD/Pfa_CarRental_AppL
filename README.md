# Pfa_CarRental_AppL


![login interface](https://github.com/HRF-FSD/Pfa_CarRental_AppL/blob/master/logo.png?raw=true)

# EMSICARS Rentals (PFA)

Ceci est une application Desktop qui permet aux administrateurs de gerer leurs voitues pretes à etre louer et leurs employés, ainsi aux employés de traiter les clients et leurs demandes de locations.

## Technologies
   * Python
   * Tkinter
   * MySQL
   
## Technologies
   * Python
   * Tkinter
   * MySQL
   
## Configuration Base de Données
Pour configurer la base de données: 
* ouvrez le fichier connectDB.py .
* Verifer si les infos de la base de données conferment à ceux de votre machine.
* Exécutez le script pour créer la base de données en exécutant la commande suivante : python connectDB.py OU python -m connectDB 
## Utilisation 
Pour lancer l'application, exécutez le fichier login.py.
* Connectez-vous en utilisant votre nom d'utilisateur et votre mot de passe .
* Utilisez les différents menus pour ajouter, afficher, modifier et supprimer des voitures, des employées, des clients et des locations.
* Cliquez sur "LOGOUT" pour vous déconnecter de votre session.
## Fonctionnalités 
L'application offre des fonctionnalités pour gérer vos produits, catégories, employés et fournisseurs.
* **Authentification et autorisation :** l'application dispose d'un système de login pour gérer les accès aux différentes fonctionnalités de l'application. Les utilisateurs doivent s'authentifier pour accéder à leur compte.

* **Gestion des voitures :** le fichier gestion_voitures.py permet aux utilisateurs d'ajouter, supprimer, modifier et rechercher des voitures dans la base de données.

* **Gestion des locations :** le fichier Gestion_Location.py permet aux utilisateurs d'ajouter, afficher et supprimer les locations ainsi d'etablier la facture associée.

* **Gestion des employés :** le fichier gestion_employee.py permet aux utilisateurs d'ajouter, afficher, modifier, supprimer et rechercher des employés dans la base de données.

* **Gestion des clients :** le fichier gestion_clients.py permet aux utilisateurs d'ajouter, afficher, modifier, supprimer et rechercher des clients dans la base de données.

* **LogOut :** l'application dispose d'une fonctionnalité de déconnexion qui permet aux utilisateurs de se déconnecter de leur compte.
## Fichiers associés 
* **login.py :** contient le systeme d'authentification ainsi que l'interface login.
* **menu.py :** Contient le menu d'utilisation ainsi que son interface graphique.
* **connectDB.py :** contient les infos de la base de données ainsi que les commande SQL pour l'ajout aux tables et la creations de ces derniers s'ils n'existent pas.
* **gestion_clients.py :** permet d'effectuer tout les fonctionnalités de gestion des clients et les afficher dans une liste Treeview.
* **gestion_employee.py :** permet d'effectuer tout les fonctionnalités de gestion des employés et les afficher dans une liste Treeview.
* **gestion_voitures.py :** permet d'effectuer tout les fonctionnalités de gestion des voitures et les afficher dans une liste Treeview.
* **Gestion_Location.py :** permet d'effectuer tout les fonctionnalités de gestion des locations et les afficher dans une liste Treeview.
* **functions1.py :** qui affiche les images des voitures à partir d'un API 
* **factureInfo.py :** Qui affiche la facture et le montant à payer par rapport au prix par journée et la durée de pret.
* **carsInfos.py :** Interace qui affiche les infos de la voitures selectionnée.
 


## screenshots
* **login interface**
![login interface](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/login%20page.jpg?raw=true)

* **Menu admin black theme**
![menu B](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/menu%20interface%20black%20theme.jpg?raw=true)

* **Menu admin white theme**
![menu W](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/menu%20interface%20white%20theme.jpg?raw=true)

* **Add client**
![ClientAdd](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/add%20client.jpg?raw=true)

* **Add car**
![CarAdd](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/add%20car.jpg?raw=true)

* **Car Infos**
![CarInfos](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/car%20info.jpg?raw=true)

* **Facture**
![Facture](https://github.com/HRF-FSD/screenshots-PFA/blob/main/screenshots%20PFA/facture.jpg?raw=true)




## Auteurs

- [@HARAF AYMEN](https://github.com/HRF-FSD)
- [@AHMED LAAZIZ ZAKARIA ](https://github.com/ZikoTheBora)
- [@ELGHOUL SANAE](https://github.com/Elghoulsanaa)


## Remerciements 
Cher M. Ayoub Charef,

Je tiens à vous exprimer ma profonde gratitude pour l'encadrement que vous nous avez offert. Votre expertise, votre patience et votre dévouement ont été d'une grande aide pour nous. 
râce à votre encadrement, j'ai pu acquérir de nouvelles compétences tant que niveau des technologies utilisés q'au niveau des compétences de recherche de l'information.

Un grand merci à nouveau pour vous Mr [CHAREF Ayoub](https://www.linkedin.com/in/ayoub-charef-531897128/).
cordialement,
* HARAF Aymen
* AHMED LAAZIZ Zakaria
* ELGHOUL Sanae.
