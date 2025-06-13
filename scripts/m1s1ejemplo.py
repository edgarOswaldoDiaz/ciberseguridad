import json


def analizar_problema_seguridad(jefe_inmediato, datos_logs, entrevistas, reportes_monitoreo, modo_colaborativo=False):
    """
    Analiza un problema de seguridad informática siguiendo estos pasos:
      1. Recepción de instrucciones y definición de objetivos
      2. Recolección y preprocesamiento de información
      3. Evaluación de vulnerabilidades y cálculo de matriz de riesgos
      4. Colaboración y validación de hallazgos
      5. Generación y entrega de informe final
    Parámetros:
      jefe_inmediato: objeto con método get_instrucciones()
      datos_logs: ruta o estructura de logs de sistemas
      entrevistas: lista de participantes para entrevistas
      reportes_monitoreo: origen de datos de monitoreo automático
      modo_colaborativo: booleano para compartir resultados intermedios
    Retorna:
      informe final como diccionario
    """
    # 1. Recepción de instrucciones y definición de objetivos
    instrucciones = jefe_inmediato.get_instrucciones()
    proyecto = instrucciones.get('proyecto')
    alcance = instrucciones.get('alcance')
    objetivos = {
        'proyecto': proyecto,
        'alcance': alcance
    }

    # 2. Recolección y preprocesamiento
    datos = obtener_logs(datos_logs)
    entrevistas_data = realizar_entrevistas(entrevistas)
    reportes = descargar_reportes(reportes_monitoreo)

    activos = identificar_activos(datos, entrevistas_data)
    datos_limpios = filtrar_ruido(datos)

    # 3. Evaluación de vulnerabilidades y cálculo de matriz_ riesgos
    matriz_riesgos = {}
    for activo in activos:
        amenazas = evaluar_amenazas(activo)
        vulnerabilidades = escanear_vulnerabilidades(activo)
        riesgo = calcular_riesgo(amenazas, vulnerabilidades)
        matriz_riesgos[activo] = riesgo

    # 4. Colaboración y validación
    if modo_colaborativo:
        compartir_resultados(equipo=get_equipo(), resultados=matriz_riesgos)
        realizar_reunion(equipo=get_equipo())

    # 5. Generación y entrega de informe
    informe = generar_informe(matriz_riesgos, hallazgos=amenazas, recomendaciones=vulnerabilidades)
    feedback = jefe_inmediato.revisar(informe)
    informe_final = ajustar_informe(informe, feedback)
    jefe_inmediato.entregar(informe_final)
    return informe_final


def analizar_con_dfd(sistema_objetivo, modo_colaborativo=False):
    """
    Utiliza Diagramas de Flujo de Datos (DFD) y estructuras de control para analizar riesgos:
      1. Construcción de DFD Contexto y Nivel 1
      2. Validación de confidencialidad, integridad y disponibilidad
      3. Detección de fallas en controles de acceso
      4. Generación de DFD de riesgos y plan de mitigación
      5. Entrega de resultados
    Parámetros:
      sistema_objetivo: descriptor o identificador del sistema a modelar
      modo_colaborativo: booleano para revisar con equipo
    Retorna:
      estructura con DFD de riesgos y plan de mitigación
    """
    # 1. Construir DFD
    contexto = crear_dfd_contexto(sistema_objetivo)
    nivel1 = descomponer_dfd(contexto)

    riesgos_detectados = []

    # 2. Recorrer flujos de Nivel1 con estructuras de control
    for flujo in nivel1['flujos']:
        # Confidencialidad
        if flujo.get('es_confidencial') and not validar_cifrado(flujo):
            riesgos_detectados.append((flujo['id'], 'Sin cifrado'))
        # Integridad
        if flujo.get('requiere_integridad'):
            muestra = capturar_muestra(flujo)
            if not comprobar_hash(muestra):
                riesgos_detectados.append((flujo['id'], 'Hash inválido'))
        # Disponibilidad
        latencia = medir_latencia(flujo)
        if latencia > flujo.get('umbral_entrega'):
            riesgos_detectados.append((flujo['id'], 'Alta latencia'))

    # 3. Validar controles de acceso
    for proceso in nivel1['procesos']:
        controles = obtener_controles_acceso(proceso)
        if not controles:
            riesgos_detectados.append((proceso['id'], 'Sin control de acceso'))

    # 4. Generar DFD de riesgos y plan de mitigación
    dfd_riesgos = crear_dfd_con_riesgos(nivel1, riesgos_detectados)
    plan_mitigacion = {}
    for elemento, motivo in riesgos_detectados:
        plan_mitigacion[elemento] = proponer_mitigacion(motivo)

    # 5. Revisión colaborativa y entrega
    if modo_colaborativo:
        revisar_con_equipo(dfd_riesgos)
        incorporar_sugerencias(dfd_riesgos)

    return {
        'dfd_riesgos': dfd_riesgos,
        'plan_mitigacion': plan_mitigacion
    }
