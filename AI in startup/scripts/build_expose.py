#!/usr/bin/env python
"""Build the complete Expose document with all formal framework elements."""
import os, re, shutil
from xml.sax.saxutils import escape as xml_escape

WORK_DIR = os.path.join(os.environ.get('TEMP', '/tmp'), 'expose_work')
PROMPT_DIR = os.path.join(os.environ.get('TEMP', '/tmp'), 'prompt_texts')
DOC_XML = os.path.join(WORK_DIR, 'word', 'document.xml')
LOGO_SRC = os.path.join(os.environ.get('TEMP', '/tmp'), 'hfwu_logo.png')
LOGO_DST = os.path.join(WORK_DIR, 'word', 'media', 'image2.png')

def esc(text): return xml_escape(text)
def page_break(): return '    <w:p><w:r><w:br w:type="page"/></w:r></w:p>\n'

def empty_para(center=False, size=24, spacing_after=0):
    jc = '<w:jc w:val="center"/>' if center else ''
    return ('    <w:p><w:pPr><w:spacing w:after="'+str(spacing_after)+'" w:line="360" w:lineRule="auto"/>'+jc
            +'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
            +'<w:sz w:val="'+str(size)+'"/><w:szCs w:val="'+str(size)+'"/></w:rPr></w:pPr></w:p>\n')

def heading1_no_num(text):
    e = esc(text)
    return ('    <w:p><w:pPr><w:pStyle w:val="berschrift1"/>'
            '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="0"/></w:numPr>'
            '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/></w:rPr>'
            '</w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
            '</w:rPr><w:t>'+e+'</w:t></w:r></w:p>\n')

def normal_para(text, bold=False, italic=False, center=False, size=24,
                font="Times New Roman", spacing_after=120, hanging_indent=False):
    e = esc(text)
    jc_val = "center" if center else "both"
    rpr = ('<w:rFonts w:ascii="'+font+'" w:hAnsi="'+font+'" w:cs="'+font+'"/>'
           '<w:sz w:val="'+str(size)+'"/><w:szCs w:val="'+str(size)+'"/>')
    if bold: rpr += '<w:b/>'
    if italic: rpr += '<w:i/>'
    sa = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') or '  ' in text else ''
    ind = '<w:ind w:left="709" w:hanging="709"/>' if hanging_indent else ''
    return ('    <w:p><w:pPr><w:spacing w:after="'+str(spacing_after)+'" w:line="360" w:lineRule="auto"/>'
            +ind+'<w:jc w:val="'+jc_val+'"/><w:rPr>'+rpr+'</w:rPr></w:pPr>'
            '<w:r><w:rPr>'+rpr+'</w:rPr><w:t'+sa+'>'+e+'</w:t></w:r></w:p>\n')

def prompt_para(text, size=20, font="Times New Roman"):
    e = esc(text)
    rpr = ('<w:rFonts w:ascii="'+font+'" w:hAnsi="'+font+'" w:cs="'+font+'"/>'
           '<w:sz w:val="'+str(size)+'"/><w:szCs w:val="'+str(size)+'"/>')
    return ('    <w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/>'
            '<w:rPr>'+rpr+'</w:rPr></w:pPr>'
            '<w:r><w:rPr>'+rpr+'</w:rPr><w:t xml:space="preserve">'+e+'</w:t></w:r></w:p>\n')

def table_cell(text, bold=False, size=20, shading=None, width=None):
    e = esc(text)
    rpr = ('<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
           '<w:sz w:val="'+str(size)+'"/><w:szCs w:val="'+str(size)+'"/>')
    if bold: rpr += '<w:b/>'
    shd = '<w:shd w:val="clear" w:color="auto" w:fill="'+shading+'"/>' if shading else ''
    w = '<w:tcW w:w="'+str(width)+'" w:type="dxa"/>' if width else ''
    sa = ' xml:space="preserve"' if text.startswith(' ') or text.endswith(' ') else ''
    return ('<w:tc><w:tcPr>'+w+shd+'</w:tcPr>'
            '<w:p><w:pPr><w:spacing w:after="40" w:line="240" w:lineRule="auto"/>'
            '<w:rPr>'+rpr+'</w:rPr></w:pPr>'
            '<w:r><w:rPr>'+rpr+'</w:rPr><w:t'+sa+'>'+e+'</w:t></w:r></w:p></w:tc>\n')

