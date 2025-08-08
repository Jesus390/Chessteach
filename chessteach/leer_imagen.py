import cv2 as cv

class Imagen():
    def __init__(self, ruta):
        self.ruta = ruta
        
    def leer(self):
        return cv.imread(self.ruta)
    
    def mostrar(self):
        imagen = self.leer()
        cv.imshow("", imagen)
        cv.waitKey(0)

if __name__ == "__main__":
    ruta = "recursos/imagenes/test/bg-blanco.png"
    imagen = Imagen(ruta)
    imagen.mostrar()