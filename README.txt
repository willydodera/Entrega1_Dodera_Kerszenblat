Sistema de Registro de Horario
-----------------------------------------------------------------------------------------------------------------
Desarrollado por Magali Kerszenblat y William Dodera
-----------------------------------------------------------------------------------------------------------------
Descripción del Proyecto:

Creamos una aplicación web que permite el registro de horario de ingreso y egreso de empleados en una compañia. 
Los usuarios en principio se encuentran con una pantalla de presentación de las distintas funcionalidades.
Si el usuario no está registrado deberá hacer click en "Crear usuario".
Una vez registrado, ya podrá ingresar y egresar, quedando registrados en la base de datos la fecha y
el horario.
Si el empleador desea observar el horario en el que ingreso/egreso alguno de sus empleados, solo deberá 
dirigirse a la sección "Registro de horas" y colocar el usuario de dicho empleado.
-----------------------------------------------------------------------------------------------------------------
Readme:

*Abrir la carpeta del proyecto desde visual studio code

*Abrir la terminal

*Instalar:
		Python        3.10.5
		pip           22.1.2
		virtualenv    20.14.1

*Activar el entorno virtual: dir> myvenv/Scripts/activate

*Instalar los requerimientos: dir> pip install -r requirements.txt

Una vez que todo este instalado correctamente:

*Moverse al directorio del proyecto: dir> cd final

*Para ejecutar se debe correr el comando: dir> python manage.py runserver

*Abrir el navegador y colocar en la url la ip del local host.

*Lo primero que se va a observar es la pantalla de inicio, la principal. Desde
la misma se puede ir a las distintas funcionalidades.

*Ingresar al formulario donde dice "Crear usuario":
  -Rellenar los campos para registrar el nuevo usuario.

*Luego ir a la seccion de "Ingresar":
  -Colocar el usuario y contraseña creados y click en "Enviar"

*Luego ir a la seccion de "Egresar":
  -Repetir pasos punto anterior 

*Por ultimo ir a la seccion registro de horas:
  -Colocando el usuario y se podra visualizar la fecha y hora del ingreso/egreso del usuario.
