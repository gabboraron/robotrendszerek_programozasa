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


## EA5 - moduláris bobotszoftverek 
> - alacsony késleltetésű nagy sávszélű hálózatok
> - elosztott szoftverrendszerek
> - felhő alapú számítások
> - LiDARok, térérzékelés, kinect
> - VR / AR
> - fogalmi szintű következtetés, ontológiák, nlp
> - gépi tanulás
> - akkumlátor technológiák

- http://www.robothalloffame.org/
- https://everydayrobots.com/
- https://www.unlimited-robotics.com/
- https://www.flr.io/

komponens rendszerek:
- Robot Technology Middleware: 
  - https://www.corba.org/
  - [RTC 1.1](https://www.omg.org/spec/RTC/1.1/About-RTC/)
  - point-point komunikációs modell
  - name service IP címre küldhető adatfolyamok
- [microsoft robotics developer studio](https://en.wikipedia.org/wiki/Microsoft_Robotics_Developer_Studio)
  - SOAP
  - statefull kapcsolatra épít
  - 2015-ben leállt
- ROS
  - XMLRPC http://wiki.ros.org/xmlrpcpp
  - tipizált topicok
  
moduláris keretrendsterek kommunikációi:
 - data flow
   - egyirányú
   - pipeline
   - ROS-ban publish-subscribe filozófián alapul
 - remote procedure call
   - a fogyasztó használja a szolgáltató általa adott szolgáltatásokat
   - szerializáltan történik
   - adattípusok és interfészek nyelvfüggetlen kódolása
   - [protocol buffer](https://developers.google.com/protocol-buffers)
   - felhasználás pl: adatstreamek [visual servoingnál](https://en.wikipedia.org/wiki/Visual_servoing)

komponensk keretrendszerke kapcsialktait tekintve a ROS és az RTM kapcsolatai megfeleltethetőek egymásnak

Interface definition language ([IDL](https://www.techtarget.com/whatis/definition/IDL-interface-definition-language))

![ ROS Services kapcsolatok](https://answers.ros.org/upfiles/13283489446262677.jpg)

![socket - lollipop](https://openrtm.org/openrtm/sites/default/files/1681/provider_and_consumer_en.png)

### ROS1 VS ROS2
| ROS1 |ROS2 |
|:----:|:----:|
| ros core | [DDS](https://design.ros2.org/articles/ros_on_dds.html) - service discovery, interoparibilitás |
| ros modulok -> paraméter szerver | ros modulok -> leterjednek a változtatások a nodeokba a paraméter szerverből |

