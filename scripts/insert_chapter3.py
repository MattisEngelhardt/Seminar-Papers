import os

# Dynamic path resolution: relative to workspace root (one directory up from scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.dirname(SCRIPT_DIR)
doc_path = os.path.join(WORKSPACE_ROOT, "unpacked_expose", "word", "document.xml")

if not os.path.exists(doc_path):
    # Fallback to the original hardcoded path if relative path doesn't exist
    doc_path = r"c:\Users\engel\OneDrive\000000000000000000000000000 mg3\unpacked_expose\word\document.xml"

if os.path.exists(doc_path):
    with open(doc_path, "r", encoding="utf-8") as f:
        xml = f.read()
else:
    raise FileNotFoundError(f"Could not locate document.xml. Searched path: {doc_path}")

def h1(text):
    return f'''    <w:p w14:paraId="03000001" w14:textId="77777777" w:rsidR="00CC0001" w:rsidRDefault="00CC0001">
      <w:pPr>
        <w:pStyle w:val="berschrift1"/>
        <w:spacing w:before="240"/>
        <w:jc w:val="left"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        </w:rPr>
        <w:t>{text}</w:t>
      </w:r>
    </w:p>'''

def h2(text, pid):
    return f'''    <w:p w14:paraId="{pid}" w14:textId="77777777" w:rsidR="00CC0001" w:rsidRDefault="00CC0001">
      <w:pPr>
        <w:pStyle w:val="berschrift2"/>
        <w:spacing w:before="240" w:after="120"/>
        <w:jc w:val="left"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
          <w:sz w:val="24"/>
        </w:rPr>
        <w:t>{text}</w:t>
      </w:r>
    </w:p>'''

def body_p(text, pid):
    return f'''    <w:p w14:paraId="{pid}" w14:textId="77777777" w:rsidR="00CC0001" w:rsidRDefault="00CC0001">
      <w:r>
        <w:t>{text}</w:t>
      </w:r>
    </w:p>'''

def bold_body(bold_text, rest_text, pid):
    return f'''    <w:p w14:paraId="{pid}" w14:textId="77777777" w:rsidR="00CC0001" w:rsidRDefault="00CC0001">
      <w:r>
        <w:rPr><w:b/></w:rPr>
        <w:t xml:space="preserve">{bold_text} </w:t>
      </w:r>
      <w:r>
        <w:t>{rest_text}</w:t>
      </w:r>
    </w:p>'''

def q(s):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("„", "&#x201E;")
    s = s.replace("“", "&#x201C;")
    s = s.replace("”", "&#x201D;")
    return s

paras = []
paras.append(h1("3 Untersuchungsdesign"))

paras.append(body_p(q(
    "Das Untersuchungsdesign charakterisiert die methodische Vorgehensweise einer Studie; "
    "die zugrunde liegenden Entscheidungen müssen im Sinne intersubjektiver Nachvollziehbarkeit "
    "transparent gemacht werden (vgl. Döring, 2023, S. 184). Im Folgenden werden die zentralen "
    "Designentscheidungen für die in Abschnitt 2.6 abgeleitete Forschungsfrage dargelegt und begründet."
), "03010001"))

paras.append(h2("3.1 Erkenntnisziel und Erkenntnisinteresse", "03020001"))

paras.append(body_p(q(
    "Das Erkenntnisziel ist die Grundlagenforschung. Die Einordnung leitet sich logisch aus der "
    "Forschungsfrage ab: Die Frage nach der „Rolle“ von KI zielt auf den Aufbau von Verständnis "
    "über ein kaum untersuchtes Phänomen — konkret die Erweiterung des Unit-Profitability-First-Gedankens "
    "um eine KI-Dimension —, nicht auf die Lösung eines konkreten Unternehmensproblems "
    "(vgl. Döring, 2023, S. 187). Die dreigliedrige Abgrenzung zwischen Grundlagen-, Interventions- "
    "und Evaluationsforschung bestätigt diese Einordnung, da die Forschungsfrage weder auf die "
    "zielgerichtete Veränderung von Sachverhalten noch auf die Bewertung von Maßnahmen abzielt, "
    "sondern auf die Entwicklung von Theorien zur Beschreibung und Erklärung eines Phänomens "
    "(vgl. Döring, 2023, S. 953). Auch eine Einordnung als Anwendungsforschung, die auf die Lösung "
    "konkreter Praxisprobleme abzielt (vgl. Döring, 2023, S. 187), scheidet aus, da keine "
    "Handlungsempfehlungen im Auftrag abgeleitet werden."
), "03030001"))

