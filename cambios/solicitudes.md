# Registro de Solicitudes y Cambios - GAVE ARIAS

## INC-014: Error en cálculo de subtotal
- **Descripción:** El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada.
- **Tipo de cambio:** Corrección de defecto (Bugfix)
- **Justificación:** Es un error lógico que afecta la precisión financiera de los pedidos.
- **Requisito afectado:** RN-01
- **Archivos afectados:** codigo/pedidos.py
- **Riesgo:** Bajo
- **Criterio de aceptación:** Para S/ 80 y 3 unidades, el subtotal debe ser exactamente S/ 240.
- **Decisión de aprobación simulada:** Aprobado por el área de desarrollo.

## CR-015: Incorporación de cálculo de costo de envío y total
- **Descripción:** La gerencia comercial solicita incorporar el cálculo automático del costo de envío y del total del pedido.
- **Tipo de cambio:** Nueva funcionalidad (Feature)
- **Justificación:** Automatizar tarifas de envío según reglas comerciales RN-02 y RN-03.
- **Requisitos afectados:** RN-02, RN-03, RN-04
- **Archivos afectados:** codigo/pedidos.py, documentos/requisitos.md
- **Riesgo:** Medio
- **Criterio de aceptación:** Cumplir con las tarifas gratuitas o fijas y sumar correctamente el total.
- **Decisión de aprobación simulada:** Aprobado por la gerencia comercial.
