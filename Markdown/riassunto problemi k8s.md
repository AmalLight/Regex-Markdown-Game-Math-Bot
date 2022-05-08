# Tabella

|  Voce della Colonna | Descrizione della Colonna |
| --- | --- |
| Nome dell'Autore | Mohammad |
| Cognome dell'Autore | Fumagalli Tahboub |
| Versioni Testate di Kubernetes | yyy |
| Data di oggi | zzz |
| Destinatari del Documento | xxx |

---
# Leggenda

1. [Autore](#tabella)

2. [Problematiche più importanti](#importante)

3. [Problematiche meno importanti](#rilevante)

4. [Criticità](#considerevole)

---
# Importante

###### per aggiornamenti al sistema si intende per esempio il passaggio dalla versione a alla versione b di tutto l'intero cluster kubernetes .

  1. Gli aggiornamenti al sistema kubernetes non sono attualmente automatici.
Anche con gli attuali playbook scritti spesso c'è bisogno di un intervento manuale per il ripristino di tutte le funzionalità: pod , servizi , connessioni , ecc..

  2. Attualmente gli aggiornamenti al sistema kubernetes [^3] causano un disservizio che in media è quantificabile sui 30 minuti .

  3. il Master va potenziato gli servono più di 8gb di ram .

---
# Rilevante

  1. non è possibile fare un riavvio delle macchine [^2] avendo la certezza che l'infrastruttura kubernetes sarà ripristinata correttamente in automatico .
Con questo è da intendersi che spesso serve un intervento manuale per il ripristino completo dei pods e dei servizi ad essi associati [^1] .

  2. Attualmente il riavvio delle macchine [^2] causa un disservizio che in media è quantificabile sui 30 minuti .

  3. Per quanto riguarda i singoli componenti è importante dire che l'installazione che viene fatta con helm presenta delle problematiche di disinstallazione .
Attualmente per la fase di sviluppo e di test in cui spesso la disinstallazione è la strada più veloce per capire dove risieda un problema di un certo gruppo di componenti,
vengono usati semplici script bash per la rimozione completa delle precedenti parti prima considerate .
Questo rende difficile capire ( e penso che sia una criticità di kubernetes ) se il tutto è stato fatto al meglio .
Per intendersi meglio l'effetto voluto sarebbe quello di ottenere un istanza kubernetes precedente all'installazione delle precedenti parti prima considerate .
Non avere certezza di ciò può essere rischioso nel futuro .

---
# Considerevole

  1. Possibili tentativi di Hacking per versioni mantenute obsolete .
  2. Pochi ambienti diversificati ( con le stesse prestazioni elevate ) per i lavori di sviluppo e di test .
  3. I malfunzionamenti dei singoli pod e componenti si propagano con malfunzionamenti in buona parte del cluster kubernetes ( per diverse ragioni [^4] ) .
  4. Sospetto che kubernetes vada spesso in loop quando va in crash ( per diversi motivi [^5] ) , pertanto tende a consumare tutte le risorse disponibili come se fosse entrato un ciclo while di programmazione .
Questo aspetto andrebbe approfondito poiché sicuramente si può controllare e risolvere ma è pericoloso lasciare che il Go ( il principale linguaggio di programmazione usato per programmare Kubernetes ) si auto gestisca in caso di loop e di crash .

---
# Le Note

[^1]: Questa procedura non viene eseguita spesso ma è comunque da tenerne in considerazione .
[^2]: Per il riavvio delle macchine in questo caso si intende più specificatamente l'intera operazione di drain e uncordon per master e workers ( worker 1 2 e 3 ) .
[^3]: Gli aggiornamenti al sistema kubernetes comprendono anche l'intera procedura di drain e uncordon per master e workers .
[^4]: Le diverse ragioni possono essere: 1° questi pod/servizi vengono considerati in altri pod/servizi , 2° altri pod/servizi monitorano l'intero andamento del cluster kubernetes .
[^5]: I diversi motivi possono essere: 1° un componente richiede maggiori risorse , 2° un processo ha un picco di richieste per avere maggiori risorse . In entrambi i casi kubernetes prova a liberare delle risorse che non ha o che non ha preventivato ( poi però deve riconcederle a chi le ha tolte ) , e così si crea un circolo vizioso .