paras.append(body_p(q(
    "Das Erkenntnisinteresse ist explorativ, da die Forschungsfrage auf die Erkundung eines "
    "Sachverhalts mit dem Ziel der Theoriebildung zielt (vgl. Döring, 2023, S. 194). Diese Einordnung "
    "ergibt sich nachvollziehbar aus dem aktuellen Forschungsstand: Die Schnittmenge aus KI-Einsatz, "
    "Gründungsphase, B2C-E-Commerce und Unit-Profitability-First stellt wissenschaftliches Neuland "
    "dar — es existieren keine etablierten Theorien oder überprüfbaren Hypothesen hierzu. "
    "Ein deskriptives Erkenntnisinteresse scheidet aus, da es repräsentative "
    "Stichproben und Populationsbeschreibungen erfordert; ein explanatives setzt vorab aufgestellte "
    "Hypothesen voraus, die mangels Forschungsstand nicht ableitbar sind (vgl. Döring, 2023, S. 194). "
    "Explorative Studien werden häufig als qualitative Studien durchgeführt, da dieses Vorgehen "
    "offen ist für unerwartete Befunde (vgl. Döring, 2023, S. 194)."
), "03040001"))

paras.append(h2("3.2 Gegenstand", "03050001"))

paras.append(body_p(q(
    "Gegenstand der Arbeit ist eine empirische Studie, da die Forschungsfrage eine eigene "
    "Datenerhebung erfordert und nicht durch eine reine Literaturarbeit beantwortet werden kann "
    "(vgl. Döring, 2023, S. 188). Eine Theoriestudie kommt ebenso wenig in Frage wie eine "
    "Methodenstudie, da die empirische Erkundung eines inhaltlichen Phänomens im Vordergrund steht. "
    "Bei Qualifikationsarbeiten fällt "
    "die Wahl meist auf eine empirische Originalstudie (vgl. Döring, 2023, S. 193); eine "
    "Replikationsstudie scheidet aus, da keine vergleichbaren Vorgängerstudien existieren."
), "03060001"))

paras.append(body_p(q(
    "Die Datengrundlage ist eine Primäranalyse. Diese Einordnung ergibt sich nachvollziehbar "
    "aus dem aktuellen Forschungsstand: Die Daten zum Zusammenhang von KI-Einsatz und "
    "Unit-Economics-Entscheidungen in der Gründungsphase müssen selbst erhoben und analysiert "
    "werden (vgl. Döring, 2023, S. 193), da weder Datensätze für eine Sekundäranalyse noch eine "
    "hinreichende Dichte vergleichbarer Studien für eine Metaanalyse vorliegen — eine Metaanalyse "
    "wäre zudem „methodisch aufwendig und komplex, d. h. als Einstiegsstudie für Neulinge eher "
    "ungeeignet“ (Döring, 2023, S. 194)."
), "03070001"))

paras.append(h2("3.3 Ansatz", "03080001"))

