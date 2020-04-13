# rpi-dashboard

Devo fare una premessa: non sono un programmatore e questo launcher è stato creato come passatempo. ;)
Sono sicuro che non sarà elegante o ottimizzato, ma fa esattamente quello che cercavo.

L'obbiettivo era quello di utilizzare il mio raspberry con display osoyoo 3.5", in modo da poter visualizzare
delle schede in continuo aggiornamento. Potevo farlo con homeassistant e la sua pagina web, ma chromium funziona veramente male su un display di piccole dimensioni, e le prestazioni sono scarse. Con un futuro display da 7 pollici potrò pensare ad una interfaccia con pulsanti e molte più etichette. Il tema dark è necessario per una migliore visibilità.

Il programma attualmente pubblicato ha bisogno di:

- mqtt server installato come docker container (o installato direttamente nel raspberry);
- mqtt client installato (sudo apt-get install mosquitto-clients)
- cron per aggiornare i valori mqtt a intervalli regolari
- python per creare la maschera con tkinter e paho mqtt

E' compatibile con Python v2.x e 3.x (qualche piccola modifica), mentre sono necessari i moduli :

pip3 install setuptools
pip3 install paho-mqtt 

Ogni minuto il raspberry esegue, con crontab:

/bin/sh /start_sensoriraspberry.sh

L'idea è in continua evoluzione: ora punterò ad integrarlo con homeassistant per creare un pannello di comando casalingo non basato su web, per i motivi già indicati in precedenza.

Le schede che vedete sono di esempio, tramite mqtt si può inserire qualsiasi risultato proveniente da riga di comando:

- sensori raspberry, 
- dati provenienti da siti internet usando curl, 
- sensori mqtt da dispositivi tasmota
- altri sensori utilizzando homeassistant come piattaforma principale (raccoglie al suo interno una infinità di plugins), e tramite la sua configurazione pubblicare topics su mqtt.

Dato che utilizzo regolarmente Homeassistant per la domotica casalinga, mi piacerebbe integrare questo launcher con alcuni sensori già presenti in home assistant, tramite mqtt.






