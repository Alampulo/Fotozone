# FOTOZONE
#### Description
This is my personal gallery website where you can see photos that i have uploaded.

# Author
 Juma Bryan

## As A user you can :
* View different photos that interest me.
* Click on a single photo to expand it and view the details of the photo.
* View different categories of photos.
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Usage example

1. Open the website and browse the images.
2. If  image captures your attention  you you can click on it to view in a better size\

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images by Location|



## Development setup

To access  this site Coding system  , you will need to:

1. Clone this repo:
  ```bash
  git clone https://github.com/Alampulo/FOTOZONE
  ```
2. Move to the folder and install requirements
  ```bash
  cd Fotozone
  pip install -r requirements.txt
  ```
3. Create database on psql shell

  psql
  CREATE DATABASE Fotozone;

4. Migrate the database and run the application

  python manage.py migrate
  python manage.py runserver


## Technologies Used
* python3:Django
* Flask :Jinja
* HTML & CSS
* Bootstrap
* Heroku
* Git

## Known Bugs
* There are currently no known bugs. If you experience any feel free to open an issue
or contact me personally.

### Support and contact details
If you have any queries regarding the my site,
Please feel free to contact on [gmail](mailto://jumabryan10@gmail.com) and we will be happy to look into your query

## Licensing
 This Project is under the MIT License 2018
