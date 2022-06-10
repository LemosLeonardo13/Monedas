
from  cv2 import cv2

import numpy as np #numpy me da funciones para matrices


valorGausse=3
ValorKernel=3

Original=cv2.imread("foto\monedas.jpg")
Grises=cv2.cvtColor(Original,cv2.COLOR_RGB2BGR)
Gauss=cv2.GaussianBlur(Grises, (valorGausse,valorGausse),0)

Canny =cv2.Canny(Original,100,200)

#Kernel=np.ones((ValorKernel,ValorKernel),np.uint8)

#cierre=cv2.morphologyEx(Gauss,cv2.MORPH_CLOSE, Kernel)

#contorons,_=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#print("MONEDAS ENCOTRADAS{}".format(len(contorons)))
#cv2.drawContours(Original, contorons, -1, (0,0,255),2)

#MOSTRAR RESULTADOS

cv2.imshow("Grises", Grises)
cv2.imshow("Gauss", Gauss)
#cv2.imshow("Canny", Canny)
#cv2.imshow("CONTORNOS", contorons)
#cv2.imshow("Resultado", Original)

cv2.waitKey(0)