paras.append(body_p(q(
    "Zur Beantwortung der Forschungsfrage wird ein qualitativer Forschungsansatz gewählt, "
    "bei dem offene Forschungsfragen an wenigen Fällen detailliert mit dem Ziel der Theoriebildung "
    "untersucht werden (vgl. Döring, 2023, S. 186). Die Wahl ergibt sich nachvollziehbar aus dem "
    "aktuellen Forschungsstand: Ein qualitatives Design ist insbesondere dann indiziert, wenn ein "
    "neuer Gegenstand erkundet und eine Theorie entwickelt werden soll (vgl. Döring, 2023, S. 187). "
    "Ein quantitatives Design scheidet aus, da es vorab operationalisierte Variablen und überprüfbare "
    "Hypothesen voraussetzt, die beim aktuellen Forschungsstand nicht "
    "ableitbar sind. Der qualitative Ansatz folgt einer theorieentdeckenden Forschungslogik, bei der "
    "das induktive, datengestützte Vorgehen besonders wichtig ist (vgl. Döring, 2023, S. 25). "
    "Die theoretischen Konzepte aus dem Literature Review — Dynamic Capabilities, Unit Profitability "
    "First und das DTC-Modell — fungieren als „sensibilisierende Konzepte“ "
    "(Döring, 2023, S. 169), die den Blick für die qualitative Exploration schärfen, ohne ihn "
    "durch vorab fixierte Hypothesen zu verengen."
), "03090001"))

paras.append(body_p(q(
    "Ergänzend wird das Mixed-Method-Potenzial im Sinne eines Vorstudienmodells reflektiert. "
    "Da die Forschungsfrage auf Theoriebildung zielt, kommt das Vorstudienmodell in Betracht, bei dem "
    "eine qualitative Studie Hypothesen generiert, die anschließend quantitativ geprüft werden "
    "(vgl. Döring, 2023, S. 186). Die vorliegende Primärstudie könnte Hypothesen über die "
    "spezifischen KI-Rollen für Unit Profitability generieren. Demgegenüber setzt das "
    "Vertiefungsmodell eine quantitative Ausgangsstudie voraus (vgl. Döring, 2023, S. 27), die "
    "mangels operationalisierbarer Variablen nicht durchführbar ist — es kommt daher ausschließlich "
    "das Vorstudienmodell in Betracht. Ein vollständiges Mixed-Methods-Design wird nicht realisiert, "
    "da die erforderlichen Vorkenntnisse in beiden Forschungsparadigmen sowie die zeitlichen und "
    "personellen Ressourcen dies nicht zulassen (vgl. Döring, 2023, S. 187)."
), "030A0001"))

paras.append(h2("3.4 Untersuchungsobjekte", "030B0001"))

paras.append(body_p(q(
    "Die Grundgesamtheit leitet sich logisch aus der Forschungsfrage ab: Gründerinnen und Gründer "
    "sowie Führungskräfte von B2C-E-Commerce-Startups in der Gründungsphase, die KI-Tools im "
    "Kontext von Unit-Profitability-Entscheidungen einsetzen. Die Eingrenzung erfolgt zeitlich "
    "(Gründungsphase, ca. null bis drei Jahre), inhaltlich (B2C-E-Commerce als Geschäftsmodell) und "
    "durch den nachweisbaren KI-Einsatz — diese Merkmale definieren die Zielpopulation "
    "(vgl. Döring, 2023, S. 294). Führungskräfte werden einbezogen, da operative und strategische "
    "Entscheidungen häufig nicht trennscharf auf eine Rolle beschränkt sind."
), "030C0001"))

paras.append(body_p(q(
    "Es wird eine Gruppenstudie durchgeführt, da die Forschungsfrage auf das Phänomen KI in der "
    "Gründungsphase allgemein zielt — auf fallübergreifende Muster in der KI-Nutzung, nicht auf "
    "einen individuellen Einzelfall (vgl. Döring, 2023, S. 216). Eine Einzelfallstudie wäre nur "
    "indiziert, wenn sich die Forschungsfrage auf einen individuellen Einzelfall bezöge "
    "(vgl. Döring, 2023, S. 218)."
), "030D0001"))

