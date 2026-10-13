import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

class PDFReportGenerator:
    def __init__(self, filename="informe_suelo_eeaoc.pdf"):
        self.filename = filename

    def generar_informe(self, datos_muestra: dict, resultados: list, output_path: str = None):
        """
        Genera el informe PDF de aptitud de suelos para la EEAOC.
        
        datos_muestra: dict con {'muestra': '...', 'cultivo': '...', 'fecha': '...'}
        resultados: lista de dicts con:
            [
                {
                    'variable': 'Materia Orgánica',
                    'valor': 1.5,
                    'unidad': '%',
                    'clasificacion': 'Bajo',
                    'recomendacion': '...'
                },
                ...
            ]
        """
        path = output_path if output_path else self.filename
        
        # ---> NUEVO: Asegurarnos de que la carpeta de destino exista antes de crear el PDF <---
        directorio = os.path.dirname(path)
        if directorio:
            os.makedirs(directorio, exist_ok=True)
            
        doc = SimpleDocTemplate(path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        story = []
        
        styles = getSampleStyleSheet()
        
        # Estilos personalizados
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#1b4332'),
            alignment=1, # Centrado
            spaceAfter=6
        )
        
        subtitle_style = ParagraphStyle(
            'SubtitleStyle',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#555555'),
            alignment=1,
            spaceAfter=15
        )
        
        section_style = ParagraphStyle(
            'SectionStyle',
            parent=styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#2d6a4f'),
            spaceBefore=10,
            spaceAfter=6
        )
        
        normal_style = ParagraphStyle(
            'NormalStyle',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#333333')
        )
        
        header_table_style = ParagraphStyle(
            'HeaderTableStyle',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.white,
            fontName="Helvetica-Bold"
        )

        # Encabezado institucional
        story.append(Paragraph("ESTACIÓN EXPERIMENTAL AGROINDUSTRIAL OBISPO COLOMBRES", title_style))
        story.append(Paragraph("Sección Suelos y Nutrición Vegetal — Sistema de Análisis de Aptitud de Suelos", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2d6a4f'), spaceAfter=15))
        
        # Datos de identificación de la muestra
        story.append(Paragraph("<b>Identificación de la Muestra</b>", section_style))
        
        info_data = [
            [Paragraph(f"<b>Muestra:</b> {datos_muestra.get('muestra', 'N/D')}", normal_style),
             Paragraph(f"<b>Cultivo Seleccionado:</b> {datos_muestra.get('cultivo', 'N/D')}", normal_style)],
            [Paragraph(f"<b>Fecha de Emisión:</b> {datos_muestra.get('fecha', 'N/D')}", normal_style),
             Paragraph("<b>Laboratorio:</b> EEAOC", normal_style)]
        ]
        
        info_table = Table(info_data, colWidths=[270, 270])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8f9fa')),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        
        story.append(info_table)
        story.append(Spacer(1, 15))
        
        # Resultados y Evaluación
        story.append(Paragraph("<b>Resultados y Evaluación de Variables Prioritarias</b>", section_style))
        
        table_data = [[
            Paragraph("Variable", header_table_style),
            Paragraph("Valor", header_table_style),
            Paragraph("Unidad", header_table_style),
            Paragraph("Clasificación", header_table_style),
            Paragraph("Recomendación Agronómica", header_table_style)
        ]]
        
        for item in resultados:
            clasif = item.get('clasificacion', 'Normal')
            table_data.append([
                Paragraph(item.get('variable', ''), normal_style),
                Paragraph(str(item.get('valor', '')), normal_style),
                Paragraph(item.get('unidad', ''), normal_style),
                Paragraph(f"<b>{clasif}</b>", normal_style),
                Paragraph(item.get('recomendacion', ''), normal_style)
            ])
            
        results_table = Table(table_data, colWidths=[100, 55, 55, 90, 220])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2d6a4f')),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        
        story.append(results_table)
        story.append(Spacer(1, 20))
        
        # Pie de página / Observaciones
        story.append(Paragraph("<b>Observaciones Técnicas:</b>", section_style))
        obs_text = "Los rangos de clasificación y criterios agronómicos aplicados se basan en las normativas y validaciones de la Estación Experimental Agroindustrial Obispo Colombres (EEAOC) para el cultivo especificado."
        story.append(Paragraph(obs_text, normal_style))
        
        doc.build(story)
        return path