def gen_deckblatt():
    xml = ('    <w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
           '<w:r><w:rPr><w:noProof/></w:rPr><w:drawing>'
           '<wp:inline distT="0" distB="0" distL="0" distR="0" '
           'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">'
           '<wp:extent cx="2268000" cy="1134000"/>'
           '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
           '<wp:docPr id="2" name="HFWU Logo"/>'
           '<wp:cNvGraphicFramePr>'
           '<a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>'
           '</wp:cNvGraphicFramePr>'
           '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
           '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
           '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
           '<pic:nvPicPr><pic:cNvPr id="0" name="image2.png"/><pic:cNvPicPr/></pic:nvPicPr>'
           '<pic:blipFill><a:blip r:embed="rId9"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
           '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="2268000" cy="1134000"/></a:xfrm>'
           '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
           '</pic:pic></a:graphicData></a:graphic>'
           '</wp:inline></w:drawing></w:r></w:p>\n')
    for _ in range(4): xml += empty_para(center=True)
    xml += normal_para("Handel, Vertrieb und E-Commerce", bold=True, center=True, size=28, spacing_after=0)
    xml += empty_para(center=True)
    xml += normal_para("Schriftliche Arbeit", center=True, size=24, spacing_after=0)
    xml += normal_para("im Modul", center=True, size=24, spacing_after=0)
    xml += normal_para("Methodische Grundlagen 3", bold=True, center=True, size=28, spacing_after=0)
    xml += empty_para(center=True)
    xml += normal_para("Sommersemester 2026", center=True, size=24, spacing_after=0)
    for _ in range(4): xml += empty_para(center=True)
    xml += normal_para("vorgelegt von", center=True, size=24, spacing_after=0)
    xml += normal_para("Mattis Engelhardt (Matr. Nr. 4110790)", center=True, size=24, spacing_after=0)
    xml += empty_para(center=True)
    xml += normal_para("vorgelegt bei", center=True, size=24, spacing_after=0)
    xml += normal_para("Herrn Prof. Dr. Dirk Funck", center=True, size=24, spacing_after=0)
    xml += empty_para(center=True)
    xml += normal_para("HfWU Nürtingen-Geislingen", center=True, size=24, spacing_after=0)
    for _ in range(3): xml += empty_para(center=True)
    xml += normal_para("Abgabedatum: 18.05.2026", center=True, size=24, spacing_after=0)
    xml += page_break()
    return xml

def gen_forschungsfrage():
    xml = ''
    for _ in range(12): xml += empty_para(center=True)
    xml += normal_para("Übergeordnete Forschungsfrage", bold=True, center=True, size=28, spacing_after=0)
    xml += empty_para(center=True)
    xml += normal_para(
        "Welche Rolle spielt KI in der Gründungsphase von B2C-E-Commerce-Startups "
        "zur Stärkung des Unit-Profitability-First-Gedankens?",
        italic=True, center=True, size=24, spacing_after=0)
    return xml

def gen_section_break_1():
    return ('    <w:p><w:pPr><w:sectPr>'
            '<w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134" '
            'w:header="720" w:footer="720" w:gutter="0"/>'
            '<w:cols w:space="720"/><w:titlePg/>'
            '</w:sectPr></w:pPr></w:p>\n')

def gen_toc():
    xml = heading1_no_num("Inhaltsverzeichnis")
    xml += ('    <w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
            '<w:sz w:val="24"/></w:rPr>'
            '<w:t>Bitte Inhaltsverzeichnis aktualisieren (Rechtsklick &#x2192; Felder aktualisieren)</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>\n')
    xml += page_break()
    return xml

