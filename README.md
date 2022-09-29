# robotrendszerek programozása

## EA4
elosztott szolgáltatások:
### [MQTT](https://mqtt.org/):

![mqtt ábra](https://mqtt.org/assets/img/mqtt-publish-subscribe.png)

[három féle üzenetküldés](https://www.techtarget.com/searchunifiedcommunications/definition/QoS-Quality-of-Service) van:
- QoS 0 - nem baj ha kiesik egy üzenet
- QoS 1 - lgealább egyszer visszaigazolás az üzenetküldésről
- QoS 2 - pontosan egyszer  érkezzen meg az üzenet

### [gRPC](https://grpc.io/)
- formalizált kontraktus
- interface definíció
- függvény prototípusok melyeket átadunk
- google adatközpontban kezdték el fejleszteni

### mások
- [corba](https://hu.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)
- []()

### [DDS](https://en.wikipedia.org/wiki/Data_Distribution_Service)
- a gRPChez hasonló
  - fizetős
  - ROS2.0 alapon free
  
### [Kafka](https://kafka.apache.org/)
- párhuzamos üzenetküldés akárp árhuzamos hardwaren
- nagy méretű csomagok küldése

### [Node-RED](https://nodered.org/)
- node.js alapú kommunikáció konffigurátor

### [maxwhere](https://www.maxwhere.com/)

### Online robotprogramozás
- műhelyben a robotra elkészítjük a programot
- könnyű robotalkalmazást fejleszetni olcsóbban

### Offline robotprogramozás
- egy virtualizált környezetben készítjük el a robot programot
- a modellben kipróbáljuk a működését
- kell hozzá:
  - logikai modell
  - geometriei modell
  - modellezésben lehet tesztelni
- a végén a műhely programozással kell végigvenni a digitális modell pontatlanságait és eltéréseit
- csökkenthető a minimális idő a projektkezdéstől a gyártásig

### közvetlen betanítás
- pont-pont működés alapján betanítás
- a kezelő által adott utasítások rögzülnek és köhögi vissza a robot
- learning by demostration: mikor a feladatokat tanítjuk be a robotnak
