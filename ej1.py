class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []
        print(f"Inventario para la tienda '{self.nombre_tienda}' creado.")

    def _buscar_producto(self, nombre):
        for producto in self.productos:
            if producto['nombre'].lower() == nombre.lower():
                return producto
        return None

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
            return

        producto_existente = self._buscar_producto(nombre)
        if producto_existente:
            producto_existente['cantidad'] += cantidad
            print(f"Se actualizó la cantidad de '{nombre}'. Nueva cantidad: {producto_existente['cantidad']}.")
        else:
            self.productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
            print(f"Producto '{nombre}' agregado exitosamente.")

    def vender_producto(self, nombre, cantidad):
        producto = self._buscar_producto(nombre)
        if producto is None:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
            return

        if cantidad <= 0:
            print("Error: La cantidad a vender debe ser un valor positivo.")
            return

        if producto['cantidad'] < cantidad:
            print(f"Error: No hay suficiente stock. Cantidad actual de '{nombre}': {producto['cantidad']}.")
        else:
            producto['cantidad'] -= cantidad
            print(f"Venta realizada. Se vendieron {cantidad} unidades de '{nombre}'. Stock restante: {producto['cantidad']}.")

    def mostrar_inventario(self):
        print(f"\n--- Inventario de '{self.nombre_tienda}' ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
        print("-----------------------------------------")

    def producto_mas_caro(self):
        if not self.productos:
            return None, None
        
        mas_caro = max(self.productos, key=lambda p: p['precio'])
        return mas_caro['nombre'], mas_caro['precio']

if __name__ == "__main__":
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    mi_tienda = InventarioTienda(nombre_tienda)

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto mas caro")
        print("5. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                mi_tienda.agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Error: El precio y la cantidad deben ser numeros.")
        
        elif opcion == '2':
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
                mi_tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un numero entero.")

        elif opcion == '3':
            mi_tienda.mostrar_inventario()

        elif opcion == '4':
            nombre, precio = mi_tienda.producto_mas_caro()
            if nombre:
                print(f"El producto mas caro es '{nombre}' con un precio de ${precio:.2f}.")
            else:
                print("El inventario esta vacio, no hay productos para consultar.")

        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")