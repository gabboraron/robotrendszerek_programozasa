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


## EA 5 - interpolációs módszer
### Joint space motion (*point to point motion*; *joint interpolation*)
- a robot pálya csuklótér beli lineáris interpolációval történik
- Descartesi térben csak egyenest rajzolunk a térben

![csuklomozgas példa](https://github.com/gabboraron/robotrendszerek_programozasa/blob/main/csuklomozgas_feladat.png)

ahol
```

q1 = [q1A  q2A]
q2 = [q1B  q2B]

```

A kérdés az, hogy mennyi idő alatt teljesíti a csuklótér beli mozgást

![csuklómmozgas példa vége](https://github.com/gabboraron/robotrendszerek_programozasa/blob/main/csuklomozgas_feladat2.png)

 Ezzel szemben ha cartesian térben maradok akkor a két pont között egy [pályamenti sebesség profil](https://www.linearmotiontips.com/how-to-calculate-velocity/)t (*trapezoid speed profiling*)
 
 ![páylamenti  sebesség profil](https://www.mathworks.com/help/examples/robotics/win64/DesignATrajectoryWithVelocityLimitsUsingTrapVelTrajExample_03.png)
 
[Peter Corke féle Matlab toolbox](https://petercorke.com/toolboxes/robotics-toolbox/)al modellezhető.

### information pool:
- Aktivátor szintű irányítás: mikor az impulzusok maguk fognak eljutni a kar végéig
- TOR(Task oriented robot programming): task oritned runtimban van a szemtanikus technológiai leírás -> létrejön runtimeban a robot  utasításokat -> 
- szemantikus robot képes lehet a task oriented robot programozásra 

![szemanzikus robot](http://ai.stanford.edu/blog/assets/img/posts/2020-03-17-modeling-risky-humans/image1.png)

Virca: http://www.virca.hu/

## EA 6 - UR
## EA 7 - UR + Fanuc
## EA 8 Fanuc 
- Fanuc webcontrol: https://github.com/ABC-iRobotics/fanuc-webcontrol
- fanuc webcontrol programozás natívan: https://github.com/ABC-iRobotics/fanuc-webcontrol/tree/master/karel

## EA 9 robodk
## EA 10 ROS
## ROS1 
debian alapon: https://wiki.ros.org/noetic

`/opt/ros/noetic`

- workspace 
  - package 
    - node1
    - node2
    - ...

`roscore`-> `ROS launch` file amivel a nodeok indíthatóak

- `catkin create pkg [packagename] [dependency]`
- `catkin node`

### noetic
![node-master communication](https://adityakamath.github.io/assets/img/ros_master_node_topic.png)

ROS master -> ROS node 
 -> node1: publish topic1
 -> node2: subscribe topic2

Minden node több topicba is tud publikálni, de előbb a masternél feliratkozik rá, és szolgáltatásokat végezhet/kérhet le, pl: subscribe, publish

## ROS2 
debian alapon: https://docs.ros.org/en/humble/

`/opt/ros/humble`

- workspace 
  - package 
    - node1
    - node2
    - ...

`ros2 launch package launch.py` file amivel a nodeok indíthatóak

`ros2 pkg [packagename] [dependency]`

### Humble
![ros2 communication](https://i.ytimg.com/vi/aeOS9xqblrg/maxresdefault.jpg)

Csak azonos hálózaton kell legyenek a nodeok és a kommunikáció megoldott a nodeok között, csak az alap beállításokat módosítani kell. 

https://www.youtube.com/watch?v=aeOS9xqblrg


subscribe példa: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29


összeköthető rvizel is, ami egy robotvizualizációs eszköz


