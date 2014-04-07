# Manual de Alta de Desarrollador.
Proyecto Despe.ga - Marzo 2014.

![alt text](http://www.despe.ga/static/logo.png)

## Instalación

### Instalar Heroku (Ubuntu)
* sudo apt-get install heroku
* wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

##### OPCIONAL - Crear directorio para almacenar proyectos
* mkdir proyectos
* cd proyectos

### Clonar repositorio y crear branch local.
* git clone https://github.com/facutk/despe.ga.git

### Instalar Virtual Enviroment
* Instalar paquete python-pip. (Desde synaptics, apt-get, etc)
* sudo pip install virtualenv
* virtualenv venv
* source venv/bin/activate

#### Comprobar requerimientos
* cat requirements.txt

#### (No tengo idea que hace)
* pip freeze

#### Instalar requerimientos
* pip install -r requirements.txt

#### Iniciar entorno virtual
* foreman start

### Configurar email y nombre en git
* git config --global user.email "your_mail@example.com"
* git config --global user.name "Your_name"

### Hacer que no pida username y password en todos los commit
* git config --global credential.helper cache
* git config --global credential.helper 'cache --timeout=3600'

### Commitear a github (ejemplo, comittear README.md)
* git add README.md
* git commit -m "Agregamos README.md"
* git push origin master

### Commitear a heroku, version en produccion
* git push heroku master

# Solución de problemas

### Solución cuando queres commitear cambios y dice "Everything up-to-date"
**Posiblemente estes trabajando fuera del branch**

#### Listar Branches Remotos
* git remote show origin

#### Listar Branches Locales
* git branch

**Entre los branches locales dice "no branch"? Estas trabajando fuera del branch.**
**¿Como volver?**

#### Commitear cuando hiciste cambios en detached state (no branch)
* git branch temp
* git checkout master # or any other branch
* git merge temp
* git branch -d temp
