# rpi-dashboard

Faccio una premessa, non sono un programmatore e questo launcher è stato creato come passatempo. ;)
Sono sicuro che non sarà elegante o ottimizzato, ma fa esattamente quello che cercavo.

L'obbiettivo era quello di utilizzare il mio raspberry con display osoyoo 3.5", in modo da poter visualizzare
delle schede in continuo aggiornamento.

Il programma utilizza:

- mqtt installato come docker container;
- cron per aggiornare i valori mqtt a intervalli regolari
- python per creare la maschera con tkinter e paho mqtt

L'idea è in continua evoluzione.

