[{"id":"1ee7a934.0b87c7","type":"tab","label":"set_LED","disabled":false,"info":""},
{"id":"5e4d23f9.c86d4c","type":"http in","z":"1ee7a934.0b87c7","name":"Set GPIO_5","url":"/setgpio5","method":"get","upload":false,"swaggerDoc":"","x":190,"y":400,"wires":[["e9794136.d371a","547f2f1f.06883"]]},
{"id":"e9794136.d371a","type":"function","z":"1ee7a934.0b87c7","name":"Set to 1","func":"msg.payload = 1\nreturn msg;","outputs":1,"noerr":0,"x":400,"y":420,"wires":[["28cd9a1e.127176"]]},
{"id":"28cd9a1e.127176","type":"rpi-gpio out","z":"1ee7a934.0b87c7","name":"","pin":"29","set":"","level":"0","freq":"","out":"out","x":560,"y":380,"wires":[]},
{"id":"547f2f1f.06883","type":"function","z":"1ee7a934.0b87c7","name":"Return Status","func":"msg.payload=\"GPIO_5 set to HIGH\"\nreturn msg;","outputs":1,"noerr":0,"x":420,"y":520,"wires":[["79282e1f.bf756","ca56f913.e13b98"]]},
{"id":"79282e1f.bf756","type":"http response","z":"1ee7a934.0b87c7","name":"","statusCode":"","headers":{},"x":730,"y":380,"wires":[]},
{"id":"ca56f913.e13b98","type":"debug","z":"1ee7a934.0b87c7","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":930,"y":380,"wires":[]},
{"id":"bdeb09b4.b04ca8","type":"http in","z":"1ee7a934.0b87c7","name":"Clear GPIO_5","url":"/clear5","method":"get","upload":false,"swaggerDoc":"","x":190,"y":360,"wires":[["1a33023a.cb49de","37220ee9.13bfe2"]]},
{"id":"1a33023a.cb49de","type":"function","z":"1ee7a934.0b87c7","name":"Clear to 0","func":"msg.payload = 0\nreturn msg;","outputs":1,"noerr":0,"x":400,"y":340,"wires":[["28cd9a1e.127176"]]},
{"id":"37220ee9.13bfe2","type":"function","z":"1ee7a934.0b87c7","name":"Return Status","func":"msg.payload=\"GPIO_5 set to LOW\"\nreturn msg;","outputs":1,"noerr":0,"x":420,"y":240,"wires":[["79282e1f.bf756","ca56f913.e13b98"]]}]