def gen_abkuerzungen():
    xml = heading1_no_num("Abkürzungsverzeichnis")
    abbreviations = [
        ("AI", "Artificial Intelligence"), ("B2C", "Business-to-Consumer"),
        ("CEO", "Chief Executive Officer"), ("DTC", "Direct-to-Consumer"),
        ("ERM", "Emotional-Rational-Motivational Model"), ("IT", "Information Technology"),
        ("KECCT", "Knowledge-Experience-Competence-Characteristics-Team"),
        ("KI", "Künstliche Intelligenz"),
        ("MAXQDA", "Software für qualitative Datenanalyse"),
        ("QDA", "Qualitative Datenanalyse"), ("S.", "Seite"), ("vgl.", "vergleiche"),
        ("z. B.", "zum Beispiel"), ("u. a.", "unter anderem"),
    ]
    xml += ('<w:tbl><w:tblPr><w:tblW w:w="8271" w:type="dxa"/><w:tblBorders>'
            '<w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '<w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '<w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '<w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
            '</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>'
            '<w:tblGrid><w:gridCol w:w="2000"/><w:gridCol w:w="6271"/></w:tblGrid>\n')
    for abbr, meaning in abbreviations:
        xml += '<w:tr>\n' + table_cell(abbr, size=24, width=2000) + table_cell(meaning, size=24, width=6271) + '</w:tr>\n'
    xml += '</w:tbl>\n'
    xml += page_break()
    return xml

def gen_abbildungsverzeichnis():
    xml = heading1_no_num("Abbildungsverzeichnis")
    xml += normal_para("Abb. 1: Literaturlandkarte ..................... S. X", spacing_after=120)
    xml += page_break()
    return xml

def gen_gender_disclaimer():
    return normal_para(
        "Aus Gründen der besseren Lesbarkeit wird in dieser Arbeit die maskuline Sprachform verwendet. "
        "Sämtliche Personenbezeichnungen gelten gleichermaßen für alle Geschlechter.",
        italic=True, spacing_after=120)

def gen_section_break_2():
    return ('    <w:p><w:pPr><w:sectPr>'
            '<w:type w:val="nextPage"/>'
            '<w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134" '
            'w:header="720" w:footer="720" w:gutter="0"/>'
            '<w:pgNumType w:fmt="lowerRoman"/>'
            '<w:cols w:space="720"/>'
            '<w:footerReference w:type="default" r:id="rId10"/>'
            '</w:sectPr></w:pPr></w:p>\n')

def gen_literaturverzeichnis():
    xml = heading1_no_num("Literatur- und Quellenverzeichnis")
    entries = [
        'Aryadita, H., Sukoco, B. M., & Lyver, M. (2023). Founders and the success of start-ups: An integrative review. Cogent Business & Management, 10(3), 2284451. https://doi.org/10.1080/23311975.2023.2284451',
        'Byun, K. J., & Yoo, S. (2025). Does overconfidence of CEOs increase startup performance? The role of marketing capability. European Journal of Marketing, 59(5), 1400–1425. https://doi.org/10.1108/EJM-01-2024-0085',
        'Cutolo, D., & Kenney, M. (2021). Platform-Dependent Entrepreneurs: Power Asymmetries, Risks, and Strategies in the Platform Economy. Academy of Management Perspectives, 35(4), 584–605. https://doi.org/10.5465/amp.2019.0103',
        'Döring, N. (2023). Forschungsmethoden und Evaluation in den Sozial- und Humanwissenschaften. Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-662-64762-2',
        'Guo, H., Guo, A., & Ma, H. (2022). Inside the black box: How business model innovation contributes to digital start-up performance. Journal of Innovation & Knowledge, 7(2), 100188. https://doi.org/10.1016/j.jik.2022.100188',
        'Helfat, C. E. (2022). Strategic organization, dynamic capabilities, and the external environment. Strategic Organization, 20(4), 734–742. https://doi.org/10.1177/14761270221115377',
        'Helfat, C. E., & Peteraf, M. A. (2015). Managerial cognitive capabilities and the microfoundations of dynamic capabilities. Strategic Management Journal, 36(6), 831–850. https://doi.org/10.1002/smj.2247',
        'McKee, S., Sands, S., Pallant, J. I., & Cohen, J. (2023). The evolving direct-to-consumer retail model: A review and research agenda. International Journal of Consumer Studies, 47(6), 2816–2842. https://doi.org/10.1111/ijcs.12972',
        'Tidhar, R., Hallen, B. L., & Eisenhardt, K. M. (2025). Measure Twice, Cut Once: Unit Profitability, Scalability, and the Exceptional Growth of New Firms. Organization Science, 36(1), 88–120. https://doi.org/10.1287/orsc.2021.15970',
        'Weng, Q., Wang, D., De Lurgio Ii, S., & Schuetz, S. (2025). How do small-to-medium-sized e-commerce businesses stay competitive? Evidence on the critical roles of IT capability, innovation and multihoming. Internet Research, 35(1), 126–151. https://doi.org/10.1108/INTR-01-2023-0061',
        'Yang, H., Zhang, Y., Chen, K., & Li, J. (2023). The double-edged sword of delivery guarantee in E-commerce. Decision Support Systems, 175, 114042. https://doi.org/10.1016/j.dss.2023.114042',
    ]
    for entry in entries:
        xml += normal_para(entry, size=24, spacing_after=200, hanging_indent=True)
    xml += page_break()
    return xml

