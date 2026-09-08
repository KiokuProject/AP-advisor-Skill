[English](./README.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md) | [한국어](./README.ko.md) | **Deutsch**

# AP Advisor Skills

Schicke eine Aufgabe und deinen Lösungsversuch. Die Skills helfen dir, den
ersten Fehler zu finden, diesen Schritt zu korrigieren und die nächste Übung
passend zu deiner Antwort auszuwählen.

Die fünf Skills unterstützen sieben AP-Kurse in Codex. Du kannst Englisch,
Japanisch, vereinfachtes oder traditionelles Chinesisch, Koreanisch und Deutsch verwenden.

| Skill zum Installieren | Unterstützte Kurse |
| --- | --- |
| [ap-calculus-advisor](./ap-calculus-advisor/) | AP Precalculus, AP Calculus AB, AP Calculus BC |
| [ap-psychology-advisor](./ap-psychology-advisor/) | AP Psychology (Psychologie) |
| [ap-biology-advisor](./ap-biology-advisor/) | AP Biology (Biologie) |
| [ap-csa-advisor](./ap-csa-advisor/) | AP Computer Science A (CSA) |
| [ap-csp-advisor](./ap-csp-advisor/) | AP Computer Science Principles (CSP) |

## Loslegen

Bitte den Skill Installer, die gewünschten Fächer zu installieren:

```text
$skill-installer Install the skill at path ap-calculus-advisor from iyorixy/AP-advisor-Skill as ap-calculus-advisor.
$skill-installer Install the skill at path ap-psychology-advisor from iyorixy/AP-advisor-Skill as ap-psychology-advisor.
$skill-installer Install the skill at path ap-biology-advisor from iyorixy/AP-advisor-Skill as ap-biology-advisor.
$skill-installer Install the skill at path ap-csa-advisor from iyorixy/AP-advisor-Skill as ap-csa-advisor.
$skill-installer Install the skill at path ap-csp-advisor from iyorixy/AP-advisor-Skill as ap-csp-advisor.
```

Installiere die einzelnen Fachordner, nicht das Stammverzeichnis des Repositorys.
Falls ein installierter Skill nicht erscheint, starte Codex neu. Die lokalen
Prüfskripte benötigen Python 3.10 oder neuer und nur dessen Standardbibliothek.

Füge die Aufgabe, benötigte Grafiken, Daten oder Code sowie deinen Versuch hinzu:

```text
$ap-calculus-advisor Ich lerne AP Calculus AB. Wähle die nächste Aufgabe anhand meiner Fehler. Gib jeweils nur einen Hinweis und lass mich selbst versuchen, bevor du die Lösung zeigst.
```

Noch kein Versuch? Nenne den Kurs und das gewünschte Thema. Coach stellt eine
Aufgabe und wartet auf deine Antwort. Du musst keinen Topic-Code kennen.

## Wobei die Skills helfen

| Dein Ziel | Beispiel für eine Anfrage |
| --- | --- |
| Ein Konzept verstehen oder üben (Generate) | „Erkläre das und gib mir eine ähnliche Aufgabe ohne Lösung.“ |
| Die eigene Lösung prüfen (Review) | „Finde den ersten Fehler in meinem Lösungsweg.“ |
| Lernschwerpunkte setzen (Advisor) | „Wähle anhand dieser Fehler die nächsten ein bis drei Übungen aus.“ |
| Nach jedem Versuch passende Rückmeldung erhalten (Coach) | „Führe mich Schritt für Schritt und passe die nächste Aufgabe an meine Fehler an.“ |

Du musst dir die Modusnamen nicht merken. Du kannst jederzeit eine vollständige
Erklärung verlangen, das Thema wechseln oder das Coaching beenden.

## So passt Coach die Übungen an

Für alle sieben Kurse gilt: **Dein tatsächlicher Fehler bestimmt den nächsten
Schritt.** Eine niedrige Punktzahl oder eine falsche Antwortoption allein erklärt
noch nicht die Ursache.

| Was dein Versuch zeigt | Was Coach als Nächstes tut |
| --- | --- |
| Ein Konzept oder eine Regel wird verwechselt | Stellt einen kurzen Vergleich an oder prüft eine Anwendungsvoraussetzung. |
| Der Ansatz stimmt, aber die Rechnung nicht | Hilft bei diesem Rechenschritt und hält das Niveau ähnlich. |
| Eine Grafik oder Tabelle wird falsch gelesen | Lässt dich zunächst ein wichtiges Merkmal ablesen. |
| Die Definition stimmt, aber der Bezug zur Situation fehlt | Fragt nach der Verbindung zu einem konkreten Detail. |
| Im Modell, Versuchsaufbau oder Argument fehlt etwas | Konzentriert sich auf die fehlende Beziehung, den Vergleich oder die Begründung. |
| Ein Index, eine Schleifengrenze oder ein Objektzustand wird falsch behandelt | Prüft einen Ausführungsschritt oder einen gezielten Testfall. |
| Eine Bedingung oder Teilantwort wurde übersehen | Lässt dich nur die fehlende Anforderung ergänzen. |

