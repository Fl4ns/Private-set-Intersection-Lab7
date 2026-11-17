# Private-set-Intersection-Lab7

En este repositorio se encuentra el desarrollo asociado al laboratorio Nro 7 de la asignatura de Criptografía y Seguridad de la información (TEL252)


### Integrantes del equipo

| Nombre              | Rol         |
| ------------------- | ----------- |
| Constanza Acosta    | 202330019-5 |
| Ignacia Marquez     | 202030015-1 |
| Hanz Varela         | 202230014-0 |

### Contexto:
Cada año se filtran miles de millones de contraseñas, y tu navegador puede avisarte si una contraseña tuya está entre ellas. Pero no puedes enviar tu contraseña (ni su hash) a un servidor ajeno, y el servidor no puede enviarte la base de datos completa de filtraciones. Diferentes navegadores resuelven este problema con una idea que ya conocen, propuesta por Catherine Meadows (1986). Si cada parte eleva un valor a su propio secreto, el orden de los exponentes no importa, igual que en DH.

### Objetivo:
**Aplicación:** verificación de contraseñas filtradas. El **navegador** debe saber si una credencial está filtrada sin revelarla, contra un **servidor** con miles de millones de credenciales y sin descargar la base completa.

**Alcance mínimo de la API:** un **servidor** con una base de al menos mil credenciales ficticias, y un **navegador** que consulta una credencial y sabe si está en la base sin revelarla.

### Links de apoyo:
https://openmined.org/blog/private-set-intersection-with-diffie-hellman/  
https://crypto.stackexchange.com/questions/95291/the-diffie-hellman-based-private-set-intersection-protocol-cannot-pass-simulatio
