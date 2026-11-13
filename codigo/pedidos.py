def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_envio(subtotal):
    if subtotal >= 300:
        return 0
    else:
        return 20

# Casos de prueba requeridos
casos = [(80, 3), (100, 3), (150, 3)]
for precio, cantidad in casos:
    subtotal = calcular_subtotal(precio, cantidad)
    envio = calcular_envio(subtotal)
    total = subtotal + envio
    print(f"Precio: S/ {precio} | Cantidad: {cantidad} | Subtotal: S/ {subtotal} | Envio: S/ {envio} | Total: S/ {total}")
