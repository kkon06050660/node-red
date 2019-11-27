[{"id":"804cef09.96c76","type":"tab","label":"Flow 1","disabled":false,"info":""},
{"id":"af69173a.5b67b8","type":"rpi-gpio out","z":"804cef09.96c76","name":"Green LEDoooooo","pin":"11","set":true,"level":"0","freq":"","out":"out","x":670,"y":280,"wires":[]},
{"id":"adde0603.9fff88","type":"debug","z":"804cef09.96c76","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":410,"y":80,"wires":[]},
{"id":"23876064.d01bd","type":"rpi-gpio in","z":"804cef09.96c76","name":"Button12","pin":"7","intype":"up","debounce":"25","read":true,"x":130,"y":260,"wires":[["adde0603.9fff88","a23c6477.2acf88"]]},
{"id":"a23c6477.2acf88","type":"switch","z":"804cef09.96c76","name":"if input is 1","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"1","vt":"str"},
{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":290,"y":280,"wires":[["eeae47f.9abb0b8"],["b27195fc.12e148"]]},
{"id":"eeae47f.9abb0b8","type":"change","z":"804cef09.96c76","name":"Change to 0","rules":[{"t":"set","p":"payload","pt":"msg","to":"0","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":470,"y":240,"wires":[["af69173a.5b67b8"]]},
{"id":"b27195fc.12e148","type":"change","z":"804cef09.96c76","name":"Change to 1","rules":[{"t":"set","p":"payload","pt":"msg","to":"1","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":470,"y":320,"wires":[["af69173a.5b67b8"]]}]

