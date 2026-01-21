# license_python
Dette er et lite Python-spill “Gjett tallet” som kun kan spilles med gyldig lisenskode.
Lisensene registreres via en enkel Flask-server, og hver lisens kan brukes flere ganger.


Filer
licenses.py → Oppretter databasen licenses.db og testlisenser

app.py → Flask-server for lisensregistrering og validering

game.py → Selve spillet

key.txt → Logger alle lisensforsøk


Fremgangsmåte
1. Opprett et virtuelt miljø: python -m venv .venv
2. Aktiver det virtuelle miljøet: .venv\Scripts\activate
3. Installer alle nødvendige biblioteker:          
python -m pip install requests                                     
python -m pip install flask
4. Opprett databasen (første gang): python licenses.py
5. Start serveren: python app.py
Serveren kjører på http://127.0.0.1:5000/. La dette vinduet stå åpent mens du spiller.
6. Registrer lisens (ny bruker): åpne nettleser og skriv: http://127.0.0.1:5000/register?email=ditt_email
Serveren returnerer en unik lisenskode.
7. Spill spillet: python game.py
Skriv inn din e-mail og lisenskoden du fikk fra serveren.
Hvis lisensen er gyldig → spillet starter.
Lisensen kan brukes flere ganger.
8. Alle lisensforsøk lagres i key.txt
  

Merk
Lisenskoden må registreres først via /register før spillet kan spilles.
Flask-serveren må alltid kjøre mens du spiller.
