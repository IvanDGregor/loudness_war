# Loudness War
![titulo](/images/imagen_loudness.gif)

> La expresión guerra del volumen (del inglés loudness war) se refiere a la tendencia de la industria musical a grabar, producir y emitir música elevando progresivamente el volumen todos los años creando un sonido que destaca sobre los de años anteriores.

Con esta premisa hemos analizado a traves de un DataSet con los Year-End Hot 100 de la revista 'Billboard' desde el año 1964 hasta 2015, para mas informacion sobre el DataSet en este link: https://www.kaggle.com/rakannimer/billboard-lyrics. Ademas hemos añadido información sobre datos tecnicos que nuestro DataSet no tenia. Para ello hemos utilizado la API de Spotify con la que hemos buscado por nombre de la cancion y el artista y hemos generado un nuevo DataFrame con los datos originales y los datos tecnicos proporcionados por Spotify.

Con este DataFrame se ha analizado la progesion del volumen y otros parametros a lo largo de los años.

Para ejecutar el programa es necesario pasar dos parametros por consola indicandole el año inicial y el año final de nuestro analisis.