def gen_anhangsverzeichnis():
    xml = heading1_no_num("Anhangsverzeichnis")
    for e in ["Literaturlandkarte",
              "Anhang 0: Anmerkung und Dokumentation zur Arbeit mit KI",
              "Anhang 1: Prompt 1", "Anhang 1.5: Prompt 1.5", "Anhang 2: Prompt 2",
              "Anhang 3: Prompt 3", "Anhang 3.5: Prompt 3.5", "Anhang 4: Prompt 4",
              "Anhang 5: Prompt 5", "Anhang 6: Prompt 6"]:
        xml += normal_para(e, spacing_after=60)
    xml += page_break()
    return xml

def gen_literaturlandkarte_anhang():
    xml = heading1_no_num("Literaturlandkarte")
    xml += ('    <w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:noProof/></w:rPr><w:drawing>'
            '<wp:inline distT="0" distB="0" distL="0" distR="0" '
            'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">'
            '<wp:extent cx="5400000" cy="4057461"/>'
            '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
            '<wp:docPr id="3" name="Literaturlandkarte Anhang"/>'
            '<wp:cNvGraphicFramePr>'
            '<a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/>'
            '</wp:cNvGraphicFramePr>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:nvPicPr><pic:cNvPr id="0" name="Literaturlandkarte.jpg"/><pic:cNvPicPr/></pic:nvPicPr>'
            '<pic:blipFill><a:blip r:embed="rId6"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="5400000" cy="4057461"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic>'
            '</wp:inline></w:drawing></w:r></w:p>\n')
    xml += page_break()
    return xml

