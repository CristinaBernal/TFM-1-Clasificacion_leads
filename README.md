# Clasificación de leads con mayor probabilidad de compra

## 0. Introducción

TelcoNet opera en un mercado de telecomunicaciones altamente competitivo, donde la captación de nuevos clientes supone un coste cada vez mayor. En este contexto, el crecimiento mediante la venta de servicios adicionales a la base de clientes existente se ha convertido en un pilar estratégico para el aumento de ingresos.

Dentro del portfolio de servicios, los paquetes de *streaming* de películas han sido seleccionados como foco de este proyecto debido a su elevada demanda, atractivo margen de beneficio y su capacidad para mejorar la retención de clientes. No obstante, las campañas actuales se realizan de forma genérica, enviando ofertas de manera indiscriminada sin considerar el interés real de cada cliente. Esta aproximación deriva en bajas tasas de conversión, un uso ineficiente del presupuesto de marketing y una experiencia de cliente subóptima.

Con el objetivo de mejorar la eficiencia de las campañas y maximizar el retorno económico, TelcoNet busca identificar de forma precisa qué clientes tienen una mayor probabilidad de contratar este servicio, permitiendo diseñar acciones de marketing más focalizadas, relevantes y rentables.


## 1. Objetivos de negocio

El objetivo principal de este proyecto es identificar y priorizar los leads con mayor probabilidad de contratar un servicio de *streaming* de películas, con el fin de optimizar la asignación de recursos de marketing y maximizar los ingresos.

### Objetivos específicos

**Predicción de la probabilidad de conversión**
- Estimar la probabilidad individual de compra de cada lead.
- Generar un *propensity score* entre 0 y 1 para cada cliente.
- Clasificar los leads en segmentos estratégicos: alta, media y baja probabilidad de compra.

**Cuantificación del impacto económico**
- Estimar los ingresos potenciales derivados de los leads con alta propensión.
- Calcular el impacto económico como:  
  *número de clientes × probabilidad de conversión × precio del servicio*.
- Facilitar la priorización de la inversión de marketing hacia los clientes más rentables.

**Identificación de los factores que impulsan la compra**
- Determinar qué variables influyen más en la propensión a contratar el servicio (historial de consumo, perfil sociodemográfico, tipo de contrato, uso de otros servicios, antigüedad, entre otras).
- Proporcionar *insights* accionables para diseñar campañas más efectivas y personalizadas.

**Definición del perfil del “lead ideal”**
- Describir las características comunes de los leads con alta probabilidad de compra.
- Facilitar la segmentación de clientes y la personalización de ofertas según su probabilidad de conversión y valor económico.


## 2. Preguntas clave

Para lograr estos objetivos, TelcoNet busca desarrollar un modelo de clasificación que permita identificar los clientes con mayor probabilidad de contratar un servicio de *streaming* de películas. Si el modelo funciona correctamente, las campañas de marketing serán más eficientes, se optimizará el uso de los recursos disponibles y se mejorará la experiencia del cliente al recibir ofertas más relevantes y personalizadas. Además, permitirá estimar de forma cuantitativa el impacto económico de centrar los esfuerzos en los leads con mayor propensión.

A partir de esta premisa, el modelo deberá dar respuesta a las siguientes cuestiones:

### ¿Qué clientes tienen mayor probabilidad de contratar el servicio?
- Generar un *propensity score* entre 0 y 1 para cada lead.
- Clasificar a los clientes en segmentos de alta, media y baja probabilidad de compra.

### ¿Qué ingresos potenciales se pueden generar al enfocarse en los leads de alta propensión?
- Traducir los *scores* de propensión en ingresos estimados.
- Calcular el impacto económico mediante la fórmula:  
  *número de clientes × probabilidad de conversión × precio del servicio*.

### ¿Qué características del cliente influyen más en la compra?
- Identificar las variables más relevantes mediante técnicas de interpretabilidad (por ejemplo, SHAP).
- Analizar el impacto de factores como tipo de contrato, uso de otros servicios, cargos mensuales, antigüedad, entre otros.

### ¿Existe un perfil de “lead ideal”?
- Describir las características comunes de los clientes con alta propensión.
- Utilizar este perfil como guía para el diseño de futuras campañas de marketing.

## 3. Preparación de los datos
Los datos utilizados en este proyecto provienen del dataset
**Telco Customer Churn**, disponible en Hugging Face:

- Fuente: Hugging Face Datasets
- URL: https://huggingface.co/datasets/aai510-group1/telco-customer-churn
- Splits utilizados: train, validation, test

Los datos se descargan automáticamente al ejecutar los notebooks
o el pipeline mediante la librería `pandas`.