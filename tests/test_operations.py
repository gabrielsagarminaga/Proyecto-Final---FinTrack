import unittest
import tempfile
import os
from unittest.mock import patch

from src.storage import guardar_datos
from src.operations import calcular_balance, filtrar_por_categoria, resumen_financiero


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.temp_file.close()

        self.data = [
            {
                "tipo": "ingreso",
                "monto": 5000,
                "categoria": "salario",
                "descripcion": "sueldo mensual",
                "fecha": "2026-05-09"
            },
            {
                "tipo": "gasto",
                "monto": 150,
                "categoria": "comida",
                "descripcion": "pizza",
                "fecha": "2026-05-09"
            },
            {
                "tipo": "gasto",
                "monto": 300,
                "categoria": "transporte",
                "descripcion": "gasolina",
                "fecha": "2026-05-09"
            }
        ]

        with patch("src.storage.FILE_PATH", self.temp_file.name):
            guardar_datos(self.data)

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_calcular_balance(self):
        with patch("src.storage.FILE_PATH", self.temp_file.name):
            self.assertEqual(calcular_balance(), 4550)

    def test_filtrar_por_categoria(self):
        with patch("src.storage.FILE_PATH", self.temp_file.name):
            resultados = filtrar_por_categoria("comida")
            self.assertEqual(len(resultados), 1)
            self.assertEqual(resultados[0]["descripcion"], "pizza")

    def test_resumen_financiero(self):
        with patch("src.storage.FILE_PATH", self.temp_file.name):
            resumen = resumen_financiero()
            self.assertEqual(resumen["ingresos"], 5000)
            self.assertEqual(resumen["gastos"], 450)
            self.assertEqual(resumen["balance"], 4550)


if __name__ == "__main__":
    unittest.main()