Zum Beispiel bei einer selbst erstellten Ableitungsaufgabe:

> **Du:** Für f(x) = x³ − 2x erhalte ich f′(x) = 3x² + 2.
>
> **Coach:** Der erste Term stimmt. Prüfe das Vorzeichen bei −2x und leite nur diesen Term ab.

Dann wartet Coach. Er erfindet weder deine Korrektur noch gibt er dir sofort
ein ganzes Arbeitsblatt.

Nach der Korrektur folgt **eine neue Aufgabe desselben Typs ohne Hinweise**.
Wenn du sie selbstständig löst, ändert die nächste Aufgabe ein wesentliches
Merkmal, etwa den Kontext oder die Darstellung. Bei Schwierigkeiten nehmen die
Hinweise schrittweise zu. Reicht auch Stufe 3 nicht aus, wird eine benötigte
Grundlage in einen kleineren Schritt zerlegt.

Eine gelöste Transferaufgabe zeigt Fortschritt bei diesem konkreten Lernziel.
Ein späterer Fehler löscht keine unabhängigen Erfolge, und ein einzelner Erfolg
belegt nicht die Beherrschung einer ganzen Einheit. Ausdrücklich festgelegte
Kurse, Topics, Aufgabenarten und Schwierigkeitsgrade bleiben erhalten.

## Beispiele für die einzelnen Fächer

```text
$ap-calculus-advisor Ich lerne AP Precalculus. Wähle anhand meines Versuchs zu diesem Funktionsgraphen den nächsten Schritt.
$ap-calculus-advisor Prüfe meine Ableitung in AP Calculus AB und hilf mir ab dem ersten Fehler Schritt für Schritt.
$ap-calculus-advisor Wähle anhand meiner Antwort zur Reihenkonvergenz in AP Calculus BC die nächste Übung.
$ap-psychology-advisor Ich kenne die Definition, kann sie aber nicht anwenden. Führe mich anhand meiner Antwort durch jeweils eine Aufgabe.
$ap-biology-advisor Prüfe an meiner Grafikbeschreibung und Erklärung, ob ich Daten falsch lese oder den biologischen Mechanismus nicht erkläre. Gib mir einen Schritt.
$ap-csa-advisor Meine Java-Schleife überspringt nach dem Entfernen aus einer ArrayList benachbarte Treffer. Gib mir anhand meines Codes einen Hinweis und prüfe mich danach mit einer neuen Aufgabe.
$ap-csp-advisor Wähle anhand meiner Ablaufverfolgung von AP-Pseudocode die nächste Übung. Danach möchte ich anhand meines eigenen Codes eine Prozedur erklären.
```

Füge jeweils die ursprüngliche Aufgabe und deinen tatsächlichen Versuch hinzu.

## Gut zu wissen

- **Die Übungsaufgaben werden eigens erstellt.** Für Mathematik gibt es 96
  gepflegte Aufgaben zu 32 Fehlermustern; Lücken werden bei Bedarf durch neue
  Aufgaben ergänzt. Biologie, Psychologie, CSA und CSP erstellen Übungen nach
  Bedarf. Das ist keine vollständige Aufgabensammlung und kein Zugang zu
  vertraulichem AP-Classroom-Material.
- **Du entscheidest, wann du die Lösung siehst.** Coach lässt dich normalerweise
  zuerst selbst versuchen. Eine mit Hilfe gelöste Aufgabe zählt nicht als
  selbstständiger Erfolg.
- **Lernstände bleiben standardmäßig im Gespräch.** Mathematik kann auf deinen
  ausdrücklichen Wunsch einen lokalen Lernstand in einem von dir angegebenen
  Ordner außerhalb des Repositorys speichern. Biologie, Psychologie, CSA und
  CSP verwenden nur den Gesprächsverlauf.
- **CSA und CSP folgen getrennten Rahmenplänen.** CSA verwendet den Java-Rahmenplan
  Fall 2025; CSP im Schuljahr 2026–27 den Rahmenplan Fall 2023. CSP unterstützt
  Create-Übungen und zulässige Hilfe beim Programmieren. Die Anforderungen an
  individuell erstellte Videos, PPRs und Prüfungsantworten werden gesondert erklärt.
- **Die Skills geben dem Modell Orientierung; Fehler bleiben möglich.** Sie
  enthalten Anweisungen für GPT-6 Astra und andere geeignete Modelle. Eine
  Topic-Prüfung bestätigt weder die Richtigkeit einer Erklärung noch einer
  Bewertung. Offizielle Punkte erfordern die passende Aufgabe und Bewertungsrichtlinie.

Kursdetails findest du in den oben verlinkten Skills. Lokale Lernstände,
Prüfungen und die Umsetzung beschreibt die [Entwicklungsdokumentation (Englisch)](./docs/development.md).

## Lizenz

[MIT](./LICENSE). AP ist eine Marke des College Board. Dieses Projekt wird nicht
vom College Board unterstützt oder anerkannt.