paras.append(body_p(q(
    "Die Fallauswahl folgt dem Prinzip der bewussten Auswahl im Sinne des Theoretical Sampling: "
    "Anhand bisheriger Ergebnisse werden schrittweise weitere Fälle aufgenommen "
    "(vgl. Döring, 2023, S. 303), bis die theoretische Sättigung erreicht ist — also KI-Rollen "
    "und Unit-Economics-Muster keine neuen Kategorien mehr hervorbringen "
    "(vgl. Döring, 2023, S. 304). Als Orientierungsrahmen werden sechs bis zehn Interviews "
    "angestrebt. Die Rekrutierung erfolgt über das Schneeballverfahren, da die "
    "B2C-E-Commerce-Gründerszene für akademische Forschung schwer zugänglich, intern aber über "
    "Accelerator-Kohorten und Investorenkreise eng vernetzt ist (vgl. Döring, 2023, S. 310)."
), "030E0001"))

paras.append(h2("3.5 Auswahl Erhebungsinstrumente", "030F0001"))

paras.append(body_p(q(
    "Für die Datenerhebung werden zwei qualitative Erhebungsinstrumente hinsichtlich ihrer "
    "Eignung für die vorliegende Forschungsfrage geprüft: die wissenschaftliche Beobachtung "
    "und das leitfadengestützte Experteninterview."
), "03100001"))

paras.append(bold_body(
    q("Instrument A: Wissenschaftliche Beobachtung."),
    q("Die systematische Erfassung von Merkmalen und Verhaltensweisen zum Zeitpunkt ihres "
      "Auftretens (vgl. Döring, 2023, S. 323) wäre für die Beobachtung von KI-Nutzungsroutinen "
      "im Startup-Alltag grundsätzlich denkbar. Allerdings nimmt die Beobachtung eine "
      "Außenperspektive ein und bietet keinen Zugang zur Innenwelt der Untersuchungspersonen "
      "(vgl. Döring, 2023, S. 324); viele subjektive Erlebensphänomene sind einer "
      "Fremdbeobachtung nicht zugänglich und müssen erfragt werden "
      "(vgl. Döring, 2023, S. 325). Die Forschungsfrage zielt jedoch auf kognitive "
      "Entscheidungsprozesse — Überzeugungen, strategische Abwägungen und subjektive "
      "Rollenzuschreibungen bezüglich des KI-Einsatzes für Unit Profitability —, die von "
      "außen nicht beobachtbar sind."),
    "03110001"
))

paras.append(bold_body(
    q("Instrument B: Leitfadengestütztes Experteninterview."),
    q("Die Interviewtechnik erschließt Aspekte des subjektiven Erlebens, die der Beobachtung "
      "nicht zugänglich sind, und ermöglicht die Erfassung nicht direkt beobachtbarer Ereignisse "
      "(vgl. Döring, 2023, S. 353). Als Format wird das leitfadengestützte Experteninterview "
      "gewählt, das durch sein Grundgerüst Vergleichbarkeit sichert "
      "(vgl. Döring, 2023, S. 367), während es das Spezialwissen der Befragten — strukturelles "
      "Fachwissen ebenso wie schwer verbalisierbares Praxis- und Handlungswissen — systematisch "
      "erschließt (vgl. Döring, 2023, S. 371). Gründerinnen und Gründer von "
      "B2C-E-Commerce-Startups verfügen über beide Wissenstypen: strukturelles Fachwissen zu "
      "KI-Tools und Unit Economics sowie Praxis- und Handlungswissen, das oft stark verinnerlicht "
      "ist und nur im Interview mobilisiert werden kann (vgl. Döring, 2023, S. 371). Dem stehen "
      "als Nachteile der hohe Zeitaufwand sowie das Risiko sozialer Erwünschtheit und Reaktivität "
      "gegenüber (vgl. Döring, 2023, S. 354)."),
    "03120001"
))

