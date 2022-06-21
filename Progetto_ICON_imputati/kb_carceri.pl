% Base di conoscenza
% --------------------------------

% Regole
%mostrare qualsiasi dato del carcere, dati uno o piu elementi
cercacarcere(Tipo, Citta, Regione, Posti) :- carcere(Tipo, Citta, Regione, Posti).

% --------------------------------
% 
% Dati 
%Formato: carcere(tipo_carcere, citta, regione, posti).
carcere(minorile, potenza, basilicata, 850).
carcere(minorile, campobasso, molise, 600).
carcere(minorile, l_aquila, abruzzo, 900).
carcere(minorile, milano, lombardia, 1000).
carcere(minorile, napoli, campania, 800).
carcere(minorile, bari, puglia, 600).
carcere(minorile, bergamo, lombardia, 800).
carcere(minorile, verona, veneto, 950).
carcere(minorile, trento, trentino_alto_adige, 1100).
carcere(minorile, bologna, emilia_romagna, 500).
carcere(minorile, firenze, toscana, 600).
carcere(minorile, perugia, umbria, 750).
carcere(minorile, ancona, marche, 650).
carcere(minorile, lecce, puglia, 750).
carcere(minorile, taranto, puglia, 1000).
carcere(minorile, foggia, puglia, 1200).
carcere(minorile, catanzaro, calabria, 550).
carcere(minorile, palermo, sicilia, 950).
carcere(minorile, cagliari, sardegna, 600).
carcere(minorile, aosta, valle_d_aosta, 400).
carcere(minorile, trieste, friuli_venezia_giulia, 550).
carcere(minorile, torino, piemonte, 950).
carcere(minorile, novara, piemonte, 600).
carcere(minorile, genova, liguria, 650).
carcere(minorile, roma, lazio, 1400).
carcere(penitenziario, bari, puglia, 1000).
carcere(penitenziario, milano, lombardia, 1100).
carcere(penitenziario, napoli, campania, 850).
carcere(penitenziario, bergamo, lombardia, 700).
carcere(penitenziario, verona, veneto, 950).
carcere(penitenziario, trento, trentino_alto_adige, 1000).
carcere(penitenziario, bologna, emilia_romagna, 650).
carcere(penitenziario, firenze, toscana, 650).
carcere(penitenziario, perugia, umbria, 850).
carcere(penitenziario, ancona, marche, 550).
carcere(penitenziario, lecce, puglia, 700).
carcere(penitenziario, taranto, puglia, 900).
carcere(penitenziario, foggia, puglia, 1100).
carcere(penitenziario, potenza, basilicata, 800).
carcere(penitenziario, l_aquila, abruzzo, 800).
carcere(penitenziario, campobasso, molise, 650).
carcere(penitenziario, catanzaro, calabria, 750).
carcere(penitenziario, palermo, sicilia, 900).
carcere(penitenziario, cagliari, sardegna, 700).
carcere(penitenziario, aosta, valle_d_aosta, 450).
carcere(penitenziario, trieste, friuli_venezia_giulia, 650).
carcere(penitenziario, torino, piemonte, 1000).
carcere(penitenziario, novara, piemonte, 650).
carcere(penitenziario, genova, liguria, 640).
carcere(penitenziario, roma, lazio, 1300).
carcere(massima_sicurezza, bari, puglia, 550).
carcere(massima_sicurezza, milano, lombardia, 1250).
carcere(massima_sicurezza, napoli, campania, 750).
carcere(massima_sicurezza, verona, veneto, 1050).
carcere(massima_sicurezza, trento, trentino_alto_adige, 800).
carcere(massima_sicurezza, bologna, emilia_romagna, 750).
carcere(massima_sicurezza, firenze, toscana, 750).
carcere(massima_sicurezza, perugia, umbria, 650).
carcere(massima_sicurezza, ancona, marche, 600).
carcere(massima_sicurezza, potenza, basilicata, 700).
carcere(massima_sicurezza, l_aquila, abruzzo, 750).
carcere(massima_sicurezza, campobasso, molise, 500).
carcere(massima_sicurezza, catanzaro, calabria, 950).
carcere(massima_sicurezza, palermo, sicilia, 1150).
carcere(massima_sicurezza, cagliari, sardegna, 900).
carcere(massima_sicurezza, aosta, valle_d_aosta, 300).
carcere(massima_sicurezza, trieste, friuli_venezia_giulia, 650).
carcere(massima_sicurezza, torino, piemonte, 1000).
carcere(massima_sicurezza, genova, liguria, 950).
carcere(massima_sicurezza, roma, lazio, 1450).
