import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors

pdf_path = r"c:\Users\1\Documents\Antigravity\msn3\ChatTT\ChatTT_Fejlesztesi_Utmutato.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()

# Custom Styles
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=colors.HexColor('#1E3C72'),
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'SubTitleStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#475569'),
    spaceAfter=15
)

h2_style = ParagraphStyle(
    'H2Style',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#1E3C72'),
    spaceBefore=12,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#1E293B'),
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=body_style,
    leftIndent=15,
    firstLineIndent=-10,
    spaceAfter=6
)

code_style = ParagraphStyle(
    'CodeStyle',
    parent=styles['Normal'],
    fontName='Courier-Oblique',
    fontSize=9.5,
    leading=13,
    textColor=colors.HexColor('#0F172A'),
    backColor=colors.HexColor('#F1F5F9'),
    borderColor=colors.HexColor('#CBD5E1'),
    borderWidth=0.5,
    borderPadding=6,
    spaceAfter=8
)

story = []

# Title & Header
story.append(Paragraph("<b>ChatTT - Okos Fejlesztési Útmutató</b>", title_style))
story.append(Paragraph("Párhuzamos együttműködés Alexszal (adamcsaka) az Antigravity AI és GitHub segítségével", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2A5298'), spaceAfter=14))

# Section 1
story.append(Paragraph("1. A Git &amp; GitHub Munkamenet (Branching &amp; Remotes)", h2_style))
story.append(Paragraph("A független és tiszta fejlesztés érdekében használjátok a <b>Feature Branch</b> modellt:", body_style))

story.append(Paragraph("• <b>Saját fejlesztési ágak (Branch-ek) használata:</b><br/>Ne dolgozzatok közvetlenül a <i>main</i> ágon. Ha egy új funkción (pl. <i>hangüzenetek</i> vagy <i>MSN állapotüzenet</i>) dolgozol, kérd meg az Antigravity-t:", bullet_style))
story.append(Paragraph('"Hozz létre egy feature/voice-messages git ágat és ott valósítsuk meg a funkciót."', code_style))

story.append(Paragraph("• <b>Pull Request (PR) küldése Alexnak:</b><br/>Amikor elkészül egy funkció, az Antigravity segítségével vagy a GitHubon küldj egy <b>Pull Request</b>-et Alex repójába (<i>adamcsaka/ChatTT</i>). Alex átnézheti és egy kattintással beolvaszthatja a fő repóba.", bullet_style))

story.append(Paragraph("• <b>Upstream frissítések lekérése 1 paranccsal:</b><br/>Bármikor, amikor Alex fejleszt valamit a saját repójában, csak mondd ezt az Antigravity-nek:", bullet_style))
story.append(Paragraph('"Frissítsük és mergeljük a legújabb upstream módosításokat Alex repójából!"', code_style))

story.append(Spacer(1, 10))

# Section 2
story.append(Paragraph("2. Az Antigravity AI Okos Használata", h2_style))
story.append(Paragraph("Az Antigravity nem csak kódot ír, hanem automatizálja az egész munkafolyamatot:", body_style))

story.append(Paragraph("• <b>Automatikus Élő Tesztelés és Weboldal Telepítés (GitHub Pages):</b><br/>Minden alkalommal, amikor elkészül egy frissítés, az Antigravity automatikusan pushol a GitHubra. Az élő tesztkörnyezeted mindig elérhető a <u>https://sid14925.github.io/ChatTT/</u> címen.", bullet_style))
story.append(Paragraph("• <b>Automatikus EXE Fordítás:</b><br/>Nem kell manuálisan fordítanotok a Windows futtatható fájlokat; az Antigravity a háttérben legenerálja a legfrissebb .exe fájlt és a hordozható ZIP-et.", bullet_style))
story.append(Paragraph("• <b>Összetett Funkciók Tervezése (Planning Mode):</b><br/>Ha egy komolyabb újítást szeretnétek (pl. <i>Videóhívás WebRTC-vel</i>), használd a <b>/grill-me</b> parancsot, vagy kérd meg az Antigravity-t, hogy készítsen egy részletes <i>implementation_plan.md</i> tervet.", bullet_style))

story.append(Spacer(1, 10))

# Section 3
story.append(Paragraph("3. Gyakorlati Munkaterv (Példa egy közös fejlesztési napra)", h2_style))

data = [
    [Paragraph("<b>1. Szinkronizáció</b><br/>Antigravity: 'Nézd meg van-e új commit Alex repójában!'", body_style),
     Paragraph("<b>2. Új Funkció</b><br/>Készítsetek egyedi állapotüzeneteket új git ágon.", body_style)],
    [Paragraph("<b>3. Teszt &amp; EXE</b><br/>Automata csomagolás és push a GitHubra.", body_style),
     Paragraph("<b>4. Merge Alexnak</b><br/>Nyiss Pull Request-et az adamcsaka/ChatTT felé.", body_style)]
]

table = Table(data, colWidths=[240, 240])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))

story.append(table)

story.append(Spacer(1, 14))

# Section 4
story.append(Paragraph("💡 Hasznos Parancsok az Antigravity-ben:", h2_style))
story.append(Paragraph("<b>/grill-me</b> — Architektúra Tervezés &nbsp;&nbsp;|&nbsp;&nbsp; <b>/goal</b> — Önmagát Vezérlő Tervezés &nbsp;&nbsp;|&nbsp;&nbsp; <b>/schedule</b> — Háttér Időzítés", body_style))

doc.build(story)
print("PDF generated successfully")
