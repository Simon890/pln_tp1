def env(key : str) -> str:
    with open(".env", "r") as archivo:
        linea = archivo.readline()
        while linea:            
            if linea.startswith(key):
                val = linea.strip().split("=")[1]
                if len(val) > 0: return val.strip()
                return None
            linea = archivo.readline()
    return None