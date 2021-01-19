**BUENBIT historical price**

Aplicación creada enteramente con **Python** para obtener, trackear y graficar la evolución de la cotización del par **DAI/ARS** en el exchange **[Buenbit](https://buenbit.com/).**

Para implementar el programa, se deben instalar todas las librerías **Python** necesarias y contar con una cuenta gratuita de **AWS**. Con el servicio de **AWS S3** activado, extraer las credenciales de dicho servicio para poder sincronizar los archivos en la nube y poder ver los gráficos de salida desde Internet.

Estas credenciales deben estar almacenadas en un archivo **.csv** llamado **"rootkey"**.

Una vez configurado el sistema, se debe iniciar con el archivo **"main.py"**, de esta manera correrá de manera perpetua recopilando los datos y ploteando el gráfico de la cotización, subiéndolo al **bucket S3** configurado.

Se recomienda usar el servicio de cómputo en la nube **AWS EC2** para ejecutar el programa de manera ininterrumpida para no tener fallas en el resultado final.