paras.append(bold_body(
    q("Begründete Auswahl."),
    q("Unter Beachtung des bislang definierten explorativen, qualitativen Designs mit "
      "Grundlagenforschungszielsetzung wird das leitfadengestützte Experteninterview als "
      "Erhebungsinstrument gewählt. Erstens zielt die Forschungsfrage auf kognitive "
      "Entscheidungsprozesse und subjektive Rollenzuschreibungen, die einer Beobachtung nicht "
      "zugänglich sind. Zweitens bietet das Interview eine höhere Informationsdichte: "
      "Ausführliche Schilderungen zeitlich ausgedehnter Prozesse erhält man nur mündlich im "
      "Zuge qualitativer Interviews (vgl. Döring, 2023, S. 354) — die Gründungsphase eines "
      "E-Commerce-Startups ist ein solcher vielschichtiger Prozess. Drittens ermöglicht das "
      "Leitfaden-Format die Balance zwischen Vergleichbarkeit und Offenheit, die bei einem "
      "explorativen Design unverzichtbar ist. Der Fragebogen wird verworfen, da er klar umschriebene "
      "Befragungsinhalte voraussetzt und längere Erzählungen ausschließt "
      "(vgl. Döring, 2023, S. 393) — die erforderlichen Variablen sind bei diesem kaum "
      "erforschten Zusammenhang nicht vorab identifizierbar. Auch die Dokumentenanalyse scheidet "
      "aus: Zwar bieten Startup-Dokumente einen nonreaktiven Datenzugang "
      "(vgl. Döring, 2023, S. 525), doch fehlen häufig die Kontextinformationen zu "
      "Erstellungsumständen und -absichten (vgl. Döring, 2023, S. 529). Die subjektiven "
      "Entscheidungslogiken der Gründerinnen und Gründer sind aus vorgefundenen Dokumenten nicht "
      "rekonstruierbar."),
    "03130001"
))

paras.append(bold_body(
    q("Hinweise zum weiteren Vorgehen."),
    q("Der Ablauf orientiert sich am zehnschrittigen Vorgehensmodell "
      "(vgl. Döring, 2023, S. 361); ein Leitfaden mit acht bis fünfzehn offenen Fragen "
      "(vgl. Döring, 2023, S. 368) wird erstellt und in einem Probe-Interview auf "
      "Verständlichkeit geprüft. Der Leitfaden umfasst thematisch den KI-Einsatz im "
      "Startup-Alltag, die Rolle von KI bei Unit-Economics-Entscheidungen sowie die wahrgenommenen "
      "Wirkungen auf die Profitabilitätsorientierung. Die Interviews werden per Audio dokumentiert; "
      "die informierte Einwilligung wird vorab eingeholt (vgl. Döring, 2023, S. 121), nach jedem "
      "Gespräch ein Postskriptum angefertigt. Die Transkripte werden vollständig wortwörtlich "
      "verschriftet (vgl. Döring, 2023, S. 362) und mittels qualitativer Inhaltsanalyse nach "
      "Mayring mit deduktiv-induktivem Vorgehen ausgewertet (vgl. Döring, 2023, S. 533): Die "
      "deduktiven Ausgangskategorien leiten sich aus den Konzepten des Literature Reviews ab — "
      "Dynamic Capabilities, Unit-Economics-Kennzahlen, KI-Anwendungsfelder —, während induktive "
      "Kategorien bislang unbekannte KI-Rollen abbilden. Die Kodierung erfolgt fallbezogen und "
      "fallübergreifend zur Identifikation übergeordneter Muster, Typen sowie wiederkehrender "
      "Meinungen, Einstellungen und Trends (vgl. Döring, 2023, S. 592), unterstützt durch "
      "QDA-Software wie MAXQDA (vgl. Döring, 2023, S. 598)."),
    "03140001"
))

chapter3_xml = "\n".join(paras)
xml = xml.replace("    <w:sectPr", f"{chapter3_xml}\n    <w:sectPr")

with open(doc_path, "w", encoding="utf-8") as f:
    f.write(xml)

print("Chapter 3 inserted successfully")
