## PortScanner

El escáner de puertos de red fue desarrollado en -Python- con fines didácticos, mejorando la comprensión de los procesos que se realizan al momento de ejecutar un escaneo de puertos (ver curso -[Pentesting Fundamentals](https://tryhackme.com/room/pentestingfundamentals)-). En la versión actual el escáner valida los 65535 puertos, este rango puede ser modificado según la discreción del usuario, almacenando los resultados en un archivo de texto. 

### ¿Que es un Python?

[Python](https://es.wikipedia.org/wiki/Python) es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se utiliza a menudo para crear sitios web y software, automatizar tareas y realizar análisis de datos. Python es un lenguaje de propósito general, lo que significa que se puede usar para crear una variedad de programas diferentes y no está especializado para ningún problema específico.

### ¿Que es un Puerto?

En informática, un [puerto](https://es.wikipedia.org/wiki/Puerto_(inform%C3%A1tica)) es una interfaz a través de la cual se pueden enviar y recibir los diferentes tipos de datos. Los puertos están estandarizados en todos los dispositivos conectados a la red, y a cada puerto se le asigna un número. La mayoría de los puertos están reservados para ciertos protocolos; por ejemplo, todos los mensajes del Protocolo de transferencia de hipertexto (HTTP) van al puerto 80. Mientras que las direcciones IP permiten que los mensajes vayan hacia y desde dispositivos específicos, los números de puerto permiten la orientación de servicios o aplicaciones específicas dentro de esos dispositivos.


### ¿Que es un Escáner de puertos?

El término [escáner de puertos](https://es.wikipedia.org/wiki/Esc%C3%A1ner_de_puertos) o escaneo de puertos se emplea para designar la acción de analizar por medio de un programa el estado de los puertos de una máquina conectada a una red de comunicaciones. Detecta si un puerto está abierto, cerrado, o protegido por un cortafuegos. Los administradores de seguridad de red utilizan principalmente escáneres de puertos para escanear y monitorear puertos de red en un sistema, servidor o entorno de TI.


### ¿Cómo funciona portscanner?

El escáner utiliza sockets para validar los puertos abiertos de una dirección IPv4.

```markdown
Sintax para utilizar el script.

python3 portscanner.py <IP>
```

![PortScanner](/pythonscanner.png)