def gen_anhang0():
    xml = heading1_no_num("Anhang 0: Anmerkung und Dokumentation zur Arbeit mit KI")
    xml += normal_para("Anmerkung:", bold=True, spacing_after=120)
    xml += normal_para(
        "Alle Kapitel dieser Arbeit wurden mithilfe eines generativen KI-Tools formuliert "
        "(Fall 2: Textgenerierung). Als KI-Tool wurde Claude Code (Claude Opus 4.6, Anthropic) "
        "eingesetzt. Die Literaturrecherche und Quellenauswahl erfolgten durch den Verfasser. "
        "Relevante Textstellen wurden vom Verfasser aus den Quellen entnommen, mit Seitenangaben "
        "dokumentiert und als Inputs in den jeweiligen Prompts verortet. Die KI wurde angewiesen, "
        "diese vorgegebenen Quellenstellen ausschließlich als Evidenzbasis zu verwenden und keine "
        "eigenständige Quellenrecherche oder Quellenentnahme aus dem Internet vorzunehmen. Der "
        "zugrunde gelegte Quellen- und Zitatpool wurde vollständig vom Verfasser definiert. Die "
        "methodische Quelle (Döring, 2023) wurde als Markdown-Datei bereitgestellt und gezielt "
        "per Keyword-Suche durchforstet.", spacing_after=240)
    ki_data = [
        ("Claude Code 01", "Workflow-Planung und Erstellung der Markdown-Arbeitsgrundlage",
         "Der Prompt dient dazu, eine strukturierte Planung für das Exposé-Projekt zu erstellen, einschließlich der Analyse aller Quelldateien und der Erstellung einer konsolidierten Markdown-Datei als Arbeitsgrundlage für alle weiteren Schritte.",
         "Prompt zu lang — siehe Anhang 1"),
        ("Claude Code 01.5", "Vorarbeit Einleitung: Zitat-Recherche",
         "Der Prompt dient dazu, systematisch zitierfähige Stellen aus den 10 inhaltlichen Quellen zu identifizieren und für die Einleitung aufzubereiten, wobei ausschließlich aus dem Kernpart (nicht Abstract/Introduction) zitiert werden darf.",
         "Prompt zu lang — siehe Anhang 1.5"),
        ("Claude Code 02", "Einleitung schreiben",
         "Der Prompt dient dazu, die wissenschaftliche Einleitung (ca. 1 Seite) zu generieren, die vom Makroproblem zur Forschungsfrage führt, alle Stakeholder benennt und einen Ausblick auf die Methodik gibt.",
         "Prompt zu lang — siehe Anhang 2"),
        ("Claude Code 03", "Synthese-Plan für den Literature Review",
         "Der Prompt dient dazu, einen detaillierten Synthese-Plan als Vorarbeit für den Literature Review zu erstellen, in dem die 10 Quellen systematisch verglichen und Forschungslücken identifiziert werden.",
         "Prompt zu lang — siehe Anhang 3"),
        ("Claude Code 03.5", "Literature Review schreiben",
         "Der Prompt dient dazu, den Literature Review (ca. 4 Seiten) als wissenschaftlichen Fließtext zu verfassen, basierend auf dem Synthese-Plan, mit vergleichender Gegenüberstellung der Quellen und Ableitung der Forschungsfrage.",
         "Prompt zu lang — siehe Anhang 3.5"),
        ("Claude Code 04", "Tiefenrecherche Untersuchungsdesign",
         "Der Prompt dient dazu, die Döring-Quelle systematisch zu durchforsten und einen Synthese-Plan mit exakten Zitaten als Grundlage für das Untersuchungsdesign zu erstellen.",
         "Prompt zu lang — siehe Anhang 4"),
        ("Claude Code 05", "Synthese-Blueprint Untersuchungsdesign",
         "Der Prompt dient dazu, aus den Döring-Rechercheergebnissen einen konkreten Blueprint für die Struktur und Argumentation des Untersuchungsdesigns zu entwickeln.",
         "Prompt zu lang — siehe Anhang 5"),
        ("Claude Code 06", "Untersuchungsdesign schreiben",
         "Der Prompt dient dazu, das Untersuchungsdesign (ca. 5 Seiten) als wissenschaftlichen Fließtext zu generieren, mit allen 7 Aspekten und dem Erhebungsinstrument, belegt ausschließlich mit Döring (2023).",
         "Prompt zu lang — siehe Anhang 6"),
    ]
    col_widths = [1200, 1600, 3471, 2000]
    xml += ('<w:tbl><w:tblPr><w:tblW w:w="8271" w:type="dxa"/><w:tblBorders>'
            '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
            '</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>')
    for w in col_widths: xml += '<w:gridCol w:w="'+str(w)+'"/>'
    xml += '</w:tblGrid>\n'
    headers = ["KI", "Einsatzzweck", "Ausführliche Beschreibung", "Prompt"]
    xml += '<w:tr>\n'
    for i, h in enumerate(headers):
        xml += table_cell(h, bold=True, size=20, shading="D9D9D9", width=col_widths[i])
    xml += '</w:tr>\n'
    for ki, zweck, beschr, prompt in ki_data:
        xml += '<w:tr>\n'
        xml += table_cell(ki, size=20, width=col_widths[0])
        xml += table_cell(zweck, size=20, width=col_widths[1])
        xml += table_cell(beschr, size=20, width=col_widths[2])
        xml += table_cell(prompt, size=20, width=col_widths[3])
        xml += '</w:tr>\n'
    xml += '</w:tbl>\n'
    xml += page_break()
    return xml

