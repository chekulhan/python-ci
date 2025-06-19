
from empresa import ComprobarNombredeEmpresa

def test_empresa():
    assert ComprobarNombredeEmpresa("Nt") == True
    assert ComprobarNombredeEmpresa("Google") == True