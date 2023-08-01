class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro
    
    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break

        self.actualizar_carro()

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.actualizar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"] == 0:
                    self.eliminar(producto) 
                break
        self.actualizar_carro()

    def limpiar_carro(self):
        self.carro = {}
        self.actualizar_carro()

    def actualizar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True