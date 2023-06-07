# API Blog Platzi

API Rest para obtener información de artículos publicados en el blog de [Platzi](https://platzi.com/blog).

> NOTA: En desarrollo...

### Endpoints

| Endpoint        | HTTP | Description                              | Query Params       |
| --------------- | ---- | ---------------------------------------- | ------------------ |
| 🔒 `/api`       | GET  | Obtener estatus de la api                |                    |
| 🔒 `/api/posts` | GET  | Obtener publicaciones del blog de platzi | ?filter=new&page=1 |
| `/docs`         | GET  | Documentación de OpenAPI                 |                    |

### Ejemplo

Respuesta para la petición: `GET: {HOST}/api/posts?filter=new&page=1`

```json
{
  "error": [],
  "response": [
    {
      "link": "https://platzi.com/blog/lanzate-al-espacio-platzi-space-program/",
      "title": "Lo que necesitas para ser parte del Platzi Space Program",
      "preview": "Seguramente escuchaste que Platzi lanzará un satélite al espacio. Quizás lo que no sabes es que puedes ser parte de esta misión con toda la comunidad durante...",
      "author": "tifis",
      "author_picture": "https://static.platzi.com/media/avatars/avatars/tifis_d17a3072-f911-4a99-b523-bd4fe83265ad.jpeg",
      "likes": 28,
      "comments": 8,
      "relative_time": "hace 22 horas"
    },
    { ... }
  ],
  "status_code": 200
}
```

### Comandos

```sh
# Preparar el entorno virtual para python
pipenv shell

# Instalar todas las dependencias descritas en Pipfile
pipenv install

# Ejecutar la API
pipenv run start
```

### Stack

- Python 3.8
- FastAPI

### License

[MIT](./LICENSE) &copy; Edixon Piña
