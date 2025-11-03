import pdb


class MedioPago:
    def __init__(self):
        pass

    def pagar(self, monto: float) -> str:
        raise NotImplementedError("Subclases deben implementar pagar()")
  


class Tarjeta(MedioPago):
    def __init__(self, numero: str, cvv: int):
        # super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, monto: float) -> str:
        return f"""
        Pagando {monto} con tarjeta {self.numero[-4:]}
        Transacción aprobada.
        """


class Efectivo(MedioPago):
    def __init__(self, monto_entregado: float):
        # super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto: float) -> str:
        if self.monto_entregado >= monto:
            # genera cambio/vueltas
            return f"""
            Pago realizado en efectivo. 
            Cambio: {self.monto_entregado - monto}
            """
        else:
            return f"""
            Fondos insuficientes. 
            Faltan {monto - self.monto_entregado} para completar el pago.
            """


# Ejemplo de uso
pago_tarjeta = Tarjeta(numero="1234567890123456", cvv=123)
pago_efectivo = Efectivo(monto_entregado=100)

pdb.set_trace()

print(pago_tarjeta.pagar(50))
print(pago_efectivo.pagar(105))