def gen_anhaenge():
    xml = ''
    prompt_mapping = [
        ("Anhang 1: Prompt 1", "prompt1"), ("Anhang 1.5: Prompt 1.5", "prompt1_5"),
        ("Anhang 2: Prompt 2", "prompt2"), ("Anhang 3: Prompt 3", "prompt3"),
        ("Anhang 3.5: Prompt 3.5", "prompt3_5"), ("Anhang 4: Prompt 4", "prompt4"),
        ("Anhang 5: Prompt 5", "prompt5"), ("Anhang 6: Prompt 6", "prompt6"),
    ]
    
    # Resolve workspace prompts path dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.dirname(script_dir)
    workspace_prompts_dir = os.path.join(workspace_root, "prompts")
    
    prompt_files_mapping = {
        "prompt1": "Prompt 1 Workflow und MD Datei.md",
        "prompt1_5": "Prompt 1.5 Vorarbeit Einleitung.md",
        "prompt2": "Prompt 2 Einleitung schreiben.md",
        "prompt3": "Prompt 3 Synthese Plan.md",
        "prompt3_5": "Prompt 3.5 Literature Review.md",
        "prompt4": "Prompt 4 Untersuchungsdesign Tiefenrecherche.md",
        "prompt5": "Prompt 5.md",
        "prompt6": "Prompt 6.md"
    }
    
    for i, (title, filename) in enumerate(prompt_mapping):
        xml += heading1_no_num(title)
        
        # Try loading from workspace prompts folder first (.md file)
        workspace_file = prompt_files_mapping.get(filename)
        prompt_path = os.path.join(workspace_prompts_dir, workspace_file) if workspace_file else None
        
        if prompt_path and os.path.exists(prompt_path):
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt_text = f.read()
        else:
            # Fallback to local TEMP folder (.txt file)
            prompt_path = os.path.join(PROMPT_DIR, filename + ".txt")
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt_text = f.read()
                
        for line in prompt_text.split('\n'):
            xml += prompt_para(line, size=20, font="Times New Roman")
        if i < len(prompt_mapping) - 1:
            xml += page_break()
    return xml

def gen_ehrenwoertliche():
    xml = page_break()
    xml += heading1_no_num("Ehrenwörtliche Erklärung")
    xml += normal_para("Wir versichern hiermit ehrenwörtlich:", spacing_after=200)
    xml += normal_para(
        "1. dass wir unsere schriftliche Prüfungsleistung selbständig und ohne fremde Hilfe "
        "angefertigt und keine anderen Quellen und Hilfsmittel als die angegebenen verwendet haben,",
        spacing_after=200)
    xml += normal_para(
        "2. dass wir wissen, dass wir stets zu wissenschaftlicher Redlichkeit verpflichtet sind "
        "und die Grundsätze guter wissenschaftlicher Praxis eingehalten haben – das schließt auch "
        "die ggf. durch die Prüfer*innen für meine Arbeit weiterführenden Auflagen zur Umsetzung "
        "der guten wissenschaftlichen Praxis (z. B. der Umgang/die Nutzung KI-gestützter Werkzeuge) ein.",
        spacing_after=200)
    xml += normal_para(
        "3. dass wir insbesondere die Übernahme wörtlicher Zitate sowie die Verwendung oder "
        "Verarbeitung von Gedanken Dritter an den entsprechenden Stellen eindeutig gekennzeichnet haben.",
        spacing_after=200)
    xml += normal_para(
        "Uns ist bewusst, dass die Unrichtigkeit dieser Erklärung zur Folge haben kann, dass wir "
        "von der Ableistung weiterer Prüfungsleistungen nach § 15 Abs.3 sowie § 17 Abs.1 der "
        "Studien- und Prüfungsordnung der Hochschule für Wirtschaft und Umwelt Nürtingen-Geislingen "
        "– Allgemeiner Teil für Bachelor- und Masterstudiengänge in der jeweils geltenden Fassung "
        "ausgeschlossen werden bzw. ausgeschlossen sein können und dadurch unter Umständen den "
        "Prüfungsanspruch im Studiengang endgültig verlieren.",
        spacing_after=360)
    xml += normal_para("Nürtingen, 18.05.2026", spacing_after=600)
    xml += normal_para("_______________________________", spacing_after=0)
    return xml

FOOTER_XML = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    '<w:p><w:pPr><w:jc w:val="center"/><w:rPr>'
    '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
    '<w:sz w:val="24"/></w:rPr></w:pPr>'
    '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
    '<w:sz w:val="24"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
    '<w:r><w:instrText> PAGE </w:instrText></w:r>'
    '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')

