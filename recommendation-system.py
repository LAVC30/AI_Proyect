"""Sistema de recomendacion sencillo basado en preferencias por categoria."""


PRODUCTOS = [
    {"nombre": "Auriculares inalambricos", "categorias": ["tecnologia", "audio"]},
    {"nombre": "Altavoz Bluetooth", "categorias": ["tecnologia", "audio"]},
    {"nombre": "Novela de misterio", "categorias": ["libros", "ficcion"]},
    {"nombre": "Libro de cocina", "categorias": ["libros", "cocina"]},
    {"nombre": "Esterilla de yoga", "categorias": ["deporte", "bienestar"]},
    {"nombre": "Botella reutilizable", "categorias": ["deporte", "bienestar"]},
    {"nombre": "Cafetera", "categorias": ["cocina", "hogar"]},
]


def recomendar_productos(preferencias, productos):
    """Devuelve productos cuyas categorias coinciden con las preferencias."""
    preferencias = {preferencia.strip().lower() for preferencia in preferencias}
    recomendaciones = []

    for producto in productos:
        coincidencias = preferencias.intersection(producto["categorias"])
        if coincidencias:
            recomendaciones.append((len(coincidencias), producto["nombre"]))

    recomendaciones.sort(key=lambda recomendacion: (-recomendacion[0], recomendacion[1]))
    return recomendaciones


def main():
    print("Categorias disponibles: tecnologia, audio, libros, ficcion,")
    print("cocina, deporte, bienestar y hogar.")
    entrada = input("Escribe tus preferencias separadas por comas: ")
    preferencias = entrada.split(",")

    recomendaciones = recomendar_productos(preferencias, PRODUCTOS)

    if not recomendaciones:
        print("No se encontraron productos para esas preferencias.")
        return

    print("\nProductos recomendados:")
    for puntuacion, nombre in recomendaciones:
        print(f"- {nombre} (coincidencias: {puntuacion})")


if __name__ == "__main__":
    main()