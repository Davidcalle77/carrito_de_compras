# clase CarritoCompras (sin datos)
class CarritoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}

    def agregar(self, producto, precio):
        self.productos[producto] = precio

    def total(self):
        return sum(self.productos.values())

    def __str__(self):
        lineas = [f" Carrito de: {self.cliente}"]
        lineas.append("_" * 30)
        for producto, precio in self.productos.items():
            lineas.append(f" .{producto}: ${precio:.2f}")
        lineas.append("_" * 30)
        lineas.append(f" Total: ${self.total():.2f}")
        return "\n".join(lineas)

    def __len__(self):
        return len(self.productos)
