# rpi-dashboard

Devo fare una premessa: non sono un programmatore e questo launcher è stato creato come passatempo. ;)
Sono sicuro che non sarà elegante o ottimizzato, ma fa esattamente quello che cercavo.

L'obbiettivo era quello di utilizzare il mio raspberry con display osoyoo 3.5", in modo da poter visualizzare
delle schede in continuo aggiornamento.

Il programma utilizza:

- mqtt installato come docker container;
- cron per aggiornare i valori mqtt a intervalli regolari
- python per creare la maschera con tkinter e paho mqtt

E' compatibile con Python v2.x e 3.x (qualche piccola modifica), mentre sono necessari i moduli :

pip3 install setuptools
pip3 install uptime
pip3 install paho-mqtt 

L'idea è in continua evoluzione....

Dato che utilizzo regolarmente Homeassistant per la domotica casalinga, mi piacerebbe integrare questo launcher con alcuni sensori già presenti in home assistant, tramite mqtt.

Ogni minuto il raspberry esegue, con crontab:

* * * * * /bin/sh /start_sensoriraspberry.sh