def gen_section3_sectpr():
    return ('    <w:sectPr>'
            '<w:footerReference w:type="default" r:id="rId11"/>'
            '<w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1134" w:right="2835" w:bottom="1134" w:left="1134" '
            'w:header="720" w:footer="720" w:gutter="0"/>'
            '<w:pgNumType w:fmt="decimal" w:start="1"/>'
            '<w:cols w:space="720"/><w:docGrid w:linePitch="360"/>'
            '</w:sectPr>\n')

def main():
    print("=== Building Expose with formal framework elements ===")
    with open(DOC_XML, 'r', encoding='utf-8') as f:
        doc_xml = f.read()
    print("  Read document.xml: " + str(len(doc_xml)) + " chars")
    body_match = re.search(r'(<w:body>)\s*', doc_xml)
    if not body_match: raise ValueError("Could not find <w:body> tag")
    body_tag_end = body_match.end()
    sectpr_pattern = r'\s*<w:sectPr\s[^>]*>\s*.*?</w:sectPr>'
    all_sectpr = list(re.finditer(sectpr_pattern, doc_xml[body_tag_end:], re.DOTALL))
    if not all_sectpr: raise ValueError("Could not find <w:sectPr>")
    last_sectpr = all_sectpr[-1]
    sectpr_abs_start = body_tag_end + last_sectpr.start()
    header = doc_xml[:body_tag_end]
    body_text = doc_xml[body_tag_end:sectpr_abs_start]
    print("  Body text preserved: " + str(len(body_text)) + " chars")
    print("  Generating all framework elements...")
    pre_xml = gen_deckblatt() + gen_forschungsfrage() + gen_section_break_1()
    pre_xml += gen_toc() + gen_abkuerzungen() + gen_abbildungsverzeichnis()
    pre_xml += gen_gender_disclaimer() + gen_section_break_2()
    post_xml = page_break() + gen_literaturverzeichnis() + gen_anhangsverzeichnis()
    post_xml += gen_literaturlandkarte_anhang() + gen_anhang0() + gen_anhaenge() + gen_ehrenwoertliche()
    new_doc = header + '\n' + pre_xml + body_text + '\n' + post_xml + gen_section3_sectpr() + '  </w:body>\n</w:document>'
    with open(DOC_XML, 'w', encoding='utf-8') as f:
        f.write(new_doc)
    print("  Written document.xml: " + str(len(new_doc)) + " chars")
    for fn in ['footer1.xml', 'footer2.xml']:
        fp = os.path.join(WORK_DIR, 'word', fn)
        with open(fp, 'w', encoding='utf-8') as f: f.write(FOOTER_XML)
    print("  Created footer1.xml and footer2.xml")
    shutil.copy2(LOGO_SRC, LOGO_DST)
    print("  Copied logo")
    rels_path = os.path.join(WORK_DIR, 'word', '_rels', 'document.xml.rels')
    with open(rels_path, 'r', encoding='utf-8') as f: rels_xml = f.read()
    new_rels = ('  <Relationship Id="rId9" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image2.png"/>\n'
                '  <Relationship Id="rId10" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>\n'
                '  <Relationship Id="rId11" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer2.xml"/>\n')
    ip = rels_xml.find('</Relationships>')
    rels_xml = rels_xml[:ip] + new_rels + rels_xml[ip:]
    with open(rels_path, 'w', encoding='utf-8') as f: f.write(rels_xml)
    print("  Updated document.xml.rels")
    ct_path = os.path.join(WORK_DIR, '[Content_Types].xml')
    with open(ct_path, 'r', encoding='utf-8') as f: ct_xml = f.read()
    new_types = ('  <Default Extension="png" ContentType="image/png"/>\n'
                 '  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>\n'
                 '  <Override PartName="/word/footer2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>\n')
    ip = ct_xml.find('</Types>')
    ct_xml = ct_xml[:ip] + new_types + ct_xml[ip:]
    with open(ct_path, 'w', encoding='utf-8') as f: f.write(ct_xml)
    print("  Updated [Content_Types].xml")
    print("\n=== Done! Ready for packing. ===")

if __name__ == '__main__':
    main()
